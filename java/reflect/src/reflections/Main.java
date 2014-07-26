package reflections;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

public class Main {

  public static void main(String[] args) throws NoSuchMethodException, SecurityException,
      IllegalAccessException, IllegalArgumentException, InvocationTargetException {
    // TODO Auto-generated method stub
    Class<ContainsPrivateMethod> clz = ContainsPrivateMethod.class;

    Method method = clz.getDeclaredMethod("printHello");
    method.setAccessible(true);
    method.invoke(new ContainsPrivateMethod());
    method.setAccessible(false);
    
    try {
      ContainsPrivateMethod newInstance = clz.newInstance();
    } catch (InstantiationException e) {
      e.printStackTrace();
    }
  }
}
