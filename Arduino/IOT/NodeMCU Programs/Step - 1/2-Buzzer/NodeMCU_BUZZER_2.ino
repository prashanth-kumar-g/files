#define RED D0            // Led in NodeMCU at pin GPIO16 (D0).
#define GREEN D1
#define YELLOW D2
#define BUZZER D3
void setup() 
{
  pinMode(RED, OUTPUT);    // LED pin as output.
  pinMode(GREEN, OUTPUT);
  pinMode(YELLOW, OUTPUT);
  pinMode(BUZZER, OUTPUT);
}
void loop()
{
  digitalWrite(RED, HIGH);// turn the LED off.(Note that LOW is the voltage level but actually 
  delay(100);            // wait for 1 second.
  digitalWrite(RED, LOW); // turn the LED on.
  delay(100); // wait for 1 second.

  digitalWrite(GREEN, HIGH);// turn the LED off.(Note that LOW is the voltage level but actually 
  delay(100);            // wait for 1 second.
  digitalWrite(GREEN, LOW); // turn the LED on.
  delay(100); // wait for 1 second.

  digitalWrite(YELLOW, HIGH);// turn the LED off.(Note that LOW is the voltage level but actually 
  delay(100);            // wait for 1 second.
  digitalWrite(YELLOW, LOW); // turn the LED on.
  delay(100); // wait for 1 second.

  digitalWrite(BUZZER, HIGH);// turn the LED off.(Note that LOW is the voltage level but actually 
  delay(100);            // wait for 1 second.
  digitalWrite(BUZZER, LOW); // turn the LED on.
  delay(100); // wait for 1 second.
}