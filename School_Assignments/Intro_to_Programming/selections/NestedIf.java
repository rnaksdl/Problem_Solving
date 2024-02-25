/**
 * File: NestedIf.java
 * Class: CSCI 1301
 * Author: Christopher Williams
 * Created on: Aug 28, 2018
 * Last Modified: Aug 28, 2018
 * Description:  Demonstrate use of nested-ifs
 */

import java.util.*;

public class NestedIf {
	public static void main(String[] args) {
		// get input
		Scanner input = new Scanner(System.in);
		System.out.println("Enter your age: ");
		double age = input.nextDouble();

		boolean oldEnough = false, isResident = false;

		// compare resident status
		if (age >= 18) {
			// age is fine
			System.out.println("Are you a resident (0 for yes, 1 for no)? ");
			double residentStatus = input.nextDouble();
			oldEnough = true;

			if (residentStatus == 0) {
				// can vote
				isResident = true;
			} else {
				// can't vote, not resident
				isResident = false;
			}
		} else {
			oldEnough = false;
			// can't vote, too young
		}

		// output results
		if (oldEnough) {
			if (isResident) {
				System.out.println("You can vote!");
			} else {
				System.out.println("You can't vote :(, not a resident");
			}
		} else {
			System.out.println("You can't vote :(, too young");
		}











	}

}
