int timer_seconds = 0;

void addTimer(){
  timer_seconds++;
  printTime(timer_seconds);
}

void runTimer(){
  while(timer_seconds > 0){
    timer_seconds--;
    printTime(timer_seconds);
    delay(1000);
  }
}
