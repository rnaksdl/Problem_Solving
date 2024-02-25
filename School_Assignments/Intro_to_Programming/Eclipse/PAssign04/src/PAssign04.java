/** File: PAssign04.java
 * Class: CSCI 1301
 * Author: Kyumin Lee
 * Created on: Feb 23, 2022
 * Last Modified: Feb 23, 2022
 * Description: asks user for inputs until sentinel value and determines letter grades, the highest, and the lowest. Then prints output.
 */

import java.util.Scanner;

public class PAssign04 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		// declare variables
		int grade = 0, sentinel = -999, valid = 0, invalid = 0, a = 0, b = 0, c = 0, d = 0, f = 0;
		double lowGrade = 101.00, highGrade = 0.00;
		
		// controlled while loop with sentinel
		while (grade != sentinel) {
			
			// prompt the user for input
			System.out.print("Enter grade from 0-100, -999 to stop: ");
			grade = input.nextInt();
			
			// increment variables based on input
			if (grade >= 0 && grade <= 100) {
				valid++;
				if (grade >= 90) {
					a ++;
				} else if (grade >= 80) {
					b ++;
				} else if (grade >= 70) {
					c ++;
				} else if (grade >= 60) {
					d ++;
				} else if (grade < 60) {
					f ++;
				} 
				
				// determine highest and lowest value
				if (grade > highGrade) {
					highGrade = grade;
				}
				if(grade < lowGrade) {
					lowGrade = grade;
					}
				}
			
			// promts the error
			if (grade != sentinel && grade < 0 || grade > 100) {
				System.out.println("Error: That is not a valid score.");
				invalid ++;
				
			}
			
			// when only invalid value is entered.
			if(lowGrade == 101.00) {
				lowGrade = 0.00;
			}
		}
		
//		// output
//		System.out.printf("%nValid grades:\t%d%n", valid);
//		System.out.printf("Invalid grades:\t%d%n", invalid);
//		System.out.printf("Highest grade:\t%.2f%n", highGrade);
//		System.out.printf("Lowest grade:\t%.2f%n", lowGrade);
//		System.out.printf("%nAs:\t%d%n", a);
//		System.out.printf("Bs:\t%d%n", b);
//		System.out.printf("Cs:\t%d%n", c);
//		System.out.printf("Ds:\t%d%n", d);
//		System.out.printf("Fs:\t%d%n", f);
	}
}