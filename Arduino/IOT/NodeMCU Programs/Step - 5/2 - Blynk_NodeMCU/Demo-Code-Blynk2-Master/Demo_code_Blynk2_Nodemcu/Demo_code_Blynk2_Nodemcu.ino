/*
 * Demo program to add your Nuttyfi, NodeMCU ESP8266 or ESP32 wifi board to 
 * Blynk2.0 IoT mobile app & web dashboard
 *	for any query visit to www.smedehradun.com
 *	To design your customized hardware, visit to www.nuttyengineer.com 
 */ 
// Fill-in information from your Blynk Template here
#define BLYNK_TEMPLATE_ID "Replace it"
#define BLYNK_DEVICE_NAME "Replace it"

#define BLYNK_FIRMWARE_VERSION        "0.1.0"
#define BLYNK_PRINT Serial 
#define USE_NODE_MCU_BOARD
//#define APP_DEBUG

#include "BlynkEdgent.h"

void setup()
{
  Serial.begin(9600);
  Serial.println("Serial begin at 9600");
  BlynkEdgent.begin();
  delay(2000);
}

void loop() {
    BlynkEdgent.run();
}
