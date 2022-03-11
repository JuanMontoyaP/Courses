// Video: https://youtu.be/dkB40fj0vQk

int led1 = 3;
int led2 = 4;
int led3 = 5;
int led4 = 6;
int led5 = 7;

int swPin1 = 12;
int swPin2 = 13;

int swVal1;
int swVal2;
int wait = 1000;

void setup() {
    pinMode(led1, OUTPUT);
    pinMode(led2, OUTPUT);
    pinMode(led3, OUTPUT);
    pinMode(led4, OUTPUT);
    pinMode(led5, OUTPUT);

    pinMode(swPin1, INPUT);
    pinMode(swPin2, INPUT);

    Serial.begin(9600);
}

void loop() {
    digitalWrite(led1, HIGH);
    delay(wait);
    digitalWrite(led1, LOW);

    digitalWrite(led2, HIGH);
    delay(wait);
    digitalWrite(led2, LOW);

    digitalWrite(led3, HIGH);
    delay(wait);
    digitalWrite(led3, LOW);

    digitalWrite(led4, HIGH);
    delay(wait);
    digitalWrite(led4, LOW);

    digitalWrite(led5, HIGH);
    delay(wait);
    digitalWrite(led5, LOW);

    swVal1 = digitalRead(swPin1);
    swVal2 = digitalRead(swPin2);

    if (swVal1 == HIGH) {
        wait /= 2;
    }
    else if (swVal2 == HIGH) {
        wait *= 2;
    }
    
    Serial.println(wait);
}
