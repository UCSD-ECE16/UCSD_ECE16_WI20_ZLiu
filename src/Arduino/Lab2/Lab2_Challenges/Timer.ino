
// ========== Timer Code ========= // 
void stateMachineTimer(){
  
  if (timer_state == 0){
    showMessage("State 0", 1, true);
    //initDisplay();
    //delay(3000);
    detectTap();
    if (detectTap() == true){
      timer_state = 1;
      delay(100);
    }
  }
  else if (timer_state == 1){  
    addTimerOLED();
    delay(500);
    if(detectTap()){
      time_last_tap = millis();
    }
    
    
    
    if (millis() - time_last_tap > 3000){
      timer_state = 2;
      //showMessage("State 2", 1, true);
    }
  }
  else if (timer_state == 2){
    showMessage("State 2", 1, true);
    //while(timer_seconds > 0){
    runTimerOLED();
    if(timer_seconds == 0){
      showMessage("counting finished", 1, true);
      timer_state = 3;
    }
    
  }
  else if (timer_state == 3){
    
    showMessage("State 3", 1, true);
    setupMotor();
    buzzMotor(255);
    delay(3000);
    if (detectTap() == true){
      buzzMotor(0);
      timer_state = 0;
      delay(500);
    }
  }
}


// ========== Timer Code ========= // 
void runTimerOLED(){
  char message_buffer_countdown[4];
  while(timer_seconds > 0){     
    timer_seconds = timer_seconds - 1;
    delay(1000);
    // print to OLED instead of Serial.
    String stringTime = String(timer_seconds); //convert timer_seconds to string
    stringTime.toCharArray(message_buffer,4); //convert string to char buffer
    // show message_buffer with showMessage
    showMessage(message_buffer, 1, true);
    }
}
