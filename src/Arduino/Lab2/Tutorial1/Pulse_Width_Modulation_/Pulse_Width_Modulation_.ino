#include <Wire.h>

const int pwmFrequency = 5000;
const int pwmChannel = 0;
const int pwmBitResolution = 8; 


void setup() {
  Serial.begin(9600);
  // cpnfigure PWM functionalities 
  ledcSetup(pwmChannel, pwmFrequency, pwmBitResolution);

  // attach the pwmChannel to the output GPIO to be controlled 
  ledcAttachPin(LED_BUILTIN, pwmChannel);

}

void loop() {
  delay(100);
  ledcWrite(pwmChannel, 0);
  // ledcWrite will write the value to the pwmChannel;
  delay(100);
  ledcWrite(pwmChannel, 127);
  Serial.println("%50 PWM");
  delay(100);
  ledcWrite(pwmChannel, 255);
  Serial.println("100% PWM");
  delay(100);
  ledcAttachPin(pwmChannel, 127);
}
