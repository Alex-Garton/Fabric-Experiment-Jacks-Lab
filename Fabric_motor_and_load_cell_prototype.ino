#include "HX711.h"
#include "Stepper.h"
/*
Serial.print("Reading:");
  units = scale.get_units();
  Serial.print(units);
  Serial.println(" Newtons");
  if(incomingByte=='0')
    exit(0);
*/ 
HX711 scale;

uint8_t DAT = 8;
uint8_t CLK = 7;
const int stepPin = 3;
const int dirPin = 2; 
float calibration_factor = 607; //defined with calibration code
float units;
int incomingByte = Serial.read();


const int stepsPerRevolution = 5;
Stepper myStepper(5, 2,3);

void setup() {
  scale.begin(DAT, CLK);
  pinMode(stepPin,OUTPUT);
  pinMode(dirPin,OUTPUT);
  pinMode(CLK, INPUT);
  pinMode(DAT, INPUT);
  Serial.begin(9600);
  scale.set_scale(calibration_factor);
  scale.tare();
 
  Serial.println("Readings"); 
}

void loop() {
 int i=0;
 myStepper.step(1);
 //delay(1000);
 Serial.println("Reading:");
    /*units = scale.get_units();
    Serial.print(units);
    Serial.println(" Newtons");
    if(incomingByte=='0')
      exit(0);
  */

}
