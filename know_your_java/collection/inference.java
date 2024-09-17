// Type inference
import java.util.*;

public class Inference {
  public static void main(String[] args) {
    String greet = "hello";

    System.out.println(greet);
    // greet is initialized with a String type and when we switch to var
    // the string greet will still return the type as a String if we check the 
    // bytecode. 

   var numbers = new ArrayList<Integer>(List.of(1, 2, 3));
   // numbers is a reference of the type ArrayList<Integer>
   //
   System.out.println(numbers);

   numbers.remove(1);

   System.out.println(numbers);
  }
}
