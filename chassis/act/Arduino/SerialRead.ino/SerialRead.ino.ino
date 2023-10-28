
/* The relay based swapper. It takes a command from the serial port. The command format shoud be N,D 
where "N" number of millis command is being executed. It is a name of command that is a charecter as follows:

"F" - goes forward
"B - goes backward 
"L" - turning left
"R" - turning right

Examples: "F,3000" - moving forward for three seconds
          "L,10" - moving left for one hundred's of a second "pivital turn"

Result is either 'ok' or 'error: <Explanation>'
          "F,abcd" - "error: cannot convert 'abcd' into a number
          "S,1200  - "error: unknown command 'S'
          "L,25" - ok          

*/
 
int inByte = 0;
bool flag = false;
int RELAY_1 = 7;
int RELAY_2 = 6;
int RELAY_3 = 5;
int RELAY_4 = 4;


void setup() {
  // start serial port at 9600 bps:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(4, OUTPUT); // Relay 4
  pinMode(5, OUTPUT); // Relay 3
  pinMode(6, OUTPUT); // Relay 2
  pinMode(7, OUTPUT); // Relay 1 

  
}

void loop() {
  while (Serial.available() == 0) {}     //wait for data available
  String commandAndVal = Serial.readString();  //read until timeout
  commandAndVal.trim();                        // remove any \r \n whitespace at the end of the String
  if (commandAndVal.startsWith("B,")) { // going backward
    commandAndVal.replace("B,", "");
    // If 'F' (meaning 'Forwards'); switching the relay 1 and 3 on 
    digitalWrite(RELAY_2, HIGH); // Relay 2 switches ON
    digitalWrite(RELAY_3, HIGH); // Relay 3 switches ON
    // All the rest should be zero
    digitalWrite(RELAY_1, LOW);  // Relay 1 should stay LOW
    digitalWrite(RELAY_4, LOW);  // Relay 4 should stay low
    
    delay(commandAndVal.toInt()); // Keeping the relays 1 and 3 running for some time
     
    // Swiching all relays 7 and 5 into LOW   
    digitalWrite(RELAY_2, LOW); // Relay 1 is moving back to the "LOW" positio
    digitalWrite(RELAY_3, LOW);  // Relay 5 moving back to the "LOW" position
    Serial.print("Ok");
  } else if(commandAndVal.startsWith("F,")) { // going backward
    commandAndVal.replace("F,", "");
    // If 'F' (meaning 'FORWARD') switching the relay 2 and 4 on 
    digitalWrite(RELAY_1, HIGH); // Relay 1 switches ON
    digitalWrite(RELAY_4, HIGH); // Relay 4 switches ON
    // All the rest should be zero
    digitalWrite(RELAY_2, LOW);  // Relay 2 should stay LOW
    digitalWrite(RELAY_3, LOW);  // Relay 3 should stay low
    
    delay(commandAndVal.toInt()); // Keeping the relays 1 and 3 running for some time
     
    // Swiching all relays 1 and 4 into LOW   
    digitalWrite(RELAY_1, LOW); // Relay 1 is moving back to the "LOW" position
    digitalWrite(RELAY_4, LOW);  // Relay 4 moving back to the "LOW" position
    Serial.println("Ok");
  } else if(commandAndVal.startsWith("R,")) { // Turning right pivotal clock wise
    commandAndVal.replace("R,", "");
    // If 'R' (meaning 'RIGHT') switching the relay 2 and 4 on 
    digitalWrite(RELAY_2, HIGH); // Relay 4 switches ON
    digitalWrite(RELAY_4, HIGH); // Relay 4 switches ON

    digitalWrite(RELAY_1, LOW); // Relay 1 stays OFF
    // All the rest should be zero
    digitalWrite(RELAY_3, LOW);  // Relay 3 stays LOW
    
    delay(commandAndVal.toInt()); // Keeping the relays 1 and 3 running for some time
     
    // Swiching all relays 4 and 2 into LOW   
    digitalWrite(RELAY_2, LOW); // Relay 4 is moving back to the "LOW" position
    digitalWrite(RELAY_4, LOW);  // Relay 2 moving back to the "LOW" position
    Serial.println("Ok");
  } else if(commandAndVal.startsWith("L,")) {
    commandAndVal.replace("L,", "");
    digitalWrite(RELAY_1, HIGH); // Relay 1 switches ON
    digitalWrite(RELAY_3, HIGH); // Relay 3 switches ON

    digitalWrite(RELAY_2, LOW); // Relay 2 stays OFF
    // All the rest should be zero
    digitalWrite(RELAY_4, LOW);  // Relay 4 stays LOW
    
    delay(commandAndVal.toInt()); // Keeping the relays 1 and 3 running for some time
     
    // Swiching all relays 4 and 2 into LOW   
    digitalWrite(RELAY_1, LOW); // Relay 1 is moving back to the "LOW" position
    digitalWrite(RELAY_3, LOW);  // Relay 3 moving back to the "LOW" position
    Serial.println("Ok");
  } else if(commandAndVal.startsWith("N,")) { // None. Idle command that does not change any motor state 
    commandAndVal.replace("N,", "");
    delay(commandAndVal.toInt()); // Just delaying for no reasonS
    Serial.println("Ok");
  } else {
    Serial.println("Error: Command does not exist "+commandAndVal);
  }

  
    
}
