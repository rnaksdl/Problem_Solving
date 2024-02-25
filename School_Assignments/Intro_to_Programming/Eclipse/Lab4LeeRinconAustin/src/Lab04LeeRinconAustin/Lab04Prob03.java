/** File: PAssign0.java
 * Class: CSCI 1301
 * Author: Lee, Rincon, Austin
 * Created on: Feb 11, 2022
 * Last Modified: Feb 11, 2022
 * Description:  generates randum number and give status and computes based on status
 */ 

import java.util.Scanner;

public class Lab04Prob03 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		//	user values for side lengths
		System.out.print("Enter first side length");
		double side1 = input.nextDouble();
		System.out.print("Enter second side length");
		double side2 = input.nextDouble();
		System.out.print("Enter third side length");
		double side3 = input.nextDouble();
		
		//	value of s
		double s = (side1 + side2 + side3) / 2;
		
		//	compute area
		double area = Math.sqrt(s * (s - side1) * (s - side2) * (s - side3));
		
		//	print message
		
		System.out.println("For side lengths of " + side1 + ", " + side2 + ", " + side3 + ", the area is " + area + ".");
	}
}
