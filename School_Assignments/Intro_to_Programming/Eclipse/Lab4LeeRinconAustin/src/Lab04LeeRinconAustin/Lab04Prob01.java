/** File: PAssign0.java
 * Class: CSCI 1301
 * Author: Lee, Rincon, Austin
 * Created on: Feb 11, 2022
 * Last Modified: Feb 11, 2022
 * Description:  generate random number and determine if eligible age
 */ 

public class Lab04Prob01 {
	public static void main(String[] args) {
		//	generate random numbers for age
		int age = (int)(Math.random()*100);
		//	determine if eligible to purchase alcohol based on age
		String Eligible;
		
		if(age >= 21) {
			Eligible = "";
		}	else	{
			 Eligible = "not ";
		}
		System.out.println("You are " + age + " years old and are " + Eligible + "eligible to purchase alcohol.");
		
	}
	
	
}
