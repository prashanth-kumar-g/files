int Status = 12;  // Digital pin D6

int sensor = 13;  // Digital pin D7

#define BUZ D2

void setup() {

  pinMode(sensor, INPUT);   // declare sensor as input
  pinMode(Status, OUTPUT);  // declare LED as output
  pinMode(BUZ, OUTPUT);
  Serial.begin(9600);
  Serial.println("PIR Test 123!");
}

void loop() {

  long state = digitalRead(sensor);
    if(state == HIGH) {
      digitalWrite (Status, HIGH);
      digitalWrite (BUZ, HIGH);
      Serial.println("Motion detected!");
      delay(1000);
    }
    else {
      digitalWrite (Status, LOW);
      digitalWrite (BUZ, LOW);
      Serial.println("Motion absent!");
      delay(1000);
      }
}
