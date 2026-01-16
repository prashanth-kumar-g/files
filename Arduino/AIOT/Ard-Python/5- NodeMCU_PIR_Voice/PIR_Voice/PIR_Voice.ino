
#include <cvzone.h>

SerialData serialData;

int sendVals[2]; // Array of values to send
int sensor = 16;  // Digital pin D0



void setup() {

  serialData.begin();
  pinMode(sensor, INPUT);   // declare sensor as input
  
}

void loop() {

  
  long state = digitalRead(sensor);
    

  
  sendVals[0] = state;

  
  serialData.Send(sendVals);
  delay(200);
  
}
