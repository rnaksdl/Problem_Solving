
/** File: PAssign06.java
 * Class: CSCI 1301
 * Author: Kyumin Lee
 * Created on: Mar 14, 2022
 * Last Modified: Mar 14, 2022
 * Description: 
 */

import java.util.Scanner;

public class PAssign06 {

	public static int countCharacters(String word, char character) {
		int count = 0, length = word.length() - 1;

		for (int i = 0; i <= length; i++) {
			if (character == word.charAt(i)) {
				count++;
			}
		}
		return count;
	}

	public static void printCount(String word, char character, int count) {
		System.out.printf("%s occurs in %s %d times%n", character, word, count);
	}

	public static String reverseString(String word) {
		String reversed = "";
		for (int i = word.length() - 1; i >= 0; i--) {
			reversed += word.charAt(i);
		}
		return reversed;
	}

	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);

		String userString = "", userTempString = "", sentinel = "STOP";
		char userCharacter = ' ';
		int numOfChar = 0;

		while (userString.equals(sentinel) == false) {
			System.out.printf("Enter a string: ");
			userString = input.next();
			if (userString.equals(sentinel) == false) {
				System.out.printf("Enter a character: ");
				userTempString = input.next();
				userCharacter = userTempString.charAt(0);

				numOfChar = countCharacters(userString, userCharacter);

				printCount(userString, userCharacter, numOfChar);

				System.out.printf("The reverse of %s is %s%n", userString, reverseString(userString));
				System.out.println();
			}
		}
	}
}
