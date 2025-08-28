int Status = 12;  // Relay pin D6
int sensor = 13;  // PIR pin D7

void setup() 
{

  pinMode(sensor, INPUT);   // declare sensor as input
  pinMode(Status, OUTPUT);  // declare LED as output
  Serial.begin(9600);
  Serial.println("PIR Test 123!");
}

void loop() {

  long state = digitalRead(sensor);
    if(state == HIGH) {
      digitalWrite (Status, HIGH);
      Serial.println("Motion Detected!");
      Serial.println("Light On!");
      delay(1000);
    }
    else {
      digitalWrite (Status, LOW);
      Serial.println("Motion absent!");
      Serial.println("Light Off!");
      delay(1000);
      }
}
