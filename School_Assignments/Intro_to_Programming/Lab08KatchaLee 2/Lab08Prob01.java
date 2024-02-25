/**
 * File: Lab08Prob01.java 
 * Class: CSCI 1301 
 * Author: Mercy Katcha, Kyumin Lee
 * Created on: March 25, 2022
 * Last Modified:March 25, 2022  
 * Description: testing min and max from two floating points
 */
public class Lab08Prob01 {
	public static void main(String[] args) {

		double i = 1, j = 3;
		System.out.printf("The maximum between %.2f and %.2f is %.2f\n", i, j, max(i,j));
		System.out.printf("The minimum between %.2f and %.2f is %.2f\n", i, j, min(i, j));
		
	}

	/** Return the max between two numbers */
	public static double max(double num1, double num2) {
		double result;

		if (num1 > num2)
			result = num1;
		else
			result = num2;

		return result;
	}
	//return min from two double values
	public static double min(double num1, double num2) {
		double result;

		if (num1 < num2)
			result = num1;
		else
			result = num2;

		return result;
	}
	
}
