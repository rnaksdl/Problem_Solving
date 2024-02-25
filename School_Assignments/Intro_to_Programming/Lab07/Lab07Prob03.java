 /*
 * File: Lab07Prob03.java  
 * Class: CSCI 1301  
 * Author: Hunter & Lee 
 * Created on: March 11, 2022
 *  Description: Average overloading functions
 *
 * */

//import java.util.*;
public class Lab07Prob03 {
	public static double average(int a, int b, int c)	{		
		return (a + b + c) / 3.0;
	}
	
	public static double average(double a, double b, double c)	{		
		return (a + b + c) / 3.0;
	}
	
	public static void main(String[] args) {
			
		int a = 2, b = 3, c = 6;
		double aa = 2.74, bb = 3.45, cc = 6.21;
		
		System.out.printf("The average of %d, %d, and %d is %.5f%n", a, b, c, average(a, b,c));
		System.out.printf("The average of %.2f, %.2f, and %.2f is %.5f%n", aa, bb, cc, average(aa, bb, cc));
	}
}