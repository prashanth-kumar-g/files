
#include <ESP8266WiFi.h>
#include <WiFiClientSecure.h>

#include <UniversalTelegramBot.h>
#include <ArduinoJson.h>

//------- Replace the following! ---------------------------------------------------------------------------------------------------------

char ssid[] = "IOT-LAB";         // your network SSID (name)
char password[] = "Manju123"; // your network password

#define TELEGRAM_BOT_TOKEN "5388068474:AAHr_Qz5GHRXh_O2SY7DymOeOtFptMlSz4g"

#define CHAT_ID "614882195"


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
        bot.sendMessage(chat_id, "1 - Light On \n 2 - Light OFF \n 3 - Fan On  \n 4 - Fan Off", "");
      }

      // When a user first uses a bot they will send a "/start" command
      // So this is a good place to let the users know what commands are available
      else if (text == F("Start")) {

        bot.sendMessage(chat_id, "Ok, Lets Get Start\n", "");
      }
      else if (text == F("Hi")) {

        bot.sendMessage(chat_id, "Hi Manju", "");
      }
      else if (text == F("Bye")) {

        bot.sendMessage(chat_id, "Bye Manju, See You Soon", "");
      }
      else if (text == F("How are you")) {

        bot.sendMessage(chat_id, "I am Fine, How abt You", "");
      }
      else if (text == F("BCA")) {

        bot.sendMessage(chat_id, "I am Fine, How abt You", "");
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
