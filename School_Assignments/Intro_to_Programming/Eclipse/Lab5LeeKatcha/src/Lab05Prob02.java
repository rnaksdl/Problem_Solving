/** File: Lab05Prob02.java
 * Class: CSCI 1301
 * Author: Kyumin Lee, Victoria Katcha
 * Created on: Feb 18, 2022
 * Last Modified: Feb 18, 2022
 * Description: gets input and computes sum and average
 */

import java.util.Scanner;

public class Lab05Prob02 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		//declares values
		int value = 0;
		int sum = 0;
		double count = 1;
		double average = 0.0;
		int sentinel = 672;
		
		//
		while (value != sentinel) {
			value = input.nextInt();
			if (value >= 0 && value % 2 == 0 && value != sentinel) {
				sum += value;
				average = sum / count;
				count ++;
			}	
		}
		System.out.printf("For the positive, even numbers, the sum was %d and the average was %.4f.", sum, average);
	}
}
