 /*
 * File: Lab07Prob02.java  
 * Class: CSCI 1301  
 * Author: Hunter & Lee 
 * Created on: March 11, 2022
 * Description: Average functions and the average function
 *
 * */

//import java.util.*;
public class Lab07Prob02 {

	
	
	public static double average(int a, int b, int c) {		
		return (a + b + c) / 3.0;
	}
	public static void main(String[] args) {
			
		int a = 2, b = 3, c = 6;
		System.out.printf("The average of %d, %d, and %d is %.5f%n", a, b, c, average(a, b,c));
		
	}

}
