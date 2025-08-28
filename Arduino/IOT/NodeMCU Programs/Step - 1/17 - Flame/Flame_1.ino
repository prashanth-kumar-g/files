//Welcome to The IoT Projects
//IoT Based Fire Alarm Notification and control system using ESP8266
#include <ESP8266WiFi.h>
#include <WiFiClientSecure.h>
#include <UniversalTelegramBot.h>
#include <ArduinoJson.h>


int LED = D2;
int RELAY = D4;
int Flame_sensor = D1;
int Flame_detected;



void setup()
{
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  pinMode(RELAY, OUTPUT);
  digitalWrite(RELAY, HIGH);
  pinMode(Flame_sensor, INPUT_PULLUP);
  //timer.setInterval(1000L, notifyOnFire);
}
void loop()
{
  Flame_detected = digitalRead(Flame_sensor);
  Serial.println(Flame_detected);
  //delay(100);
  if (Flame_detected == 0) {
    Serial.println("Flame detected...! take action immediately.");
    digitalWrite(LED, HIGH);
    digitalWrite(RELAY, HIGH);
    delay(10000);
  }
  else
  {
    Serial.println("No Fire detected. stay cool");
    digitalWrite(LED, LOW);
    digitalWrite(RELAY, LOW);
  }
}
