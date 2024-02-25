/** File: PAssign0.java
 * Class: CSCI 1301
 * Author: Lee, Rincon, Austin
 * Created on: Feb 11, 2022
 * Last Modified: Feb 11, 2022
 * Description:  Prompts the user and gets input to determine length and prints output
 */ 

import java.util.Scanner;

public class Lab04Prob04 {
	public static void main(String [] args) {
		Scanner input = new Scanner(System.in);
		
		//	prompt the user for string value
		System.out.print("Enter a string value: ");
		String userInput = input.nextLine();
		
		//	decalre variables
		char firstLetter = userInput.charAt(0);
		char lastLetter = userInput.charAt(userInput.length() - 1);
		char middleLetter = userInput.charAt((int)Math.ceil(userInput.length() / 2.0));
		
		// determine if there is the word is long enough and print the output
		if (userInput.length() >= 4) {
			System.out.println("For the string " + userInput + ":");
			System.out.println("first letter is " + firstLetter);
			System.out.println("last letter is " + lastLetter);
			System.out.println("\"middle\" letter is " + middleLetter);
		} else {
			System.out.println("The string you entered (" + userInput + ") contains less than 4 characters");
		}
	}
}
