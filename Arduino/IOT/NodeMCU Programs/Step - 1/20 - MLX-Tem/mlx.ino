#include <Adafruit_MLX90614.h>

Adafruit_MLX90614 mlx = Adafruit_MLX90614();

void setup() {
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
  delay(2000);
}
