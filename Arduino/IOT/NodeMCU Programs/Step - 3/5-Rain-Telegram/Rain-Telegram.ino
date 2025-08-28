
#include <ESP8266WiFi.h>
#include <WiFiClientSecure.h>
#include <UniversalTelegramBot.h>
#include <ArduinoJson.h>

// Replace with your network credentials
const char* ssid = "vivoY53s";
const char* password = "queenkula";

// Initialize Telegram BOT
#define BOTtoken "6140050189:AAH4JXSzgJsTjJZBty48ZYpCTiZ8vKP2uPO"  // your Bot Token (Get from Botfather)


#define CHAT_ID "778740740"

X509List cert(TELEGRAM_CERTIFICATE_ROOT);
WiFiClientSecure client;
UniversalTelegramBot bot(BOTtoken, client);

//------------------------------Rain Sensor-------------------------------------------
// for ESP8266 Microcontroller
#define rainAnalog A0    // A0 in NodeMCU
#define rainDigital D1
//------------------------------Rain Sensor-------------------------------------------

void setup() 
{
  //------------------------------Rain Sensor-------------------------------------------
  Serial.begin(9600);
  pinMode(rainDigital,INPUT);
  //------------------------------Rain Sensor-------------------------------------------
  
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
   
    int rainAnalogVal = analogRead(rainAnalog);
  int rainDigitalVal = digitalRead(rainDigital);

  Serial.print("Rain Level :");
  Serial.print(rainAnalogVal);
  Serial.print("\t");
  Serial.println(rainDigitalVal);
  delay(200);
  if (rainAnalogVal < 500)
  {
     bot.sendMessage(CHAT_ID, "Heavy Rain is Falling !!", "");
    Serial.println("Message Sent to Telegram");

  }
  else if (rainAnalogVal < 800)
  {
    bot.sendMessage(CHAT_ID, "Average Rain is Falling !!", "");
    
    //Serial.println("Message Sent to Telegram");
  }
  else if (rainAnalogVal < 1023)
  {
    bot.sendMessage(CHAT_ID, "Rain is Falling !!", "");
  
   // Serial.println("Message Sent to Telegram");
  }
  else
  {
    Serial.println("No Rain");
  }
  
  
}
