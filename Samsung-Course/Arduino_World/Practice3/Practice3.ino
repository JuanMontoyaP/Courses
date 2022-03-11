int led = 13;
int swPin = 7;
int swVal = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  pinMode(swPin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  swVal = digitalRead(swPin);

  if (swVal == HIGH) {
    digitalWrite(led, HIGH);
  }
  else {
    digitalWrite(led, LOW);
  }
}
