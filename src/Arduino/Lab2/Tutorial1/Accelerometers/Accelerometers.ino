int accelZ = A0;


void setup() {
  pinMode(accelZ, INPUT);
  Serial.begin(9600);

}

void loop() {
  // read the current voltage at the pin 
  int accel_val = analogRead(accelZ);
  // Serial.print("the acceleration is ");
  Serial.println(accel_val);
  delay(20);
}
