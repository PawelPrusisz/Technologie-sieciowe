class Transmitter {

  String name;
  String signal = "";
  int position;
  int propLenght;
  int curProp;
  int attemptCounter = 1;
  int signalPositionL;
  int signalPositionR;
  boolean transmitting;
  int delay;
  boolean msgSent;
  int waitTime = 0;
  int transmissionFailCounter;


  Transmitter(String name, int position, int leng){
    this.name = name;
    this.position = position;
    signalPositionR = position + 1;
    signalPositionL = position - 1;
    transmitting = false;
    curProp = 0;
    propLenght = leng;
    for(int i = 0; i < leng; i++)
    {
        signal += "0";
    }
  }
}