

/*
 * File: Lab07Prob04.java  
 * Class: CSCI 1301  
 * Author: Hunter & Lee 
 * Created on: March 11, 2022
 * Description: Average overloading functions and MORE
 * */

//import java.util.*;
public class Lab07Prob04 {



	public static double average(int a, int b, int c)	{		
		return (a + b + c) / 3.0;
	}
	public static double average(double a, double b, double c)	{		
		return (a + b + c) / 3.0;
	}
	public static double average(int a, int b, int c, int d)	{		
		return (a + b + c + d) / 4.0;
	}
	public static double average(double a, double b, double c, double d)	{		
		return (a + b + c + d) / 4.0;
	}
	public static void main(String[] args) {

		int a = 2, b = 3, c = 6, d;
		double aa = 2.74, bb = 3.45, cc = 6.21, dd;

		System.out.printf("The average of %d, %d, and %d is %.5f%n", a, b, c, average(a, b,c));
		System.out.printf("The average of %.2f, %.2f, and %.2f is %.5f%n", aa, bb, cc, average(aa, bb, cc));
		a = 2;
		b = 3;
		c = 6;
		d = 11;
		aa = 2.74;
		bb = 3.45;
		cc = 6.21;
		dd = 11.91;

		// Calling these functions with four parameters instead of three parameters matches the signature of our new function, and thus does not call our old function...
		System.out.printf("The average of %d, %d, %d, and %d is %.5f%n", a, b, c, d, average(a, b, c, d));
		System.out.printf("The average of %.2f, %.2f, %.2f, and %.2f is %.5f%n", aa, bb, cc, dd, average(aa, bb, cc, dd));
	}

}
