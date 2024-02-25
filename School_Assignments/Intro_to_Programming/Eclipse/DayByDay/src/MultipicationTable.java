
public class MultipicationTable {
	/** Main method */
	public static void main(String[] args) {
		// Display the table heading
//		System.out.println("           Multiplication Table");
		System.out.printf("%11s%s%n", "", "Multiplication Table");

		// Display the number title
//		System.out.print("    ");
		System.out.printf("%4s", "");
		for (int j = 1; j <= 9; j++) {
//			System.out.print("   " + j);
			System.out.printf("%3s%d", "", j);
		}

		System.out.println();
		// output separator 
		for (int i = 1; i <= 36; i++) {
			System.out.print("-");
		}
		System.out.println();

		// Print table body
		for (int i = 1; i <= 9; i++) {
			// print "row" and vertical bars
			System.out.print(i + " | ");
			for (int j = 1; j <= 9; j++) {
				// Display the product and align properly
				System.out.printf("%4d", i * j);
			}
			System.out.println();
		}
	}
}
