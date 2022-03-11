int note_c4 = 262;
int note_d4 = 294;
int note_e4 = 330;
int note_f4 = 349;
int note_g4 = 392;
int note_a4 = 440;
int note_b4 = 494;
int note_c5 = 523;

int speakerSensor = 8;
int noteDuration = 500;

void setup() {
  // put your setup code here, to run once:
  pinMode(speakerSensor, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  tone(speakerSensor, note_c4, noteDuration);
  delay(500);
  tone(speakerSensor, note_d4, noteDuration);
  delay(500);
  tone(speakerSensor, note_e4, noteDuration);
  delay(500);
  tone(speakerSensor, note_f4, noteDuration);
  delay(500);
  tone(speakerSensor, note_g4, noteDuration);
  delay(500);
  tone(speakerSensor, note_a4, noteDuration);
  delay(500);
  tone(speakerSensor, note_b4, noteDuration);
  delay(500);
  tone(speakerSensor, note_c5, noteDuration);
  delay(500);
}
