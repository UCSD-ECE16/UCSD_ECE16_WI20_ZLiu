
void addTimer(){
  // add one to timer_seconds
  timer_seconds = timer_seconds + 1;
  }

void runTimer(){
  flag = 1;
  while(timer_seconds > 0){
    // minus one second from the timer_second
    timer_seconds = timer_seconds - 1;
    // print the time with printTime(int)
    printTime(timer_seconds);
    // wait a second 
    delay(1000);
  }
  if(timer_seconds == 0){
    printTime(timer_seconds);
    delay(1000);
  }
  flag = 0;
}
