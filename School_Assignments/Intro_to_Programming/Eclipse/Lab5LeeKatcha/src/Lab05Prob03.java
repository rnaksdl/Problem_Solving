/** File: Lab05Prob03.java
 * Class: CSCI 1301
 * Author: Kyumin Lee, Victoria Katcha
 * Created on: Feb 18, 2022
 * Last Modified: Feb 18, 2022
 * Description: 
 */

import java.util.Scanner;

public class Lab05Prob03 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		double value = 0;
		double sentinel = -19.5;
		double minValue = -111;
		double maxValue = 111;
		
		
		while (value != sentinel) {
			System.out.print("Enter a number with a decimal value: ");
			value = input.nextDouble();
			if (value >= -100 && value <= 100) {
			}
			
		}
		
		System.out.println("There were no valid values");
	}
}