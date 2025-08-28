int relayInput = 2; // D4

void setup() {
  Serial.begin(9600);
  Serial.println("Relay test!");

  pinMode(relayInput, OUTPUT); // initialize pin as OUTPUT

}

void loop() {

  digitalWrite(relayInput, HIGH); // turn relay on
  Serial.println("Relay On!");

  delay(1000);

  digitalWrite(relayInput, LOW); // turn relay off
  Serial.println("Relay OFF!");

  delay(1000);

}
