void setup() {
  // put your setup code here, to run once:
  setupButton();
  setupLED();
  setupMessage();
}

void loop() {
  // put your main code here, to run repeatedly:
  Lab1();
}

void Lab1_c2(){
  if(getButton() == LOW){
    addTimer();
    delay(100);
  }
  else{
    runTimer();
  }
}
