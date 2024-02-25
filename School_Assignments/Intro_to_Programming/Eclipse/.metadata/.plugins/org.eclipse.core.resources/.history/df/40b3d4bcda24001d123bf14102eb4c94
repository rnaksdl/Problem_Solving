import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.fail;

import org.junit.jupiter.api.Test;

/**
 * JUnit tests for the class Java1Review.
 *
 * Each method in this class tests a different method in Java1Review. Study the
 * tests to determine how to write the Java1Review methods.
 *
 * If you decide to write your own tests, please do so in the main method of
 * Java1Review. Do not modify this file.
 *
 * To run the JUnit tests in Eclipse, right-click JUnitTests.java in the
 * Package Explorer and select "Run As" > "JUnit Test" from the context menu.
 * (If a pop-up window appears with a notification about errors, click the
 * "Proceed" button.) A JUnit tab will open next to the Package Explorer that
 * shows a list of the tests. If a test is shown with a green check mark, this
 * indicates that the corresponding Java1Review method passed.
 */
class JUnitTests {

	@Test
	void testFloatingPointDivision() {
		// JUnit tests use assertion methods to check the output of code. This
		// test uses assertEquals, which compares its first two arguments. If
		// the arguments are equal, the assertion passes; otherwise, the
		// assertion fails. To pass a JUnit test, every assertion in the method
		// must pass.
		assertEquals(4.0 / 4.0, Java1Review.divide(4.0, 4.0));
		assertEquals(4.0 / 3.0, Java1Review.divide(4.0, 3.0));
		assertEquals(4.0 / 2.0, Java1Review.divide(4.0, 2.0));
		assertEquals(4.0 / 1.0, Java1Review.divide(4.0, 1.0));
		assertEquals(Double.POSITIVE_INFINITY, Java1Review.divide(4.0, 0.0));
	}

	@Test
	void testIntegerDivision() {
		// In Java, different methods can have the same name. This is called
		// "method overloading." In order for the compiler to tell them apart,
		// the methods must have different parameter lists.
		assertEquals(1, Java1Review.divide(4, 4));
		assertEquals(1, Java1Review.divide(4, 3));
		assertEquals(2, Java1Review.divide(4, 2));
		assertEquals(4, Java1Review.divide(4, 1));

		// Unlike floating-point division, dividing by integer 0 causes an
		// arithmetic exception. Don't worry about the try-catch syntax right
		// now. We'll cover it later in the semester.
		try {
			Java1Review.divide(4, 0);
			fail();  // This method will cause the test to fail.
		} catch (ArithmeticException exception) {
			// If Java1Review.divide throws an arithmetic exception, the
			// program immediately leaves the try block (skipping the fail
			// method) and enters the catch block.
		}
	}

	@Test
	void testIsDivisibleBy7() {
		// This test uses the assertion methods assertTrue and assertFalse.
		// These methods work just like assertEquals, but the second argument
		// is a fixed boolean value. For instance, the first assertion below
		// could be written like this:
		//     assertEquals(Java1Review.isDivisibleBy7(0), true);
		assertTrue(Java1Review.isDivisibleBy7(0));
		assertFalse(Java1Review.isDivisibleBy7(1));
		assertTrue(Java1Review.isDivisibleBy7(7));
		assertFalse(Java1Review.isDivisibleBy7(13));
		assertTrue(Java1Review.isDivisibleBy7(-14));
	}

	@Test
	void testMain() {
		// In Java, even the main method can be overloaded, although this is
		// likely to confuse anyone reading your code.
		assertEquals("Overloaded main method was passed \"Hi!\".",
				Java1Review.main("Hi!"));
		assertEquals("Overloaded main method was passed \"I heart Java\".",
				Java1Review.main("I heart Java"));
		assertEquals("Overloaded main method was passed \"1337 h4x0r\".",
				Java1Review.main("1337 h4x0r"));
	}

	@Test
	void testFindMin() {
		assertEquals(1, Java1Review.findMin(1, 2, 3));
		assertEquals(1, Java1Review.findMin(3, 1, 2));
		assertEquals(1, Java1Review.findMin(2, 3, 1));
		assertEquals(-7, Java1Review.findMin(-7, 42, 18));
		assertEquals(-7, Java1Review.findMin(42, 18, -7));
		assertEquals(-7, Java1Review.findMin(18, -7, 42));
	}

