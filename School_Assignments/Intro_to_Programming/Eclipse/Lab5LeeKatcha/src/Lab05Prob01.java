/** File: Lab05Prob01.java
 * Class: CSCI 1301
 * Author: Kyumin Lee, Victoria Katcha
 * Created on: Feb 18, 2022
 * Last Modified: Feb 18, 2022
 * Description: Squares the value util 250 and prints.
 */ 

public class Lab05Prob01 {
	public static void main(String[] args) {
		
		//declare values
		int value = 0;
		double sqValue = 0;
		double sentinel = 300.00;
		
		// squares the value until 250
		while (sqValue < sentinel) {
			value++;
			sqValue = Math.pow(value, 2);
		}
		
		//prints
		System.out.printf("The square of %d is greater than %.2f", value, sentinel);
	}
}

