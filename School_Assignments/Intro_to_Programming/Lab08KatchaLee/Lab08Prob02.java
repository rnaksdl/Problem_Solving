/**
 * File: Lab08Prob01.java 
 * Class: CSCI 1301 
 * Author: Mercy Katcha, Kyumin Lee
 * Created on: March 25, 2022
 * Last Modified:March 25, 2022 
 * Description: finding values from array using index.
 */
public class Lab08Prob02 {
	public static void main(String[] args) {
		//create array
		double[] myArray = { -12.6018020118, 15.3437682821, 145.8110691671, 11.1681119916, 82.0442710394,
				155.0005475009, -6.1179400421, 120.1984991874, 38.6575114628, 77.1494972203 };

		//create loop to print in order of values 
		for (int i = 0; i < myArray.length; i++) {
			//print array in order
			System.out.printf("Index %d of %d: %.5f\n", i, myArray.length - 1, myArray[i]);
		}
	}
}
