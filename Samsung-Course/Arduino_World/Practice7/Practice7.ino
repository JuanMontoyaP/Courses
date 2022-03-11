# include <Servo.h>

Servo servo;
int potenPin = 0;
int servoPin = 9;

int angle;
int sensorVal;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  servo.attach(servoPin);
  while(!Serial);
  Serial.println("Servo Motor");
}

void loop() {
  // put your main code here, to run repeatedly:
  sensorVal = analogRead(potenPin);
  angle = map(sensorVal, 0, 1023, 0, 179);

  Serial.print("Servo Motor angle : ");
  Serial.println(angle);

  servo.write(angle);
  delay(100);
}
