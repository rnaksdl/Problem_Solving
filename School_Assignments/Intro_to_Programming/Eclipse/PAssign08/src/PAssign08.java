/** File: PAssign08.java
 * Class: CSCI 1301
 * Author: Kyumin Lee
 * Created on: April 1, 2022
 * Last Modified: April 8, 2022
 * Description: checks two arrays' condition and computes then prints
 */

public class PAssign08 {
	public static void main(String[] args) {

		// arrays of Annual maintenance/renovations ($USD) and Annual rental income ($USD)
		int[] annualRnvtnArr = {21500, 29275, 37250, 35322, 19757, 24625, 30300, 18759, 15217, 27090, 12439, 22005};
		int[] annualRentArr = {26752, 21421, 39759, 24783, 15297, 25264, 32159, 16157, 21705, 19420, 18275, 21350};
		boolean[] decisionArr = new boolean [annualRnvtnArr.length];

		// inititalizing total Renovation/rental income before/after donation
		double ttlRnvtnBfr = 0.0, ttlRentBfr = 0.0, ttlRnvtnAft = 0.0, ttlRentAft = 0.0, ttlDonatedRent = 0.0, DonatedRentIncome = 0.0;

		// loop to calculate total before and after donation
		for (int i = 0; i < annualRnvtnArr.length; i++) {
			ttlRnvtnBfr += annualRnvtnArr[i];
			ttlRentBfr += annualRentArr[i];

			// computing total and giving value to array according to its condition
			if (keepProperty(annualRnvtnArr[i], annualRentArr[i]) == true) {
				ttlRnvtnAft += annualRnvtnArr[i];
				ttlRentAft += annualRentArr[i];
				decisionArr[i] = true;
			} else {
				ttlDonatedRent += annualRentArr[i];
				decisionArr[i] = false;
				DonatedRentIncome +=  annualRentArr[i];
			}
		}

		// outputs
		System.out.printf("Total maintenance/renovation before donation: $%,.2f%n", ttlRnvtnBfr);
		System.out.printf("Total rental income before donation: $%,.2f%n", ttlRentBfr);
		System.out.println();
		System.out.printf("Total maintenance/renovation after donation: $%,.2f%n", ttlRnvtnAft);
		System.out.printf("Total rental income after donation: $%,.2f%n", ttlRentAft);
		System.out.println();
		System.out.printf("Total Donated Rental Income: $%,.2f%n", DonatedRentIncome);
		System.out.println();
		printDecisions(decisionArr);
	}

	// method that decide whether to keep(true) or donate(false)
	public static boolean keepProperty(int value1, int value2) {
		
		// declaration and calculation
		double computedArr1 = value1 * 4.75;
		double computedArr2 = (value2 * 10.25)/2;
		
		// returns value according to condition
		if (computedArr1 < computedArr2) {
			return true;
		} else {
			return false;
		}

	}

	// methods that pritns the array according to its value
	public static void printDecisions(boolean[] decesionArr) {
		String decesion = "";
		
		// loop to see its condition and print
		for (int i = 0; i < decesionArr.length; i++) {
			if (decesionArr[i] == true) {
				decesion = "keep";
			} else {
				decesion = "donate";
			}
			System.out.printf("Property %d - %s%n", i, decesion);
		}
	}
}