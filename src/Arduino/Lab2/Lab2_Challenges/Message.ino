


int i = 1;
// ==== Message CODE ====== // 
void receiveMessage(){
  if (Serial.available() > 0) {
    char incomingChar = Serial.read();   // read byte from serial     
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

bool sending_data = true; //to send data?5

void sendData(){
    checkMessage();
    if(sending_data){
        if(millis()-last_sample_time >= sampling_delay){
            last_sample_time = millis();
            readADC();
            Serial.print(last_sample_time);
            Serial.print(',');
            Serial.print(accelX_Val);
            Serial.print(',');
            Serial.print(accelY_Val);
            Serial.print(',');
            Serial.println(accelZ_Val);
            // Serial.print(',');
            // Serial.println(particleSensor.getIR());
        }
    }
    delay(10);
}

long calcSamplingDelay(long sampling_rate){
    return 1000/sampling_rate;//number of microseconds to wait between samples
}

void checkMessage(){
  String message = String(in_text); // converts in_text into a string
  //delay(1000);
  Serial.print(message);
  if(message == "stop data"){
    sending_data = false; 
    //delay(1000);
  }
  else if(message == "start data"){
    sending_data = true; 
    //delay(1000);
  }
}
