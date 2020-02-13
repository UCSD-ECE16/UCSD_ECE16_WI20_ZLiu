int ms=0;
int timer_seconds = 0;
int button_val; 
int flag = 0; 


void setup() {
  setupLED();
  setupButton();
  setupMessage();
  Serial.begin(115200);
}

void loop() {
  //condition1();
  //condition2();
  //condition3();
  //condition4();
  //condition5();
  //condition6();
  Lab1_C2(); //call the Lab1 Challenge function  
  //Serial.println(timer_seconds);
  //delay(1000);
  //Serial.println(button_val);
  //ms = millis();
  //Serial.println(ms);
}

void Lab1_C2(){
  button_val = getButton();
  if(button_val == 0 && flag == 0) {
    addTimer();
    Serial.println(timer_seconds);
    // runTimer();
    delay(1000);
  }
  else if(button_val == 1) {
    runTimer();
  }
}

void Lab3(){
  sendData();
}
