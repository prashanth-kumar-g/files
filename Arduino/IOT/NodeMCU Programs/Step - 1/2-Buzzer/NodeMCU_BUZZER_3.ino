#define BUZZER D2
void setup() 
{
  pinMode(BUZZER, OUTPUT);
}
void loop()
{
  digitalWrite(BUZZER, HIGH);// turn the LED off.(Note that LOW is the voltage level but actually 
  delay(200);            // wait for 1 second.
  digitalWrite(BUZZER, LOW); // turn the LED on.
  delay(200); // wait for 1 second.
}