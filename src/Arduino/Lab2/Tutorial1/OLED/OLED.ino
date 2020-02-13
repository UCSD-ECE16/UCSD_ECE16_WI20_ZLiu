// OLED library includes 
#include "U8x8lib.h"

// OLED setup
# define OLED_RESET 4 // this value resets the OLED ??// WHAT ARE WE DOING HERE 
U8X8_SSD1306_128X32_UNIVISION_HW_I2C u8x8(OLED_RESET);     //??// WHAT ARE WE DOING HERE 

// ===================OLED Code=====================

//--------------------------------------------------------------------------------------------------------------------
// Initialize the OLED with base font for fast refresh 
// --------------------------------------------------------------------------------------------------------------------
void initDisplay(){
  u8x8.begin();
  u8x8.setPowerSave(0);
  u8x8.setFont(u8x8_font_amstrad_cpc_extended_r);
  u8x8.setCursor(0, 0);
}


void showMessages(const char * messages, int row, bool cleardisplay)
{
  if(cleardisplay){
    u8x8.clearDisplay();
  }
  u8x8.setCursor(0, row);
  u8x8.print(messages);
}
