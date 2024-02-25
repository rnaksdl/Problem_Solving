/**
 * File: Lab02Prob03.java
 * Class: CSCI 1301
 * Author: Kyumin Lee, Adelaide Blankenship
 * Created on: Jan 21, 2022
 * Last Modified: Jan 21, 2022
 * Description: Takes user input and calculates
 */

import java.util.Scanner;

public class Lab02Prob03 {
	public static void main(String [] args) {
		// Takes input from User to do calculation for age
		Scanner input = new Scanner(System.in);
		// Prompt the user for a number
		System.out.print("Enter your birth year: ");
		
		// Store the number they enter in birthYear
		int birthYear = input.nextInt();
		
		// Creates variable currentYear and subtracts birthYear to print currentAge
		int currentYear = 2022;
		int currentAge = currentYear - birthYear;
		double halfAge = currentAge / 2.0;
		
		/** prints current age on console
		 *  add 15 to currentAge and print 'after 15 years you will be + currentAge+15'
		 *  double currentAge and print 'Someone twice your age is + currentAge*2'
		 *  Calculate and print 'someone half your age is + currentAge/2"
		 */
		
		System.out.println("You were born in " + birthYear + " and are " + currentAge + " years old.");
		System.out.println("In 15 years, you will be " + (currentAge + 15) + " years old.");
		System.out.println("Someone twice your age is " + (currentAge * 2) + " years old.");
		System.out.println("Someone half your age is " + halfAge + " years old.");
		}
}
