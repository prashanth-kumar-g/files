const int ain=A0;
int relayInput = 16; // D0
int inputVal=0;

void setup()
{
  Serial.begin(9600);
  pinMode(relayInput, OUTPUT); // initialize pin as OUTPUT
}
void loop()
{
inputVal=analogRead(ain);
Serial.println(inputVal);
if(inputVal > 500)
{
  digitalWrite(relayInput, HIGH); // turn relay on
  Serial.println("Relay On!");
}
else
{
  digitalWrite(relayInput, LOW); // turn relay off
  Serial.println("Relay OFF!");
}
delay(500);
}
