import java.util.*;

public class HelloWorld {

    // method main(): ALWAYS the APPLICATION entry point
    public static void main (String[] args) {
    System.out.println ("Hello World!");

    String[] result = "this is fun ".split("\\s");
    
    if (result.length < 2) {
      System.out.println("Skipping...")  ;
    } else {
      for (int x=0; x<result.length-1; x++)
         System.out.println(result[x]+" "+result[x+1]);
    }
    
 



    }
}

