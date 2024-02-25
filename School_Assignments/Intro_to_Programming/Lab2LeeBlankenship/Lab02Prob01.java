/**
 * File: Lab02Prob01.java
 * Class: CSCI 1301
 * Author: Kyumin Lee, Adelaide Blankenship
 * Created on: Jan 21, 2022
 * Last Modified: Jan 21, 2022
 * Description: Prints birth year and current age.
 */

public class Lab02Prob01 {
	public static void main(String [] args) {
	// Creates variable currentYear and subtracts birthYear to print currentAge
	// variable birthYear and currentYear
	int birthYear = 1997;
	int currentYear = 2022;
	//currentAge calculation
	int currentAge = currentYear - birthYear;
	// prints current age on console
	System.out.println("You were born in " + birthYear + " and are " + currentAge + " years old.");
	}
}
