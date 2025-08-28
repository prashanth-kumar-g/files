
#include <ESP8266WiFi.h>
#include <WiFiClientSecure.h>
#include <UniversalTelegramBot.h>
#include <ArduinoJson.h>

// Replace with your network credentials
const char* ssid = "IOT-LAB";
const char* password = "Manju123";

// Initialize Telegram BOT
#define BOTtoken "6363502528:AAH8GIqcY16mixUOCN9jGsmv_wNt2nzlPdA"  // your Bot Token (Get from Botfather)


#define CHAT_ID "5172950600"

X509List cert(TELEGRAM_CERTIFICATE_ROOT);
WiFiClientSecure client;
UniversalTelegramBot bot(BOTtoken, client);


void setup() 
{
  Serial.begin(9600);
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
    bot.sendMessage(CHAT_ID, "Message Sending to Prashanth Kumar G !!!", "");
    Serial.println("Message Sent to Telegram");
    delay(3000);
}
