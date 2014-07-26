package threading;

public class SimpleThreading {

  public static void main(String[] args) {
    // TODO Auto-generated method stub
    Foo foo = new Foo() {
      
      @Override
      public int ret1() {
        return 1;
      }
    };
    System.out.println(foo.ret1());
    
  }

  public static class Foo {
    public Foo() {
    }
    
    public int ret1() {
      return 0;
    }

  }
  
}
