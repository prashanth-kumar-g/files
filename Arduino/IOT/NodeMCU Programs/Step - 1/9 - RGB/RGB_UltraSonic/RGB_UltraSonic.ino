const int RED = 14; // D5
const int GREEN = 12; // D6
const int BLUE = 13; // D7

const int trigPin = 16;  //D0
const int echoPin = 5;  //D1

// defines variables
long duration;
int distance;

void setup() {
  Serial.begin(9600); // Starts the serial communication
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  pinMode(RED, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);
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
Serial.print("Distance: ");
Serial.println(distance);
delay(500);

if(distance <= 5)
{
  analogWrite(RED, 0);
  analogWrite(GREEN,255);
  analogWrite(BLUE, 255);  
  delay (500);
}
else if(distance <=10 && distance >5)
{
  analogWrite(RED, 0);
  analogWrite(GREEN, 0);
  analogWrite(BLUE, 255);  
  delay (500);
}
else if(distance <=20 && distance >10)
{
  analogWrite(RED, 255);
  analogWrite(GREEN, 0);
  analogWrite(BLUE, 255);  
  delay (500);
}
else if(distance <=50 && distance >20)
{
  analogWrite(RED, 255);
  analogWrite(GREEN, 255);
  analogWrite(BLUE, 0);  
  delay (500);
}
else if(distance >50)
{
  analogWrite(RED, 0);
  analogWrite(GREEN, 255);
  analogWrite(BLUE, 128);  
  delay (500);
}
}