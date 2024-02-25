/**
 * File: PAssign02.java
 * Class: CSCI 1301
 * Author: Kyumin Lee
 * Created on: Feb 2, 2022
 * Last Modified: Feb 2, 2022
 * Description:  Java program that calculates a weighted-average using the weights from this course 
 */

import java.util.Scanner;

public class PAssign02 {
	public static void main(String[] args) {
	
		// declare variables
		int numOfGrade = 7;
		double revel, assign, lab, exam1, exam2, exam3, finalExam, finalGrade;
		
		Scanner input = new Scanner(System.in);
		
		//	input for Revel grade
		System.out.print("Enter Revel grade: ");
		revel = input.nextDouble();
		
		//	input for Programming Assignments grade
		System.out.print("Enter Programming Assignments grade: ");
		assign = input.nextDouble();
		
		//	input for Lab grade
		System.out.print("Enter Lab grade: ");
		lab = input.nextDouble();
		
		//	input for Exam 1 grade
		System.out.print("Enter Exam 1 grade: ");
		exam1 = input.nextDouble();
		
		//	input for Exam 2 grade
		System.out.print("Enter Exam 2 grade: ");
		exam2 = input.nextDouble();
		
		//	input for Exam 3 grade
		System.out.print("Enter Exam 3 grade: ");
		exam3 = input.nextDouble();
		
		//	input for Final Exam grade
		System.out.print("Enter Final Exam grade: ");
		finalExam = input.nextDouble();
		
		//	compute final grade
		finalGrade = (revel * 0.1) + (assign * 0.1) + (lab * 0.1) + (exam1 * 0.15) + (exam2 * 0.15) + (exam3 * 0.15) + (finalExam * 0.25);
		
		//print
		System.out.println("There were " + numOfGrade + " grades entered.");
		System.out.println("The final grade for this course is " + finalGrade + ".");
	}
}