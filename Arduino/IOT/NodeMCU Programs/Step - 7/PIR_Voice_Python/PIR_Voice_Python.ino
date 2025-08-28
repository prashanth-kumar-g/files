
#include <cvzone.h>
#include <ESP8266WiFi.h>
#include <WiFiClientSecure.h>
#include <UniversalTelegramBot.h>
#include <ArduinoJson.h>

SerialData serialData;

int sendVals[2]; // Array of values to 



// Replace with your network credentials
const char* ssid = "IOT-LAB";
const char* password = "Manju123";

// Initialize Telegram BOT
#define BOTtoken "6363502528:AAH8GIqcY16mixUOCN9jGsmv_wNt2nzlPdA"  // your Bot Token (Get from Botfather)


#define CHAT_ID "5172950600"

X509List cert(TELEGRAM_CERTIFICATE_ROOT);
WiFiClientSecure client;
UniversalTelegramBot bot(BOTtoken, client);

// PIR Configuration 
int Status = 16;  // Digital pin D0
int sensor = 5;  // Digital pin D1

void setup() {

  serialData.begin();
  // PIR------------------------------------------------------------------------------------
  pinMode(sensor, INPUT);   // declare sensor as input
  pinMode(Status, OUTPUT);  // declare LED as output
  Serial.println("PIR Started!");
  // PIR------------------------------------------------------------------------------------


  
  configTime(0, 0, "pool.ntp.org");      // get UTC time via NTP
  client.setTrustAnchors(&cert); // Add root certificate for api.telegram.org

  
  // Attempt to connect to Wifi network:
  Serial.print("Connecting Wifi: ");
  Serial.println(ssid);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  bot.sendMessage(CHAT_ID, "Bot started up", "");
}

void loop() {
long state = digitalRead(sensor);
    if(state == HIGH) {
      digitalWrite (Status, HIGH);
      bot.sendMessage(CHAT_ID, "Motion detected !!", "");
      
      delay(1000);
    }
    else {
      digitalWrite (Status, LOW);
      delay(1000);
      }

  
  sendVals[0] = Status;

  
  serialData.Send(sendVals);
  delay(200);
  
}
