
#include <Servo.h>

Servo myservo;  // create servo object to control a servo



void setup()
{
  myservo.attach(16);  // D0
}

void loop() 
{ 

  myservo.write(0); 
  delay(500);  
  myservo.write(180);  
  delay(1000);  
  
} 
