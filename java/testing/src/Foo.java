package foopkg;

public class Foo {

	public String x;
	
	public Foo() {
	}

	public Foo(String _) {
		x = _;
	}
	
	public int add(int a, int b) {
		return a+b;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Foo foo = new Foo();
        System.out.println("1+1="+foo.add(1,1));
	}

}
