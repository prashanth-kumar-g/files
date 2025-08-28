#include <Servo.h>
Servo myservo;  // create servo object to control a servo

int Servom = 12;  // Digital pin D6
int PIR = 13;  // Digital pin D7

void setup() {

  pinMode(PIR, INPUT);   // declare sensor as input
  myservo.attach(Servom);
  Serial.begin(9600);
  Serial.println("PIR Test 123!");
}

void loop() {

  long state = digitalRead(PIR);
    if(state == HIGH) 
    {
      for (int i=0; i<7; i++) 
      {
        myservo.write(0); 
        delay(500);  
        myservo.write(180);  
        delay(1000); 
        Serial.println("Motion detected!");
        delay(1000);
      }
    }
    else 
    {
      Serial.println("Motion absent!");
      delay(1000);
    }
}
