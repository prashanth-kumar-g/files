int Touch1 = 16;  // Digital pin D0


 void setup() 
 {
 pinMode(Touch1, INPUT);
 Serial.begin(9600);
}
void loop() 
{
  if (digitalRead(Touch1) == HIGH)
  {
      Serial.println("Sensor is touched");
  }
  else
  {
    Serial.println("Sensor is Not touched");
  }
  delay(500);
}
