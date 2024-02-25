
/** File: Lab06Prob01.java
 * Class: CSCI 1301
 * Author: Kyumin Lee, Hari Patel
 * Created on: Feb 25, 2022
 * Last Modified: Feb 25, 2022
 * Description: make a do while loop to print min and max value
 */

import java.util.Scanner;

public class Lab06Prob01 {
	public static void main(String[] args) {
		
		// declare variables
		double sentinel = -19.5, userInput = 0, max = -101, min = 101;

		Scanner input = new Scanner(System.in);

		// create do while loop
		do {
			System.out.print("Enter floating-point values from -100.0 - 100.0 ( -19.5 to exit): ");
			userInput = input.nextDouble();
			if (userInput >= -100 && userInput <= 100) {
				if (userInput > max) {
					max = userInput;
				}
				if (userInput != sentinel && userInput < min) {
					min = userInput;
				}
			}

			// condition
		} while (userInput != sentinel);
		if (userInput != sentinel && max == -101 || userInput == 101) {
			System.out.printf("There were no valid values");
		} else {
			
			// error
			if (max == sentinel || min == 101) {
				System.out.print("There were no valid values");
				
			// output
			} else {
				System.out.printf("The max value was %.1f\nThe min value was %.1f", max, min);
			}
		}

	}
}