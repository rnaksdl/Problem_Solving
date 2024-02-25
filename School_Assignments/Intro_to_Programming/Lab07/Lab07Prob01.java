 /*
 * File: Lab07Prob01.java  
 * Class: CSCI 1301  
 * Author: Hunter & Lee 
 * Created on: March 11, 2022
 *
 *
 * */

import java.util.*;
public class Lab07Prob01 {

	
	public static double randomMax(double scaledVal, int numRands)	{
		double max = 0;
		for(int i = 0; i < numRands; i++)
		{
			double v = Math.random() * scaledVal ;
			max = v > max ? v : max ;
		}
		return max;		
	}
	public static void main(String[] args) {
			
		
		int hardCodedNumber = 20;
		Scanner s = new Scanner(System.in);
		
		double inputNumber, maxNumber=0;
		do
		{
			System.out.print("\nEnter a positive floating point decimal as a scale value: ");
			inputNumber = s.nextDouble();
			if(inputNumber>0){
				maxNumber=randomMax(inputNumber,hardCodedNumber);
				System.out.print("\nFor "+hardCodedNumber+" random values between 0.0 and "+inputNumber+", the largest value was " + String.format("%.1f", maxNumber) + ".");

			}
		}
		while(inputNumber != 719.2);
		
		
		s.close();
		
		
	
	}

}
