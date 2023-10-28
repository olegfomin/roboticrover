# The robotic rover project
The goal of the project is to create a universal, simple, robust robotic
chassis that can be controlled over internet by a human operator who
can issue commands over the web interface or in the near future be a
completely autonomous cart being controlled by AI located inside AWS
or any other capable cloud solution. The web-server where all the 
audiable and visual information from the chassis is fed shall be able
to generate the list of simple commands that chassis can simply execute.
The chassis should be a wheeled platform you can put any other equipment
on. The chassis will include servo mechanism controller leaving four
outlets for any servos to be hooked on with.

# The current projects content
* The sample implementation of the web-site that shows a sand-box area
for the robot to play on.
* The UI Java-Script file that will show a tennis court for now. This
can be used to transport a tennis ball cannon around or for the vacuum 
cleaner to move it to and fro across the court
* The python software for the robot that is currently has
** 4 omni-directional wheels attached to 20W DC motor each
** Web-camera with pan/tilt servo mechanisms
** Microphone attached to the same support plate as the camera
** Good lythium 10A/H battery that is currently mounted on the top of
the chassis. In future models of the robot the battery should come down
because it is quite heavy
** Raspberry Pi micro controller to where web-cam and microphone are
connected and that is supposed to be connected to the
cloud all the time but can make simple decisions itself when the 
link with a cloud is broken
** Raspberry Pi also responsible for counting the number of revolutions
each of four wheels makes with the help of hall-effect sensors also
attached to the chassis 
** Arduino is currently only reslonsible for switching on and off
the set of four relays that define the dirrection and duration 
all the wheels are turning to
** Number of DC voltage buck-down regulators
  
