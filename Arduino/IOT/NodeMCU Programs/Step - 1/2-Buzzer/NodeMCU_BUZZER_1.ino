#define Buzzer D2            // Buzzer in NodeMCU at pin GPIO16 (D2).
void setup() 
{
  pinMode(Buzzer, OUTPUT);    // Buzzer pin as output.
}
void loop()
{
  digitalWrite(Buzzer, HIGH);// turn the Buzzer On.(Note that LOW is the voltage level but actually 
  delay(1000);            // wait for 1 second.
  digitalWrite(Buzzer, LOW); // turn the Buzzer off.
  delay(1000); // wait for 1 second.
}
