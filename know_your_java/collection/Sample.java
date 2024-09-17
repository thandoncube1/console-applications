import java.util.*;

public class Sample {
  public static void main(String[] args) {
    // List<Integer> numbers = new new ArrayList<Integer> (List.of(1, 2, 3));
    Collection<Integer> numbers = new ArrayList<Integer> (List.of(1, 2, 3));

    System.out.println(numbers); // [1, 2, 3]

    numbers.remove(1);

    System.out.println(numbers); // [1, 3]

  }
}

// Collection<T> - remove(T) object <----------- when collection
// List<T>       - remove(T) object
// List<T>       - remove(int index) <---------- when a list
//
// Polymorphism - the method that is called is based on the runtime type 
// of the reference rather than the compile time type of the reference of the receiver
// Polymorphism does not consider the type of the parameters at runtime. That is resolve
// at compile time.
//
// Multimethods -- is polymorphism on steroids - the method that is called is based on the runtime type of both 
// the reference of the receiver and the runtime type of the parameters of the functions
