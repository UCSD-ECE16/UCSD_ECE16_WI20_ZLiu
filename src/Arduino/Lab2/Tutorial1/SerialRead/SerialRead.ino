

void setup() {
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps 
  // check if something came on the serial port with:

}

void loop() {
  if (Serial.available() > 0){
    

  char incomingChar = Serial.read();
  Serial.print(incomingChar);
  }
}
