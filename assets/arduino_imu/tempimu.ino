#include <Wire.h>
#include <L3G.h>
#include <LSM303.h>
#define TEMP_PIN 3

L3G gyro;
LSM303 compass;

int tempReading;

char report[128];
unsigned long time;

void setup() {
  Serial.begin(9600);
  Wire.begin();
  
  boolean isFaulty = false;
  
  if (!gyro.init()) {
    Serial.println("Failed to autodetect gyro type!");
    isFaulty = true;
  }
  
  if (!compass.init()) {
    Serial.println("Failed to autodetect compass type!");
    isFaulty = true;
  }
  
  while (isFaulty);
  
  gyro.enableDefault();
  compass.enableDefault();
  analogReference(INTERNAL);
}

void loop() {
  gyro.read();
  compass.read();
  tempReading = analogRead(TEMP_PIN);
  time = millis();
  snprintf(report, sizeof(report), "\1%lu %d %d %d %d %d %d %d %d %d %d\0",
    time,
    tempReading,
    gyro.g.x, gyro.g.y, gyro.g.z,
    compass.a.x, compass.a.y, compass.a.z,
    compass.m.x, compass.m.y, compass.m.z);
  Serial.println(report);
  
  delay(100);
}
