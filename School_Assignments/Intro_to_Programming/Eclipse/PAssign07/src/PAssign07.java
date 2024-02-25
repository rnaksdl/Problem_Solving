/** File: PAssign07.java
 * Class: CSCI 1301
 * Author: Kyumin Lee
 * Created on: Mar 31, 2022
 * Last Modified: Mar 31, 2022
 * Description: letting the user to create and integer array and compute max, min, avg,
 * number of values that are above or under the average. Then prints output.
 */

import java.util.Scanner;

public class PAssign07 {
	public static void main(String[] args) {
		// scaner input, prompting the user and storing the value
		Scanner input = new Scanner(System.in);
		System.out.print("Enter number of values: ");
		int userArrLength = input.nextInt();
		System.out.println();

		// creat array that has number of items that use wants and prompting the user for values
		int[] myArr = new int[userArrLength];
		for (int i = 0; i < userArrLength; i++) {
			System.out.printf("Enter value (%d of %d): ", i + 1, userArrLength);
			int userArrValue = input.nextInt();
			myArr[i] = userArrValue;
		}

		// getting max, min values and indexes
		int max = myArr[0];
		int maxIndex = 0;
		int min = myArr[0];
		int minIndex = 0;
		for (int i = 1; i < myArr.length; i++) {
			if (myArr[i] > max) {
				max = myArr[i];
				maxIndex = i;
			}
			if (myArr[i] < min) {
				min = myArr[i];
				minIndex = i;
			}
		}

		// output
		System.out.println();
		printArr(myArr);
		System.out.println();

		System.out.printf("Maximum: %d at index %d%n", max, maxIndex);
		System.out.printf("Minimum: %d at index %d%n", min, minIndex);
		System.out.printf("Average: %.4f%n", arrAverage(myArr));
		System.out.printf("Values over average: %d%n", overArg(myArr));
		System.out.printf("Values under average: %d%n", underArg(myArr));
	}

	// mathod to print the indexes of the array
	public static void printArr(int[] arr) {
		for (int i = 0; i < arr.length; i++) {
			System.out.printf("Index %d: %d%n", i, arr[i]);
		}
	}

	// mathod to get average
	public static double arrAverage(int[] arr) {
		double average = 0;
		double sum = 0;
		for (int i = 0; i < arr.length; i++) {
			sum += arr[i];
		}
		average = sum / arr.length;
		return average;
	}

	// mathod to count number of values that are over average
	public static int overArg(int[] arr) {
		int numOfOver = 0;
		for (int i = 0; i < arr.length; i++) {
			if (arr[i] > arrAverage(arr)) {
				numOfOver++;
			}
		}
		return numOfOver;
	}

	// mathod to count number of values that are under average
	public static int underArg(int[] arr) {
		int numOfUnder = 0;
		for (int i = 0; i < arr.length; i++) {
			if (arr[i] < arrAverage(arr)) {
				numOfUnder++;
			}
		}
		return numOfUnder;
	}
}