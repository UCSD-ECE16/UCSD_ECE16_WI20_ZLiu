
#include "BluetoothSerial.h"
BluetoothSerial SerialBT;
// ========= setting PWM properties ======= //
const int pwmFrequency = 5000;
const int pwmChannel = 3;
const int pwmBitResolution = 8;
int accelZ = A0;
int accelY = 39; //(IO39/A1)
int accelX = 34; //(IO34/A2)
int accelZ_Val;
int accelY_Val;
int accelX_Val;
int timer;

// ======== MOTOR VARs ========== //
int motorPin = 5;

// ==== Message VARs ====== // 
char in_text[64];                
// Character buffer 
int in_text_index = 0;
int idx = 0; 

// ======== For the Timer ==========//
int timer_seconds;
int Millis = millis();
int tapTime;
int nowTime;
// ========= Timer Var ========= // 
int time_last_tap; //initiate the last tap time at 0
int timer_state = 0; 

void setup(){
  Serial.begin(9600);
  //SerialBT.begin("Iris's Firebeetle"); //Defaults to 115200 Baud Rate
  // setupMotor();
   //ACCEL VARs
  accelZ_Val = 0;
  //int accelY_Val = 0;
  //int accelX_Val = 0;
  //int timer = 0;
  int time_last_tap = 0; //initiate the last tap time at 0
  int timer_seconds = 0;
  setupADC();
  initDisplay();
}

void Lab2_C1(){
  // buzz motor at full power for 1 second 
  buzzMotor(255);
  delay(1000);
  buzzMotor(127);
  delay(1000);
  buzzMotor(0);
  delay(1000);
}



// Write the codes for c4 here or start a new function for c4 ? 
void Lab2_C2(){
  // Millis = millis();
  detectTap();
  if (detectTap() == true){
  // add one second to the timer and show on LED 
    addTimerOLED();
  }
}

void Lab2_C3(){
  receiveMessage();
}

void Lab2_C4(){
  detectTap();
  if (detectTap() == true){
    time_last_tap = Millis;
  }
  nowTime = Millis;
  if (nowTime - time_last_tap >= 3){
    runTimerOLED();
  }
  
}


void Lab3(){
  receiveMessage(); //checks for serial message
  sendData(); //sends data via serial if suppose to
}


void loop() {
  //Lab2_C1();
  //Lab2_C2();
  //Lab2_C3();
  //stateMachineTimer();
  //Lab2_C4();
  //showMessage("in_text", 1, true);  // This works.
  Lab3();
}
