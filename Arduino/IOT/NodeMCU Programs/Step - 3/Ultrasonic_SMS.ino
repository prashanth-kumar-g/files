const int trigPin = 2;  //D4
const int echoPin = 0;  //D3
int relayInput = 16; // D0
// defines variables
long duration;
int distance;

void setup() 
{
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  pinMode(relayInput, OUTPUT); // initialize pin as OUTPUT
  Serial.begin(9600); // Starts the serial communication
  Serial.println("Testing Relay and Ultrasonic!");
  
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
delay(1000);
if(distance< 5)
{
    digitalWrite(relayInput, HIGH); // turn relay on
    Serial.println("Relay On!");
     delay(1500);
}
else
{
   digitalWrite(relayInput, LOW); // turn relay off.
   Serial.println("Relay OFF!");
}
}
