// Author: Renzo Caballero,
// Association: King Abdullah University of Science and Technology (KAUST),
// email 1: Renzo.CaballeroRosas@kaust.edu.sa,
// email 2: CaballeroRenzo@hotmail.com,
// email 3: CaballeroRen@gmail.com,
// Website: https://renzocaballero.org/,
// January 2021; Last revision: 05/01/2021.

void setup() {
  // put your setup code here, to run once:
  pinMode(13,OUTPUT);
  digitalWrite(13,LOW);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0)
  {
    char letter = Serial.read();
    if(letter == '1')
    {
      digitalWrite(13,HIGH);
      Serial.println("THE LED IS ON");
    }
    else if(letter == '0')
    {
      digitalWrite(13,LOW);
      Serial.println("THE LED IS OFF");
    }
  }
}
