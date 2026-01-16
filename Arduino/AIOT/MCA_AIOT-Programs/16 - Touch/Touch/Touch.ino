const int ain=A0;
const int LED=2;
int inputVal=0;

void setup()
{
  pinMode(LED,OUTPUT); 
  Serial.begin(9600);
}
void loop()
{
inputVal=analogRead(ain);
Serial.println(inputVal);
delay(500);
}
