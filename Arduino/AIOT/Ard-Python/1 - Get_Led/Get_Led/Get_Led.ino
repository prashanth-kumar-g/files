#include <cvzone.h>

SerialData serialData(1, 1); //(numOfValsRec,digitsPerValRec)
int valsRec[2]; // array of int with size numOfValsRec 

void setup() {
  pinMode(16, OUTPUT);
  Serial.begin(9600);
  serialData.begin();
}

void loop() {

  serialData.Get(valsRec);
  digitalWrite(16, valsRec[0]);
  delay(10);
}
