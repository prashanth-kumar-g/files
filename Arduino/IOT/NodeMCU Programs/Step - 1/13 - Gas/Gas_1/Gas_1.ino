void setup() {
  Serial.begin(9600);
  
}

void loop() {
  Serial.print("Gas Level : ");
  Serial.println(analogRead(A0));
  delay(1000);
}
