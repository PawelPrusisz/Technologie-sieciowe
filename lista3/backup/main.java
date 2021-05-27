import java.util.ArrayList;

public class main {


  public static int networkLength = 60;
  public static int printSpeed = 60;
  public static int delayRange = 10;

  public static void main(String[] args)
  {

    String[] network = new String[networkLength];


    Transmitter t1 = new Transmitter("A", 10, 2*networkLength);
    Transmitter t2 = new Transmitter("B", 50, 2*networkLength);

    ArrayList<Transmitter> transmitters = new ArrayList<Transmitter>();

    transmitters.add(t1);
    transmitters.add(t2);

    Controller ctrl = new Controller(network,transmitters, delayRange);
    int i;
    try
    {
        i = Integer.parseInt(args[0]);
        ctrl.run(i);
    }
    catch (Exception e)
    {
        System.out.println("Interrupted");
    }
    System.out.println("finished");
  }
}