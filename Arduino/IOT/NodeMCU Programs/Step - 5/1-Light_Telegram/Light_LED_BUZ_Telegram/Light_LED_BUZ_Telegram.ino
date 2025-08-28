
#include <ESP8266WiFi.h>
#include <WiFiClientSecure.h>

#include <UniversalTelegramBot.h>
#include <ArduinoJson.h>

//-----------------------------------Sensor Variables ----------------------------------------------------------------------------------
int relayInput1 = 16; // D0
int relayInput2 = 5;  // D1
int relayInput3 = 4;  // D2
int relayInput4 = 0;  // D3


//------- Replace the following! ---------------------------------------------------------------------------------------------------------

char ssid[] = "IOT-LAB";         // your network SSID (name)
char password[] = "Manju123"; // your network password

#define TELEGRAM_BOT_TOKEN "6363502528:AAH8GIqcY16mixUOCN9jGsmv_wNt2nzlPdA"

#define CHAT_ID "5172950600"


//------- ---------------------------------------------------------------------------------------------------------------------------------


// This is the Wifi client that supports HTTPS
WiFiClientSecure client;
UniversalTelegramBot bot(TELEGRAM_BOT_TOKEN, client);

int delayBetweenChecks = 1000;
unsigned long lastTimeChecked;   //last time messages' scan has been done

unsigned long lightTimerExpires;
boolean lightTimerActive = false;

void setup() {
  
  Serial.begin(9600);
  //-----------------------------------Sensor Setup ----------------------------------------------------------------------------------
  pinMode(relayInput1, OUTPUT); // initialize pin as OUTPUT
  pinMode(relayInput2, OUTPUT);
  pinMode(relayInput3, OUTPUT);
  pinMode(relayInput4, OUTPUT);

  // Set WiFi to station mode and disconnect from an AP if it was Previously connected
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  delay(100);

  pinMode(2, OUTPUT);
  digitalWrite(2, LOW);

  // attempt to connect to Wifi network:
  Serial.print("Connecting Wifi: ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  // Only required on 2.5 Beta
  client.setInsecure();

  bot.longPoll = 60;
}

void handleNewMessages(int numNewMessages) {

  for (int i = 0; i < numNewMessages; i++) {

    // If the type is a "callback_query", a inline keyboard button was pressed
    if (bot.messages[i].type ==  F("callback_query")) {
      String text = bot.messages[i].text;
      Serial.print("Call back button pressed with text: ");
      Serial.println(text);

      } else {
      String chat_id = String(bot.messages[i].chat_id);
      String text = bot.messages[i].text;

      if (text == F("Menu")) 
      {
        //bot.sendMessage(chat_id, "/start", "");
        bot.sendMessage(chat_id, "1 - Light On \n 2 - Light Off \n 3 - Red On  \n 4 - Red Off \n 5 - Green On \n 6 - Green Off \n 7 - Buzzer On \n 8 - Buzzer Off", "");
      }

      // When a user first uses a bot they will send a "/start" command
      // So this is a good place to let the users know what commands are available
      else if (text == F("Start")) {

        bot.sendMessage(chat_id, "Ok, Lets Get Start\n", "");
      }
      else if (text == F("Light On")) {
        digitalWrite(relayInput1, HIGH); // turn relay on
        Serial.println("Light On!");
        bot.sendMessage(chat_id, "Light On", "");
      }
      else if (text == F("Light Off")) {

        digitalWrite(relayInput1, LOW); // turn relay on
        Serial.println("Light Off!");
        bot.sendMessage(chat_id, "Light Off", "");
      }
      else if (text == F("Red On")) {

        digitalWrite(relayInput2, HIGH); // turn relay on
        Serial.println("Red On!");
        bot.sendMessage(chat_id, "Red On", "");
      }
      else if (text == F("Red Off")) {

        digitalWrite(relayInput2, LOW); // turn relay on
        Serial.println("Red Off!");
        bot.sendMessage(chat_id, "Red Off", "");
      }
      else if (text == F("Green On")) {

        digitalWrite(relayInput3, HIGH); // turn relay on
        Serial.println("Green On!");
        bot.sendMessage(chat_id, "Green On", "");
      }
      else if (text == F("Green Off")) {

        digitalWrite(relayInput3, LOW); // turn relay on
        Serial.println("Green Off!");
        bot.sendMessage(chat_id, "Green Off", "");
      }
      else if (text == F("BUZ On")) {

        digitalWrite(relayInput4, HIGH); // turn relay on
        Serial.println("BUZ On!");
        bot.sendMessage(chat_id, "BUZ On", "");
      }
      else if (text == F("BUZ Off")) {

        digitalWrite(relayInput4, LOW); // turn relay on
        Serial.println("BUZ Off!");
        bot.sendMessage(chat_id, "BUZ Off", "");
      }
      else
      {
        bot.sendMessage(chat_id, "Sorry, i am not able to understand", "");
      }
      
    }
  }
}

void loop() {
  if (millis() > lastTimeChecked + delayBetweenChecks)  {

    // getUpdates returns 1 if there is a new message from Telegram
    int numNewMessages = bot.getUpdates(bot.last_message_received + 1);

    if (numNewMessages) {
      Serial.println("got response");
      Serial.println("Replyed to Telegram");
      handleNewMessages(numNewMessages);
    }

    lastTimeChecked = millis();

    if (lightTimerActive && millis() > lightTimerExpires) {
      lightTimerActive = false;
    }
  }
}