	@Test
	void testFindMinElement() {
		int[] array = {1, 2, 3};
		assertEquals(1, Java1Review.findMin(array));

		array = new int[] {3, 2, 1};
		assertEquals(1, Java1Review.findMin(array));

		array = new int[] {7};
		assertEquals(7, Java1Review.findMin(array));

		array = new int[] {2, -1, 5, 1, -3, 2, 4};
		assertEquals(-3, Java1Review.findMin(array));

		array = new int[] {1, 1, 2, 3, 5, 8, 13};
		assertEquals(1, Java1Review.findMin(array));
	}

	@Test
	void testAverage() {
		int[] array = {1, 2, 3};
		assertEquals(6.0 / 3.0, Java1Review.average(array));

		array = new int[] {3, 2, 1};
		assertEquals(6.0 / 3.0, Java1Review.average(array));

		array = new int[] {7};
		assertEquals(7.0, Java1Review.average(array));

		array = new int[] {2, -1, 5, 1, -3, 2, 4};
		assertEquals(10.0 / 7.0, Java1Review.average(array));

		array = new int[] {1, 1, 2, 3, 5, 8, 13};
		assertEquals(33.0 / 7.0, Java1Review.average(array));
	}

	@Test
	void testToLowerCase() {
		// This test uses the assertion method assertArrayEquals. This method
		// works like assertEquals, but it takes two arrays and compares them
		// element by element. The assertion passes only if the corresponding
		// elements are equal.
		String[] strings = {"ABC"};
		Java1Review.toLowerCase(strings);
		assertArrayEquals(new String[] {"abc"}, strings);

		strings = new String[] {"I ", "heart ", "Java"};
		Java1Review.toLowerCase(strings);
		assertArrayEquals(new String[] {"i ", "heart ", "java"}, strings);

		strings = new String[] {"E. E.", "Cummings"};
		Java1Review.toLowerCase(strings);
		assertArrayEquals(new String[] {"e. e.", "cummings"}, strings);
	}

	@Test
	void testToLowerCaseCopy() {
		String[] strings = {"ABC"};
		assertArrayEquals(new String[] {"abc"},
				Java1Review.toLowerCaseCopy(strings));
		// Java1Review.toLowerCaseCopy should leave the given array unchanged.
		assertArrayEquals(new String[] {"ABC"}, strings);

		strings = new String[] {"I ", "heart ", "Java"};
		assertArrayEquals(new String[] {"i ", "heart ", "java"},
				Java1Review.toLowerCaseCopy(strings));
		assertArrayEquals(new String[] {"I ", "heart ", "Java"}, strings);

		strings = new String[] {"E. E.", "Cummings"};
		assertArrayEquals(new String[] {"e. e.", "cummings"},
				Java1Review.toLowerCaseCopy(strings));
		assertArrayEquals(new String[] {"E. E.", "Cummings"}, strings);
	}

	@Test
	void testRemoveDuplicates() {
		// Java1Review.removeDuplicates looks for integers that appear more
		// than once in a given array. If an integer has duplicates, the method
		// replaces each appearance of the integer with 0.
		int[] array = {451};
		Java1Review.removeDuplicates(array);
		assertArrayEquals(new int[] {451}, array);

		array = new int[] {451, 451};
		Java1Review.removeDuplicates(array);
		assertArrayEquals(new int[] {0, 0}, array);

		array = new int[] {451, 451, 451};
		Java1Review.removeDuplicates(array);
		assertArrayEquals(new int[] {0, 0, 0}, array);

		array = new int[] {451, 451, 42, 451};
		Java1Review.removeDuplicates(array);
		assertArrayEquals(new int[] {0, 0, 42, 0}, array);

		array = new int[] {451, 451, 42, 451, 101};
		Java1Review.removeDuplicates(array);
		assertArrayEquals(new int[] {0, 0, 42, 0, 101}, array);

		array = new int[] {451, 101, 451, 42, 451, 101};
		Java1Review.removeDuplicates(array);
		assertArrayEquals(new int[] {0, 0, 0, 42, 0, 0}, array);

		array = new int[] {451, 101, 451, 42, 451, 101, -1};
		Java1Review.removeDuplicates(array);
		assertArrayEquals(new int[] {0, 0, 0, 42, 0, 0, -1}, array);

		array = new int[] {38, 451, 101, 451, 42, 451, 101, -1};
		Java1Review.removeDuplicates(array);
		assertArrayEquals(new int[] {38, 0, 0, 0, 42, 0, 0, -1}, array);
	}
}
