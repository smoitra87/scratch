package foopkg;

import static org.junit.Assert.*;

import org.junit.Test;


public class FooTest {

	@Test
	public void test() {
		Foo foo = new Foo("1");
		assertTrue(foo.add(1,1)==2);
	}

}
