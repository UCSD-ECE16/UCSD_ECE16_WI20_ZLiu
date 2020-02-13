


int red_led = 26;
int yellow_led = 27;
int blue_led = 13;

void setupLED()  {
  pinMode(red_led, OUTPUT);
  pinMode(yellow_led, OUTPUT);
  pinMode(blue_led, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(115200);
}

void condition1(){
  // blink the builtin led for the frequency of 1Hz, which means blinks once in 1s=1000ms. 
  digitalWrite(LED_BUILTIN, HIGH);
  delay(10);
  Serial.println("LED is lighted up");
  digitalWrite(LED_BUILTIN, LOW);
  Serial.println("LED is darked down");
  delay(990);
}
void condition2(){ 
  // blink the builtin led for the frequency of 10Hz, which means blinks once in 0.1s=100ms. 
  digitalWrite(LED_BUILTIN, HIGH);
  delay(10);
  digitalWrite(LED_BUILTIN, LOW);
  delay(90);
}
void condition3(){
  // blink the builtin led for the frequency of 50Hz, which means blinks once in 1s=20ms. 
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1);
  digitalWrite(LED_BUILTIN, LOW);
  delay(19);
}
void condition4(){ 
  //1s/100ms for the Red LED
  digitalWrite(red_led, HIGH);
  delay(1*1000);
  digitalWrite(red_led, LOW);
  delay(100);
}
void condition5(){ 
  //200ms/50ms for the Yellow LED
  digitalWrite(yellow_led, HIGH);
  delay(200);
  digitalWrite(yellow_led, LOW);
  delay(50);
}
void condition6(){ 
  //20ms/10ms for the Blue LED
  digitalWrite(blue_led, HIGH);
  delay(20);
  digitalWrite(blue_led, LOW);
  delay(10);
}
