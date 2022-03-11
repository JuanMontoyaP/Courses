int ledPin = 7;
int photoPin = 0;
int sensorLightValue = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  pinMode(photoPin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  sensorLightValue = analogRead(photoPin);

  Serial.println(sensorLightValue);

  sensorLightValue = map(sensorLightValue, 0, 1024, 0, 255);

  analogWrite(ledPin, 250 - sensorLightValue);

}
