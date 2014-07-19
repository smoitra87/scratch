package foopkg;

import static org.junit.Assert.*;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;


public class FooTest2 {

	Foo foo;
	@Before
	public void setUp() throws Exception {
		System.out.println("Setting up");
		foo = new Foo("hello");
	}

	@After
	public void tearDown() throws Exception {
		System.out.println("Tearing Down");
	}

	@Test
	public void testFoo() {
		foo = new Foo("world");
		assertEquals(foo.x,"world");
	}

	@Test
	public void testAdd() {
		assertEquals(foo.add(1,1),2);
	}

}
