''' 
Primarily this class keeps the connection to Arduino and Red relays
together for bow
There are six commands that are being used for now
'F' for Forward
'B' for Backward
'L' for Left
'R' for Fight
'N' for none command

All the commands are supplied with number of the millis
that a command is being executed, The command name and associated number
are separated by comma like this: F,1500
The commands 'U" and 'N' should be supplied with zero as duration, like:
U,0 
aDuration - command duration in millis

aSkipNumber - number of skips (RedRelay off) during command execution if 
              it is negative then that it is applied to the left part
              otherwise it is the right side. If it is zero then no 
              skips are applied to neither side
              
aSkipDuration - black out duration while the command is executing 

'''

from ArduinoConnection import ArduinoConnection
from RedRelay import RedRelay
import threading
import time

RED_RELAY_LEFT  = 4
RED_RELAY_RIGHT = 5

class ChassisCommand:
	command = "N" # Originaly it is 'None'
	arduinoConnection = None
	redRelay4         = None
	redRelay5         = None
	duration          = 0
	
	def __init__(self,
				anArduinoConnection,
				aRedRelay4, # Controls the right positioned motors
				aRedRelay5): # Controls the left positioned motors
		self.arduinoConnection = anArduinoConnection
		self.redRelay4         = aRedRelay4
		self.redRelay5         = aRedRelay5
		
		
	def execute(self, aDuration):
		self.duration = aDuration
		self.arduinoConnection.send(self.command, aDuration)

		
	def undo(self):
		raise Exception("'undo' is not implemented in base class please use any decendent class")
		

class ChassisForward(ChassisCommand):
	command = "F" # Going forward
	def undo(self):
		return ChassisBackward(self.arduinoConnection, 
							self.redRelay4, 
							self.redRelay5)
	
	
class ChassisBackward(ChassisCommand):
	command = "B" # Going forward
	def undo(self):
		return ChassisForward(self.arduinoConnection, 
							self.redRelay4, 
							self.redRelay5)
		
class ChassisTurnRight(ChassisCommand):
	command = "R" # Going right
	def undo(self):
		return ChassisTurnLeft(self.arduinoConnection, 
							self.redRelay4, 
							self.redRelay5)
		
class ChassisTurnLeft(ChassisCommand):
	command = "L" # Going left
	def undo(self):
		return ChassisTurnRight(self.arduinoConnection, 
							self.redRelay4, 
							self.redRelay5)

		
if __name__ == '__main__': # Testing at least one command to go all way
	import RPi.GPIO as GPIO	
	GPIO.setmode(GPIO.BCM) # satisfying relay's pre-condition

	duration = 8
	command = "F"
	relay4 = RedRelay(4)
	relay4.on()
	relay5 = RedRelay(5)
	relay5.on()
	arduinoConnection = ArduinoConnection()

	cf = ChassisForward(arduinoConnection,relay4, relay5)
	cf.execute(duration)
	relay4.off()
	relay5.off()
	
