// Exercise 5: Stream

import java.util.*;

public class Sample {
  public static void main(String[] args){
    int [] factor = new int[] { 1, 2, 3 };

    var numbers = List.of(1, 2, 3);

    var stream = numbers.stream()
      .map(number -> number * factor[0]);

    factor[0] = 0;

    stream.forEach(System.out::print);
  }
}

// What is the output here?
// Functional programming relies on lazy evaluation for efficiency
// Lazy evaluation relies on purity of functions for correctness
//
// We need to make sure that lambdas are pure
//
// Rules of purity
// 1. The function does not make any change that is visible outside
// 2. the function does not depend on anything that may change on the outside
// - Because the result is not predictable.
