class Transmitter {

  String name;
  String[] signal;
  int position;
  int propLenght;
  int curProp;
  int attemptCounter = 0;
  int signalPositionL;
  int signalPositionR;
  boolean transmitting;
  boolean idle = false;
  boolean noise = false;
  int noisCount = 0;
  int delay;
  boolean msgSent;
  int waitTime = 0;
  int transmissionFailCounter;
  boolean colisionDetected = false;


  Transmitter(String name, int position, int leng){
    this.name = name;
    this.position = position;
    signalPositionR = position + 1;
    signalPositionL = position - 1;
    transmitting = false;
    curProp = 0;
    propLenght = leng;
    signal = new String[leng];
    delay = position / 2;
    for(int i = 0; i < leng; i++)
    {
        signal[i] = "0";
    }
  }
}