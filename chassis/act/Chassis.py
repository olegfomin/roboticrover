''' The top level class that serves as a convenient facade and at
the same time it is capable to get the list of commands and execute
them one by one. It can also undo/rollback the list
of commands that was just commited by this class '''



import time
import serial
from RedRelay import RedRelay
from ArduinoConnection import ArduinoConnection
from ChassisCommand import ChassisForward
from ChassisCommand import ChassisBackward
from ChassisCommand import ChassisTurnLeft
from ChassisCommand import ChassisTurnRight

import RPi.GPIO as GPIO

class Chassis:
	
	executionList = []
	revocationList = [] # Contains the latest list just commited
	
	def __init__(self): 
		self.arduinoConnection = ArduinoConnection("/dev/ttyACM0", 9600) 
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		self.redRelay4	= RedRelay(4) # Controls the right positioned motors
		self.redRelay5	= RedRelay(5) # Controls the left positioned motors
		self.enableRelays()
		
	def enableRelays(self):
		self.redRelay4.on()
		self.redRelay5.on()
		
	def disableRelays(self):
		self.redRelay4.off()
		self.redRelay5.off()
		
# Puts forward commands and duration tuple into the execution list
	def forward(self, duration):
		self.executionList.append((ChassisForward(self.arduinoConnection, 
												self.redRelay4, 
												self.redRelay5), 
												duration))

# Puts backward commands and duration tuple into the execution list
	def backward(self, duration):
		self.executionList.append((ChassisBackward(self.arduinoConnection, 
												self.redRelay4, 
												self.redRelay5), 
												duration))

# Puts turnLeft commands and duration tuple commands into the execution list
	def turnLeft(self, duration):
		self.executionList.append((ChassisTurnLeft(self.arduinoConnection, 
												self.redRelay4, 
												self.redRelay5),
												duration))

# Puts turnRight commands and duration tuple commands into the execution list
	def turnRight(self, duration):
		self.executionList.append((ChassisTurnRight(self.arduinoConnection, 
												self.redRelay4, 
												self.redRelay5), 
												duration))
		
# Execute all commands gathered inside executionList
	def commit(self):
		for commandAndDuration in self.executionList:
			command  = commandAndDuration[0]
			duration = commandAndDuration[1]
			command.execute(duration) 
		self.revocationList = self.executionList	
		self.executionList = []
# Revokes all the immediatelly commited commands		
	def revoke(self):
		for commandAndDuration in self.revocationList:
			command  = commandAndDuration[0].undo()
			duration = commandAndDuration[1]
			command.execute(duration) 
		self.revocationList = []	

			
# Swithcing all the red relays off		
	def __del__(self):
		self.disableRelays()
		
if __name__ == '__main__':
		 chassis = Chassis()
		 chassis.turnRight(5)
		 chassis.commit()
		 chassis.revoke()

