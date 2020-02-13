

void setup() {
  Serial.begin(115200); //set baud rate to 115200
}

void loop() {
  Serial.print("Hello World");
  Serial.println("!!!");
  delay(1); //wait a little to not overwhelm the serial communication
}
