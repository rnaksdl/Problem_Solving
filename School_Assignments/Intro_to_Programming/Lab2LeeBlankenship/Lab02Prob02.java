/**
 * File: Lab02Prob02.java
 * Class: CSCI 1301
 * Author: Kyumin Lee, Adelaide Blankenship
 * Created on: Jan 21, 2022
 * Last Modified: Jan 21, 2022
 * Description: Prints four lines of texts that requires calculations as outlined in the lab description.
 */

public class Lab02Prob02 {
	public static void main(String [] args) {
		// Creates variable currentYear and subtracts birthYear to print currentAge
		// variable birthYear and currentYear
		int birthYear = 1997;
		int currentYear = 2022;
		int currentAge = currentYear - birthYear;
		double halfAge = currentAge / 2.0;
		
		/** prints current age on console
		 * 	add 15 to currentAge and print 'after 15 years you will be + currentAge+15'
		 *  double currentAge and print 'Someone twice your age is + currentAge*2'
		 *  Calculate and print 'someone half your age is + currentAge/2"
		 */
		
		System.out.println("You were born in " + birthYear + " and are " + currentAge + " years old.");
		System.out.println("In 15 years, you will be " + (currentAge + 15) + " years old.");
		System.out.println("Someone twice your age is " + (currentAge * 2) + " years old.");
		System.out.println("Someone half your age is " + halfAge + " years old.");
		}
}
