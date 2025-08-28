#include "DHT.h"

#define DHTPIN D1   // what digital pin we're connected to

// Uncomment whatever type you're using!
#define DHTTYPE DHT11  // DHT 11
//#define DHTTYPE DHT22  // DHT 22 (AM2302), AM2321
//#define DHTTYPE DHT21  // DHT 21 (AM2301)

DHT dht(DHTPIN, DHTTYPE);
void setup() {
 Serial.begin(9600);
 Serial.println("DHT11 test!");

 dht.begin();
}

void loop() {
 // Wait a few seconds between measurements.
 delay(2000);

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
}
