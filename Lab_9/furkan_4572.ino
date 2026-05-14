int led1 = 46;
int led2 = 45;
int led3 = 44;
int led4 = 43;

int buton1 = 41;
int buton2 = 40;
int buton3 = 39;
int buton4 = 38;

bool ledState1 = false;
bool ledState2 = false;
bool ledState3 = false;
bool ledState4 = false;

bool prevBtn1 = HIGH;
bool prevBtn2 = HIGH;
bool prevBtn3 = HIGH;
bool prevBtn4 = HIGH;

void setup() {
  // put your setup code here, to run once:
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);

  pinMode(buton1, INPUT_PULLUP);
  pinMode(buton2, INPUT_PULLUP);
  pinMode(buton3, INPUT_PULLUP);
  pinMode(buton4, INPUT_PULLUP);

}

void loop() {
  // put your main code here, to run repeatedly:
  bool currentBtn1 = digitalRead(buton1);
  bool currentBtn2 = digitalRead(buton2);
  bool currentBtn3 = digitalRead(buton3);
  bool currentBtn4 = digitalRead(buton4);

  if(prevBtn1 == HIGH && currentBtn1 == LOW) {
    ledState1 = !ledState1;
    digitalWrite(led1, ledState1);
  }

  if(prevBtn2 == HIGH && currentBtn2 == LOW) {
    ledState2 = !ledState2;
    digitalWrite(led2, ledState2);
  }

  if(prevBtn3 == HIGH && currentBtn3 == LOW) {
    ledState3 = !ledState3;
    digitalWrite(led3, ledState3);
  }

  if(prevBtn4 == HIGH && currentBtn4 == LOW) {
    ledState4 = !ledState4;
    digitalWrite(led4, ledState4);
  }
  
  prevBtn1 = currentBtn1;
  prevBtn2 = currentBtn2;
  prevBtn3 = currentBtn3;
  prevBtn4 = currentBtn4;

  delay(50);



  digitalWrite(led1, HIGH);
  delay(1000);

  digitalWrite(led2, HIGH);
  delay(1000);

  digitalWrite(led3, HIGH);
  delay(1000);

  digitalWrite(led4, HIGH);
  delay(1000);

  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);
  digitalWrite(led3, LOW);
  digitalWrite(led4, LOW);

  delay(1000);

}


/////////







