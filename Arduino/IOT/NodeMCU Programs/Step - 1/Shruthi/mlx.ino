#include <Adafruit_MLX90614.h>
#include <TM1637.h>
Adafruit_MLX90614 mlx = Adafruit_MLX90614();


int CLK = 14;
int DIO = 12;

TM1637 tm(CLK,DIO);



void setup() {
  tm.init();

  //set brightness; 0-7
  tm.set(2);
  Serial.begin(9600);
  while (!Serial);

  if (!mlx.begin()) {
    Serial.println("Error connecting to MLX sensor. Check wiring.");
    while (1);
  };
}

void loop() {
  Serial.print("\nAmbient temperature = "); 
  Serial.print(mlx.readAmbientTempC());
  Serial.print("°C");      
  Serial.print("   ");
  Serial.print("\nObject temperature = "); 
  Serial.print(mlx.readObjectTempC()); 
  Serial.println("°C");
  
  Serial.print("\nAmbient temperature = ");
  Serial.print(mlx.readAmbientTempF());
  Serial.print("°F");      
  Serial.print("   ");
  Serial.print("\nObject temperature = "); 
  Serial.print(mlx.readObjectTempF()); 
  Serial.println("°F");

  Serial.println("-----------------------------------------------------------------");
  displayNumber(mlx.readObjectTempC());
  delay(2000);
}
void displayNumber(int num){   
    tm.display(3, num % 10);   
    tm.display(2, num / 10 % 10);   
    tm.display(1, num / 100 % 10);   
    tm.display(0, num / 1000 % 10);
}
