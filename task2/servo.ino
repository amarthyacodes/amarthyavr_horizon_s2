#include <Servo.h>

int led = 3;
int potval;
Servo servo;

void setup(){
  pinMode(led, OUTPUT);
  servo.attach(4);
}

void loop(){
  int angle = map(analogRead(A0), 0, 1023, 0, 180);
  if (angle > 68){
    servo.write(68);
    digitalWrite(led, HIGH);
  }
    else{
      servo.write(angle);
      digitalWrite(led, LOW);
  }
  delay(5);
}
      
      
  
