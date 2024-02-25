/** File: PAssign05.java
 * Class: CSCI 1301
 * Author: Kyumin Lee
 * Created on: Feb 27, 2022
 * Last Modified: Feb 27, 2022
 * Description: gets a numeric input and outputs in 4 different patterns
 */

import java.util.Scanner;

public class PAssign05 {
	public static void main(String[] args) {
		
		// declaring variables
		Scanner input = new Scanner(System.in);
		int length = 0;
		int gap = 5;
		
		do {
			
			// error message
			if (length < 0) {
				System.out.printf("Please enter a positive value.%n%n");
			}
			
			// prompt the user and store value
			System.out.print("Enter max number of multiples: ");
			length = input.nextInt();
			
			// repeat when value is negative
		} while (length < 0);
		System.out.println();
		
		// Pattern A
		System.out.println("Pattern A:");
		for (int i = 1; i <= length; i++) {
			for (int j = 1; j <= i; j ++) {
				System.out.printf("%d ", j * gap);
			}
			System.out.println();
		}
		System.out.println();
		
		// Pattern B
		System.out.println("Pattern B:");
		for (int i = length; i >=1; i--) {
			for (int j = 1; j <= i; j++) {
				System.out.printf("%d ", j * gap);
			}
			System.out.println();
		}
		System.out.println();

		// Pattern C
		System.out.println("Pattern C:");
		for (int i = 1; i <= length; i++) {
			for (int j = i; j >= 1; j--) {
				System.out.printf("%d ", j * gap);
			}
			System.out.println();
		}
		System.out.println();
		
		// Pattern D
		System.out.println("Pattern D:");
		for (int i = length; i >= 1; i--) {
			for (int j = i; j >= 1; j--) {
				System.out.printf("%d ", j * gap);
			}
			System.out.println();

		}
	}
}
