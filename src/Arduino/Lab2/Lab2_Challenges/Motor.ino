


// ========== Motor Code =========//

void setupMotor(){
  //setup the PWM for the motor
  ledcSetup(pwmChannel, pwmFrequency, pwmBitResolution);
  ledcAttachPin(motorPin, pwmChannel);
}
void buzzMotor(int buzz_power){
  //buzz the motor at the buzz_power
  ledcWrite(pwmChannel, buzz_power);
}
