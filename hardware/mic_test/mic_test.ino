void setup() {
  // put your setup code here, to run once:
  pinMode(13, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int data = digitalRead(13);
  Serial.print("Readings : ");
  Serial.println(data);
  digitalWrite(13, data);
  delay(500);
}
