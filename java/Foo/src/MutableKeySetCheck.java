import java.util.HashMap;
import java.util.Map;
import java.util.Set;


public class MutableKeySetCheck {

  public static void main(String[] args) {

    Map<String, Integer> tbl = new HashMap<>();
    tbl.put("1", 1);
    tbl.put("2", 2);
    
    Set<String> keySet1 = tbl.keySet();
    Set<String> keySet2 = tbl.keySet();

    System.out.printf("keySet1 = %s%n",keySet1);
    System.out.printf("keySet2 = %s%n",keySet2);
    
    tbl.remove("1");
    System.out.printf("keySet1 = %s%n",keySet1);
    System.out.printf("keySet2 = %s%n",keySet2);
  }
}
