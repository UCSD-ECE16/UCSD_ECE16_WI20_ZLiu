


// ======== ADC Code ======== //
void setupADC(){
  //setup each accel pins to be an input pin
  pinMode(accelZ, INPUT);
  pinMode(accelY, INPUT);
  pinMode(accelX, INPUT);

}
void readADC(){
  //read each accel pin and assign value to the corresponding Val
  accelZ_Val = analogRead(accelZ);
  accelX_Val = analogRead(accelX);
  accelY_Val = analogRead(accelY);
}
void printADC(){ //print the ADC values
  Serial.print("Z:");
  Serial.print(accelZ_Val);
  Serial.print(",");
  Serial.print("Y:");
  Serial.print(accelY_Val);
  Serial.print(",");
  Serial.print("X:");
  Serial.println(accelX_Val);
}
