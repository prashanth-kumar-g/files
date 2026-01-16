
#include <cvzone.h>

SerialData serialData;

int sendVals[2]; // Array of values to send

const int trigPin = 16;  //D0
const int echoPin = 5;  //D1

int buz = 0;

// defines variables
long duration;
int distance;


void setup() {

  serialData.begin(9600);
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
pinMode(echoPin, INPUT); // Sets the echoPin as an Input
pinMode(buz, OUTPUT);

}

void loop() {

  // Clears the trigPin
digitalWrite(trigPin, LOW);
delayMicroseconds(2);

// Sets the trigPin on HIGH state for 10 micro seconds
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);

// Reads the echoPin, returns the sound wave travel time in microseconds
duration = pulseIn(echoPin, HIGH);

// Calculating the distance
distance= duration*0.034/2;
// Prints the distance on the Serial Monitor


  
  sendVals[0] = distance;

  
  serialData.Send(sendVals);
  delay(20);
  if(distance < 25)
  {
    digitalWrite(buz, HIGH);
    delay(700);
    digitalWrite(buz, LOW);
    delay(700);
  }
  if(distance < 15)
  {
    digitalWrite(buz, HIGH);
    delay(500);
    digitalWrite(buz, LOW);
    delay(500);
  }
  if(distance < 10)
  {
    digitalWrite(buz, HIGH);
    delay(300);
    digitalWrite(buz, LOW);
    delay(300);
  }
  if(distance < 5)
  {
    digitalWrite(buz, HIGH);
    delay(100);
    digitalWrite(buz, LOW);
    delay(100);
  }
  if(distance < 3)
  {
    digitalWrite(buz, HIGH);
    delay(20);
    digitalWrite(buz, LOW);
    delay(20);
  }
  
  
}
