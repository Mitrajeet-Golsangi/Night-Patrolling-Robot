#define USOUND_TRIGGER 6
#define USOUND_ECHO 5

void setup() {
  // put your setup code here, to run once:
  pinMode(USOUND_TRIGGER, OUTPUT);
  pinMode(USOUND_ECHO, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(USOUND_TRIGGER, HIGH);
  delayMicroseconds(10);
  digitalWrite(USOUND_TRIGGER, LOW);

  int time = pulseIn(USOUND_ECHO, HIGH);
  int dist = (time * 0.034) / 2;
  Serial.print("Dist : ");
  Serial.println(dist);
  delay(500);
}
