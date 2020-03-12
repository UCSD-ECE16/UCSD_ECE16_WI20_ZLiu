void setupMessage(){
  Serial.begin(9600);
}

void printTime(int seconds){
  Serial.println(seconds);
}
