import java.util.*;

public class Comparison {
  public static void main(String[] args) {
    // Create two unique string variables
    // Assign equal values
    // String str1 = new String("java");
    // String str2 = new String("java");
    String str1 = "java";
    String str2 = "java";

    var p = System.identityHashCode(str1);
    var q = System.identityHashCode(str2);
    
    System.out.printf("P: %s\nQ: %s\n", p, q);
    System.out.println(str1 == str2);
  }
}
