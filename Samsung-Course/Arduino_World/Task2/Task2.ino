// tinkercard: https://www.tinkercad.com/things/f7ykfU4cuPV-fourleds/editel

int led1 = 7;
int led2 = 6;
int led3 = 5;
int led4 = 4;

int buzzer = 2;
int potentiometer = 0;

int duration = 500;
int potentiometerValue;

// notes
int note1 = 262;
int note2 = 294;
int note3 = 330;
int note4 = 349;

void setup() {
    pinMode(led1, OUTPUT);
    pinMode(led2, OUTPUT);

    pinMode(potentiometer, INPUT);
    pinMode(buzzer, OUTPUT);

    Serial.begin(9600);
}

void loop() {
    potentiometerValue = analogRead(potentiometer);
    Serial.println(potentiometerValue);

    //potentiometerValue = map(potentiometerValue, 0, 1024, 262, 350);
    //Serial.println(potentiometerValue);

    if (potentiometerValue <= 255) {
        digitalWrite(led1, HIGH);
        digitalWrite(led2, LOW);
        digitalWrite(led3, LOW);
        digitalWrite(led4, LOW);

        tone(buzzer, note1, duration);
    }
    else if (potentiometerValue <= 512) {
        digitalWrite(led1, LOW);
        digitalWrite(led2, HIGH);
        digitalWrite(led3, LOW);
        digitalWrite(led4, LOW);

        tone(buzzer, note2, duration);
    }
    else if (potentiometerValue <= 668) {
        digitalWrite(led1, LOW);
        digitalWrite(led2, LOW);
        digitalWrite(led3, HIGH);
        digitalWrite(led4, LOW);

        tone(buzzer, note3, duration);
    }
    else {
        digitalWrite(led1, LOW);
        digitalWrite(led2, LOW);
        digitalWrite(led3, LOW);
        digitalWrite(led4, HIGH);

        tone(buzzer, note4, duration);
    }

    delay(500);
}
