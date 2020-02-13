
//TAP VARs
//13:02:43.835 -> Z:2341,Y:1759,X:1814

int threshZ = 2356;//determine the threshold you need
int threshY = 1800;
int threshX = 1900;

// ===== Gesture Code  ========//
bool detectTap(){
  //read the ADC values. Note that the ADC values are global so you don’t need to define a local variable for them.
  setupADC();
  readADC();
  printADC();
  bool tap_detected = false; // first set to false
  if(accelX_Val > threshX || accelY_Val > threshY || accelZ_Val > threshZ)
    tap_detected = true; //if the accel values meet the rule, set to true
  return tap_detected;
  }
