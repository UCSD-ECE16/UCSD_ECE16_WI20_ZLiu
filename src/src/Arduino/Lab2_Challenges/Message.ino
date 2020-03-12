//Message VARs
char in_text[20];                // Character buffer
int in_text_index = 0;

void setupMessage(){
  Serial.begin(115200);
}

void printTime(int seconds){
  Serial.println(seconds);
}


void receiveMessage(){
  if (Serial.available() > 0) {
    char incomingChar = Serial.read();
    if (incomingChar == '\n'){
      showMessage(in_text,1,true);
      in_text_index = 0;
      memset(in_text,0,20);
    }
    else{
      in_text[in_text_index] = incomingChar;
      in_text_index++;
    }
  }
}
