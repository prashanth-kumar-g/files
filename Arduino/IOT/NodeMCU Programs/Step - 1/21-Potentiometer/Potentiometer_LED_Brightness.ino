int pot;
int led;
void setup() {
  // put your setup code here, to run once:
  pinMode(A0, INPUT);
  pinMode(16, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  pot = analogRead(A0);
  led = map(pot, 0, 1023, 0, 255);

  analogWrite(16, led);

}
