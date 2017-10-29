#include <dht.h>

dht DHT;

#define DHT11_PIN 7

int photoRPin = 0;
int lightLevel;
int ledPin = 12;
int fan = 8;
int relayPin =  13;
int incomingByte = 0;

void setup()   {                
  pinMode(relayPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
  pinMode(fan, OUTPUT); 
  Serial.begin(9600);
}

void loop()                     
{
  if (Serial.available() > 0) {
	incomingByte = Serial.read();
        Serial.println(incomingByte);
        if (incomingByte == 49){
          digitalWrite(relayPin, HIGH);
          digitalWrite(ledPin, HIGH);
          digitalWrite(fan, HIGH);
        }
        else if (incomingByte == 50){
          digitalWrite(relayPin, LOW);
          digitalWrite(ledPin, LOW);
          digitalWrite(fan, LOW);
        }
        else if (incomingByte == 51){
          digitalWrite(fan, HIGH);
        }
        else if (incomingByte == 52){
          digitalWrite(fan, LOW);
        }
        else if (incomingByte == 53){
          digitalWrite(ledPin, HIGH);
        }
        else if (incomingByte == 54){
          digitalWrite(ledPin, LOW);
        }
        else if (incomingByte == 55){
          digitalWrite(relayPin, HIGH);
        }
        else if (incomingByte == 56){
          digitalWrite(relayPin, LOW);
        }
        else {
          digitalWrite(relayPin, LOW);
          digitalWrite(ledPin, LOW);
          digitalWrite(fan, LOW);
        }
  int chk = DHT.read11(DHT11_PIN);
  lightLevel=analogRead(photoRPin);

  }
}
