

void setup() {
  Serial.begin(115200);
  // put your setup code here, to run once:
  setupButton();
  setupLED();
  setupMessage();
  setupMotor();
  setupADC();
  initDisplay();
}

void loop() {
  Lab3();
}

void Lab1(){
  // put your main code here, to run repeatedly:
  if(getButton() == LOW){
    addTimer();
    delay(1000);
  }
  else{
    runTimer();
  }
}

void Lab2_C1(){
  buzzMotor(true);
  delay(1000);
  buzzMotor(false);
  delay(1000);
}

void Lab2_C2(){
  if (detectTap){
    addTimer();
  }
}

void Lab2(){
  stateMachineTimer();
}

void Lab3_Tutorial(){
  receiveMessage();
}


void Lab3(){
  receiveMessage();
  sendData();
}
