/*
 * Interface LDR with NodeMCU
 * By TheCircuit
 */
 #define LED D0  
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  pinMode(LED, OUTPUT); 
}

void loop() {
  // read the input on analog pin 0:
  int sensorValue = analogRead(A0);
  Serial.println(sensorValue);
  delay(500);
  
  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
  float voltage = sensorValue * (5.0 / 1023.0);
  
  // print out the value you read:
  Serial.println(voltage);
  if (voltage > 4.5)
  {
    digitalWrite(LED, HIGH);// turn the LED off.(Note that LOW is the voltage level but actually 

  }
  else
  {
    digitalWrite(LED, LOW); // turn the LED on.

  }
}
