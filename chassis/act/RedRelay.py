''' There are two red relayes currently engaged into the process
The upper relay that controls the wheels #3 and #4 simultaneously
is linked with RPi GPIO #4
The lower red relay that controls the wheels #1 and #2 together
is connected with RPi GPIO #5

You can use these relays for safety purposes in case the Arduino
connection is broken or you would want the wheels to slow down
by mwans of sending short electrical impulses rather than
having one continuous current 

Precondition: The following settings must be executed before
calling the Relay's constructor:

		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)

'''

import RPi.GPIO as GPIO
import time

class RedRelay:
	onOff = False
	pinNumber = 0
# Currently pinNumber can be either 4 that controls motors 3 and 4 and 
# valie 5 that controls motors 1 and 2 (left side)	
	def __init__(self, aPinNumber):
		GPIO.setup(aPinNumber, GPIO.OUT)
		self.pinNumber = aPinNumber
		
	def on(self):
		if(self.onOff): return
		self.onOff = not(self.onOff)
		GPIO.output(self.pinNumber, self.onOff)
		self.onOff = True

	def off(self):
		if(not(self.onOff)): return
		self.onOff = not(self.onOff)
		GPIO.output(self.pinNumber, self.onOff)
		self.onOff = False
		
	def isOn(self):
		return self.onOff
	
	def isOff(self):
		return not(self.OnOff)
		
# Small relay's test you can look under the hood to see the upper and 
# lower red relay's to switch on and off		
if __name__ == '__main__':  
	GPIO.setmode(GPIO.BCM)

	relay4 = RedRelay(4) #Upper
	relay4.on()
	time.sleep(21)
	relay4.off()
	
	time.sleep(8)

	relay5 = RedRelay(5) #Lower
	relay5.on()
	time.sleep(21)
	relay5.off()

