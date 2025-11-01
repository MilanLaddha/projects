
#include <NTPClient.h>
#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
#include <TM1637Display.h>     //

#define CLK D2                       // Define the connections pins:
#define DIO D3

TM1637Display display = TM1637Display(CLK, DIO);              // Create display object of type TM1637Display:

const char *ssid     = "LADHE";
const char *password = "20011972";

const long utcOffsetInSeconds = 19800;  //Set UTC for your country 5x3600=18000(for PAKISTAN)

// Define NTP Client to get time
WiFiUDP ntpUDP;
const int irPin1 = D1;
const int irPin2 = D0;
NTPClient timeClient(ntpUDP, "pool.ntp.org", utcOffsetInSeconds);

void setup(){

  Serial.begin(115200);
   // Clear the display:
  display.clear();
  
  WiFi.begin(ssid, password);

  while ( WiFi.status() != WL_CONNECTED ) {
    delay ( 500 );
    Serial.print ( "." );
  }

  timeClient.begin();

  pinMode(irPin1, INPUT);
  pinMode(irPin2, INPUT);
}

void loop() {
  int A,B;
  
  timeClient.update();
  display.setBrightness(7);                   // Set the brightness:
  
  A = timeClient.getHours() * 100 + timeClient.getMinutes();
  B = timeClient.getSeconds();
  
  if((B % 2) == 0)
  {
    display.showNumberDecEx(A, 0b01000000 , false, 4, 0); 
  }
  else
  {
    display.showNumberDecEx(A, 0b00000000 , false, 4, 0); 
  }
  int irValue1 = digitalRead(irPin1);
  int irValue2 = digitalRead(irPin2);
  if (irValue1==0||irValue2==0)
  {
    Serial.println("door closed");
  }
  /*
  else if(irValue1==1||irValue2==0){
    Serial.println("left door open" );
    Serial.print(A);

  }
  else if(irValue1==0||irValue2==1){
    Serial.println("right door open" );
    Serial.print(A);

  }
  */
  else
  {
    Serial.println("door open" );
    Serial.print(A);
    
  }
  
  delay(1000);
  
}
