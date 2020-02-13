


/*


int i = 1;
// ==== Message CODE ====== // 
void receiveMessage(){
  
  if (SerialBT.available() > 0) {
    char incomingChar = SerialBT.read();   // read byte from serial     
    if (incomingChar == '\n'){
      initDisplay();
      showMessage(in_text, 1, true);
    //show the in_text with show message 
    //reset the in_text index back to 0
    checkMessage();
    memset(in_text,0,20); // this will clear the in_text buffer
    idx = 0;
    }
    else{
      in_text[idx] = incomingChar;
      //assign in_text[index] to the incoming char
      //increment the index     
      idx++; 
      }
    }
}

int sampling_rate = 50;   //sampling rate in Hz
unsigned long sampling_delay = calcSamplingDelay(sampling_rate);   //microseconds between samples
unsigned long last_sample_time = 0;   //microsecond of last sample

bool sending_data = false; //to send data?

void sendData(){
    if(sending_data){
        if(micros()-last_sample_time >= sampling_delay){
            last_sample_time = micros();
            SerialBT.print("The last sample time is");
            readADC();
            SerialBT.print(last_sample_time);
            SerialBT.print(',');
            SerialBT.print(accelX_Val);
            SerialBT.print(',');
            SerialBT.print(accelY_Val);
            SerialBT.print(',');
            SerialBT.println(accelZ_Val);
        }
    }
}

long calcSamplingDelay(long sampling_rate){
    return 1000000/sampling_rate;//number of microseconds to wait between samples
}

void checkMessage(){
  String message = String(in_text); // converts in_text into a string
  //
  if(message.indexOf("stop data") > 0){
    sending_data = false; 
    delay(1000);
  }
  else if(i = 1){//(message.indexOf("start data") > 0){
    sending_data = true; 
    delay(1000);
  }
}
*/
