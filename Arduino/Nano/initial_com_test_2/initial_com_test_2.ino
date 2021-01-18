// Author: Renzo Caballero,
// Association: King Abdullah University of Science and Technology (KAUST),
// email 1: Renzo.CaballeroRosas@kaust.edu.sa,
// email 2: CaballeroRenzo@hotmail.com,
// email 3: CaballeroRen@gmail.com,
// Website: https://renzocaballero.org/,
// January 2021; Last revision: 07/01/2021.

void setup() {
  // put your setup code here, to run once:
  pinMode(13,OUTPUT);
  digitalWrite(13,LOW);
  Serial.begin(9600);
  Serial.println("<Arduino is ready>");
}

void loop() {
  // put your main code here, to run repeatedly:
  String msg;
  char aux;
  if (Serial.available() > 0)
  {
    while (Serial.available() > 0)
    {
      aux = char(Serial.read());
      if (aux != '\n')
      {
        msg += aux;
        delay(100);
      }
    }
    
    if (msg.equals("LED"))
    {
      digitalWrite(13,HIGH);
      Serial.println("The LED is HIGH");
    }
    else if (msg.equals("LED_OFF"))
    {
      digitalWrite(13,LOW);
      Serial.println("The LED is LOW");
    }
    else
    {
      Serial.println("You wrote: "+msg);
    }
    
  }
}
