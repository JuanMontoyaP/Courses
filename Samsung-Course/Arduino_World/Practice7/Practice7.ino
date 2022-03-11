int sensorPin = 0;
int sensorVal = 0;
float temperatureC;
float voltage;

int ledR = 5;
int ledY = 6;
int ledG = 7;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(ledR, OUTPUT);
  pinMode(ledY, OUTPUT);
  pinMode(ledG, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  sensorVal = analogRead(sensorPin);
  
  voltage = sensorVal * 5.0;
  voltage /= 1024.0;

  temperatureC = (voltage - 0.5) * 100;
  Serial.println(temperatureC);

  int temp = temperatureC;
  if (temp < 27) {
    digitalWrite(ledR, HIGH);
    digitalWrite(ledY, LOW);
    digitalWrite(ledG, LOW);
  }
  else if (temp < 28) {
    digitalWrite(ledR, LOW);
    digitalWrite(ledY, HIGH);
    digitalWrite(ledG, LOW);
  }
  else {
    digitalWrite(ledR, LOW);
    digitalWrite(ledY, LOW);
    digitalWrite(ledG, HIGH);
  }
  delay(100);
}
