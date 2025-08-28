

// for ESP8266 Microcontroller
#define rainAnalog A0
#define rainDigital D1


void setup() {
  Serial.begin(9600);
  pinMode(rainDigital,INPUT);
}
void loop() {
  int rainAnalogVal = analogRead(rainAnalog);
  int rainDigitalVal = digitalRead(rainDigital);

  Serial.print("Rain Level :");
  Serial.print(rainAnalogVal);
  Serial.print("\t");
  Serial.println(rainDigitalVal);
  delay(200);
}
