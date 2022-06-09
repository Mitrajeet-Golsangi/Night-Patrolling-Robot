void setup() {
  // put your setup code here, to run once:
  pinMode(8, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int data = digitalRead(8);
  Serial.print("Readings : ");
  Serial.println(data);
  delay(500);
}
