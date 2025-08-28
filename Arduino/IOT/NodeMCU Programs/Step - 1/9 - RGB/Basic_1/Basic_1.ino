const int RED = 14; // D5
const int GREEN = 12; // D6
const int BLUE = 13; // D7

void setup() {
  pinMode(RED, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);
}

void loop() { 
  analogWrite(RED, 0);
  analogWrite(GREEN,255);
  analogWrite(BLUE, 255);  
  delay (500);
  analogWrite(RED, 255);
  analogWrite(GREEN, 0);
  analogWrite(BLUE, 255);  
  delay (500);
  analogWrite(RED, 255);
  analogWrite(GREEN, 255);
  analogWrite(BLUE, 0);  
  delay (500);
  analogWrite(RED, 100);
  analogWrite(GREEN, 500);
  analogWrite(BLUE, 205);  
  delay (500);
  analogWrite(RED, 200);
  analogWrite(GREEN, 70);
  analogWrite(BLUE, 250);  
  delay (500);
}
