void setup() 
{
  pinMode(A0, INPUT);    // LED pin as output.
  Serial.begin(9600);
}
void loop()
{
  int potVal = analogRead(A0);
  Serial.println(potVal);
}
