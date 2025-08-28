/*
 * Demo program to add your Nuttyfi, NodeMCU ESP8266 or ESP32 wifi board to 
 * Blynk2.0 IoT mobile app & web dashboard
 * This program is property of SME Dehradun. for any query related to this program, 
 * contact us at www.smedehradn.com
 * if your want any solution related for any IoT Customized Boards and Sensor, 
 * then contact to www.nuttyengineer.com 
 */
// Replace/ Fill-in information from your Blynk Template here

#define BLYNK_TEMPLATE_ID "Change it"
#define BLYNK_DEVICE_NAME "Change it"

#define BLYNK_FIRMWARE_VERSION "0.1.0"
#define BLYNK_PRINT Serial
#include "BlynkEdgent.h"

void setup()
{
  Serial.begin(9600);

  Serial.println("Serial begin");
  BlynkEdgent.begin();
  delay(2000);
}

void loop() {
    BlynkEdgent.run();
}
