
#include <cvzone.h>

SerialData serialData;

int sendVals[2]; // Array of values to send

const int trigPin = 16;  //D0
const int echoPin = 5;  //D1

// defines variables
long duration;
int distance;


void setup() {

  serialData.begin(9600);
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
pinMode(echoPin, INPUT); // Sets the echoPin as an Input

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
  delay(200);
  
}
