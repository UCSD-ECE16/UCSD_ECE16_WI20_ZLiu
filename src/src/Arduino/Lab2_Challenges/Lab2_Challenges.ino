void setup() {
  // put your setup code here, to run once:
  setupButton();
  setupLED();
  setupMessage();
  setupMotor();
  setupADC();
  initDisplay();
}

void loop() {
  Lab2_C6();
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
  buzzMotor(0);
  delay(1000);
  buzzMotor(127);
  delay(1000);
  buzzMotor(255);
  delay(1000);
}

void Lab2_C2(){
  if (detectTap){
    addTimer();
  }
}

void Lab2_C6(){
  stateMachineTimer();
}
