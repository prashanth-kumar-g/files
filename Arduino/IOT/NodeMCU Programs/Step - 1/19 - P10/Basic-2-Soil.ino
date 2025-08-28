#include <SPI.h>
#include <DMD2.h>
//#include <fonts/Arial_Black_16.h> Droid_Sans_12
#include <fonts/Arial14.h>

#include <Wire.h>
#define rainAnalog A0

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
  int rainAnalogVal = analogRead(rainAnalog); 
  Serial.print("Soil Moisture = "); Serial.print(rainAnalogVal);
  Serial.println();
  delay(500);
  dmd.clearScreen();
  box.print("SOIL");
  delay(3000);
  dmd.clearScreen();
  box.print(rainAnalogVal);

  delay(3000);
  dmd.clearScreen();
  box.print("MCU");
  delay(3000);
  dmd.clearScreen();
  box.print("MCA");
  delay(3000);
  
}
