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
int j = 0;

const int stepsPerRevolution = 5;
Stepper myStepper = Stepper(stepsPerRevolution, 2,3);

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
  for (int i=0; i<4; i++) {
    myStepper.step(1);
    //i++;
  }
  delay(100);
}
  //Serial.println("Reading:");
/*  j++;
if (j = 5)  exit(0);
 

    /*units = scale.get_units();
    Serial.print(units);
    Serial.println(" Newtons");
    if(incomingByte=='0')
      exit(0);
  */
