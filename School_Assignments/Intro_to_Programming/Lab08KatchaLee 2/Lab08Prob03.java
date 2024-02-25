/**
 * File: Lab08Prob01.java 
 * Class: CSCI 1301 
 * Author: Mercy Katcha, Kyumin Lee
 * Created on: March 25, 2022
 * Last Modified:March 25, 2022 
 * Description: finding average, min and max values from array using index.
 */

public class Lab08Prob03 {
	public static void main(String[] args) {
		// create array and define values
		double[] myArray = { -12.6018020118, 15.3437682821, 145.8110691671, 11.1681119916, 82.0442710394,
				155.0005475009, -6.1179400421, 120.1984991874, 38.6575114628, 77.1494972203 };

		// Initialize variables
		double sum = 0;
		double average = 0;
		double minValue = myArray[0], maxValue = myArray[0];

		// create loop to make sum of numbers in array
		for (int i = 0; i < myArray.length; i++) {
			sum += myArray[i];

		}

		// create loop to find min and max value
		for (int i = 1; i < myArray.length; i++) {
			minValue = min(minValue, myArray[i]);

			maxValue = max(maxValue, myArray[i]);
		}

		// print results
		System.out.printf("Maximum Value: %.3f\n", maxValue);
		System.out.printf("Minimum Value: %.3f\n", minValue);

		// calculate and print average
		average = sum / myArray.length;
		System.out.printf("Average Value: %.3f\n", average);

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

	// return min from two double values
	public static double min(double num1, double num2) {
		double result;

		if (num1 < num2)
			result = num1;
		else
			result = num2;

		return result;
	}
}
