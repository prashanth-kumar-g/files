
#include <ESP8266WiFi.h>
#include <WiFiClientSecure.h>
#include <UniversalTelegramBot.h>
#include <ArduinoJson.h>
#include "DHT.h"

// Replace with your network credentials
const char* ssid = "Manju";
const char* password = "Manju123";

// Initialize Telegram BOT
#define BOTtoken "5388068474:AAHr_Qz5GHRXh_O2SY7DymOeOtFptMlSz4g"  // your Bot Token (Get from Botfather)


#define CHAT_ID "614882195"


#define DHTPIN D1   // what digital pin we're connected to

// Uncomment whatever type you're using!
#define DHTTYPE DHT11  // DHT 11
//#define DHTTYPE DHT22  // DHT 22 (AM2302), AM2321
//#define DHTTYPE DHT21  // DHT 21 (AM2301)

DHT dht(DHTPIN, DHTTYPE);



X509List cert(TELEGRAM_CERTIFICATE_ROOT);
WiFiClientSecure client;
UniversalTelegramBot bot(BOTtoken, client);


void setup() 
{
  dht.begin();
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
    bot.sendMessage(CHAT_ID, "Message Sending Testing 123!!", "");


 // Reading temperature or humidity takes about 250 milliseconds!
 // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
 float h = dht.readHumidity();
 // Read temperature as Celsius (the default)
 float t = dht.readTemperature();

 // Check if any reads failed and exit early (to try again).
 if (isnan(h) || isnan(t)) {
  Serial.println("DHT failed to read this time");
  return;
 }
 Serial.print("Humidity: ");
 Serial.print(h);
 Serial.print(" %");
 Serial.print("Temperature: ");
 Serial.print(t);
 Serial.print(" *C ");
 Serial.print("\n");
 bot.sendMessage(CHAT_ID, String(h), "");
 bot.sendMessage(CHAT_ID, String(t), "");
 Serial.println("Message Sent to Telegram");
 delay(1000);
}
