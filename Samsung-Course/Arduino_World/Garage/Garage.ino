#include <Servo.h>

Servo servo;
int servoPin = 9;
int knockSensor = 0;
int led1 = 6;
int led2 = 7;
int micSensor = 1;
int buzzer = 4;

int knockVal;
int micVal;
int angle = 0;

void setup() {
    pinMode(led1, OUTPUT);
    pinMode(led2, OUTPUT);
    pinMode(buzzer, OUTPUT);

    Serial.begin(9600);
    servo.attach(servoPin);
}

void loop() {
    servo.write(angle);
    
    knockVal = analogRead(knockSensor);
    // knockVal = map(knockVal, 0, 1024, 0, 11);
    // Serial.println(knockVal);

    if (knockVal > 3 && angle == 0) {
        angle = 90;
        servo.write(angle);

        digitalWrite(led1, HIGH);
    }

    micVal = analogRead(micSensor);
    micVal = map(micVal, 16, 400, 0, 21);
    Serial.println(micVal);

    delay(1000);

    if (knockVal < 2 && micVal >= 6 && angle == 90) {
        angle = 0;
        
        digitalWrite(led1, LOW);
        digitalWrite(led2, HIGH);
        digitalWrite(buzzer, HIGH);

        delay(1000);
        servo.write(angle);
    }

    delay(1000);
    digitalWrite(led2, LOW);
    digitalWrite(buzzer, LOW);
}