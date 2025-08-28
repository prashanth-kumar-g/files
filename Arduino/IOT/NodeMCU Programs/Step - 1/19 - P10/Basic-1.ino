#include <SPI.h>
#include <DMD2.h>
//#include <fonts/Arial_Black_16.h> Droid_Sans_12
#include <fonts/Arial14.h>

#include <Wire.h>


SoftDMD dmd(1,1);
// Number of P10 panels used X, Y
DMD_TextBox box(dmd, 1, 1, 32, 16);  
void setup() {
  Serial.begin(9600);
  Serial.println("Arduino MLX90614 Testing");  
   
  dmd.setBrightness(255); // Set brightness 0 - 255 
  dmd.selectFont(Arial14); // Font used
  dmd.begin();     // Start DMD 
  box.print("SRS"); // Display TEXT SFE
}
 
void loop() {
  Serial.print("Distance = "); Serial.print("Distance"); 
  Serial.println();
  //delay(500);
  dmd.clearScreen();
    delay(3000);
  dmd.clearScreen();
  box.print("SRS");
  delay(3000);
  dmd.clearScreen();
  box.print("BCA");
  delay(3000);
  
}
