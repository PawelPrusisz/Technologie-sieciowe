

//import java.lang.FdLibm.Pow;
import java.util.ArrayList;
import java.util.Random;


class Controller
{

  private String[] network;
  private int cnt = 0;
  private ArrayList<Transmitter> transmitterList;
  private Random r = new Random();
  private int delayRange;
  private int nLenght;

  Controller(String[] network, ArrayList<Transmitter> transmitterList, int delayRange)
  {
    this.network = network;
    nLenght = network.length;
    this.transmitterList = transmitterList;
    this.delayRange = delayRange;
    clearNetwork();
  }

  private boolean isCelar(Transmitter transmitter)
  {
    if (network[transmitter.position].equals("0") || network[transmitter.position].equals(transmitter.name))
    {
      return true;
    }
    return false;
  }

  private boolean isNoised(Transmitter transmitter)
  {
    if (network[transmitter.position].equals("#"))
    {
      return true;
    }
    return false;
  }

  void run(int it)
  {
    int i = 0;
    while (i++ < it)
    {
        System.err.println(i);
        for (Transmitter transmitter : transmitterList)
        {
            if(transmitter.transmitting)
            {
                transmittStep(transmitter);
                if(!transmitter.colisionDetected)
                {
                    transmitter.colisionDetected = true;
                    setDelay(transmitter);
                }
            }
            else if(transmitter.delay == 0)
            {
                
                transmitter.idle = false;
                transmitter.noise = false;
                if(isNoised(transmitter))
                {
                    if(transmitter.noise)
                    {
                        stepNoise(transmitter);
                    }
                    else
                    {
                        startNoise(transmitter);
                    }
                }
                else if(isCelar(transmitter))
                {
                    startTransmitting(transmitter);
                    transmitter.colisionDetected = false;
                }
                 
            }
            else
            {
                if(transmitter.idle)
                {
                    stepIdle(transmitter);
                }
                else
                {
                    startIdle(transmitter);
                }
            }
            if(!transmitter.transmitting)transmitter.delay--;
        }
      

      printNetwork();
    }
    return ;
  }

  private void startNoise(Transmitter transmitter)
  {
    transmitter.noise = true;
    transmitter.noisCount = 0;
    transmitter.signal[transmitter.position] = "#"; 
    transmitter.signalPositionL = transmitter.position - 1;
    transmitter.signalPositionR = transmitter.position + 1;
  }

  private void stepNoise(Transmitter transmitter)
  { 
    if(transmitter.noisCount <= nLenght)
    {
        transmitter.noise = false;
        setDelay(transmitter);
    }
    else
    {
        if(transmitter.signalPositionL >= 0)
        {
            transmitter.signal[transmitter.signalPositionL] = "#";
            transmitter.signalPositionL--;
        }
        if(transmitter.signalPositionR < nLenght)
        {
            transmitter.signal[transmitter.signalPositionR] = "#";
            transmitter.signalPositionR++;
        }
    }
    transmitter.noisCount++;
  }

  private void startIdle(Transmitter transmitter)
  {
    transmitter.idle = true;
    transmitter.curProp = 0;
    transmitter.signal[transmitter.position] = "0"; 
    transmitter.signalPositionL = transmitter.position - 1;
    transmitter.signalPositionR = transmitter.position + 1;
  }


  private void stepIdle(Transmitter transmitter)
  {
    if(transmitter.signalPositionL >= 0)
    {
        transmitter.signal[transmitter.signalPositionL] = "0";
        transmitter.signalPositionL--;
    }
    if(transmitter.signalPositionR < nLenght)
    {
        transmitter.signal[transmitter.signalPositionR] = "0";
        transmitter.signalPositionR++;
    }
  }
  private void setDelay(Transmitter transmitter)
  {
    transmitter.attemptCounter++;
    if(transmitter.attemptCounter > 10)transmitter.attemptCounter = 10;
    int bound = (int) Math.pow(2, transmitter.attemptCounter);
    transmitter.delay = r.nextInt(bound) + 1;
  }


  private void transmittStep(Transmitter transmitter)
  {
    if(transmitter.curProp == transmitter.propLenght)
    {
        transmitter.transmitting = false;
        randomizeDelay(transmitter);
    }
    else
    {
        if(transmitter.signalPositionL >= 0)
        {
            transmitter.signal[transmitter.signalPositionL] = transmitter.name;
            transmitter.signalPositionL--;
        }
        if(transmitter.signalPositionR < nLenght)
        {
            transmitter.signal[transmitter.signalPositionR] = transmitter.name;
            transmitter.signalPositionR++;
        }
        transmitter.curProp++;
    }
  }

  private void startTransmitting(Transmitter transmitter)
  {
    transmitter.transmitting = true;
    transmitter.curProp = 0;
    transmitter.signal[transmitter.position] = transmitter.name; 
    transmitter.signalPositionL = transmitter.position - 1;
    transmitter.signalPositionR = transmitter.position + 1;
  }

  private void randomizeDelay(ArrayList<Transmitter> transmitters)
  {

    for (Transmitter trans : transmitters)
    {
      trans.delay = r.nextInt(delayRange) + nLenght;
    }
  }

  private void randomizeDelay(Transmitter transmitter)
  {
    transmitter.delay = r.nextInt(delayRange) + nLenght;
    
  }

  private void printNetwork() {

    clearNetwork();

    for(Transmitter transmitter : transmitterList)
    {
        for(int i = 0; i < nLenght; i++)
        {
            if(!transmitter.signal[i].equals("0"))
            {
                if(network[i].equals("0"))
                {
                    network[i] = transmitter.signal[i];
                }
                else
                {
                    network[i] = "#";
                }
            }
        }
    }

    for (String aNetwork : network)
    {
      for (Transmitter transmitter : transmitterList)
      {
        if (aNetwork.equals(transmitter.name))
        {
          System.out.print(aNetwork);
        }
        else if (aNetwork.equals("0"))
        {
          System.out.print(" ");
          break;
        }
        else if (aNetwork.equals("#"))
        {
          System.out.print(aNetwork);
          break;
        }
      }
    }
    System.out.println();
    if(cntCheck())cnt++;
    else cnt = 0;
    if(cnt == 10)fixup();
  }

  private boolean cntCheck()
  {
      boolean ok = true;
      for(int i = 0; i < nLenght; i++)
      {
          if(!network[i].equals("#"))ok = false;
      }
      return ok;
  }

  private void fixup()
  {
      for(Transmitter t : transmitterList)
      {
          for(int i = 0; i < nLenght; i++)
          {
              t.signal[i] = "#"; 
          }
      }
  }
  private void clearNetwork()
  {
    for (int i = 0; i < nLenght; i++)
    {
      network[i] = "0";
    }
  }

}