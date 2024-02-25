/** File: PAssign0.java
 * Class: CSCI 1301
 * Author: Lee, Rincon, Austin
 * Created on: Feb 11, 2022
 * Last Modified: Feb 11, 2022
 * Description:  generates randum number and give status and computes based on status
 */ 

public class Lab04Prob02 {
	public static void main(String[] args) {
		
		//	decairing variables
		double salary = (int)(Math.random()*1000 - 50);
		double raise = 0;
		double statusNum = salary % 7;
		
		//	fiding raise based on status
		if (statusNum == 0) {
			raise = 0;
		}else if (statusNum == 1) {
			raise = 0.037;
		} else if (statusNum == 2) {
			raise = 0.042;
		} else if (statusNum == 3) {
			raise = 0.057;
		} else if (statusNum == 4) {
			raise = 0.061;
		} else if (statusNum == 5) {
			raise = 0.07;
		} else if (statusNum == 6) {
			raise = 0.087;
		}
		
		//	prints message
		double newSalary = salary + salary * raise;
		System.out.println("With a random status of " + statusNum + " and an initial salary of $" + salary + ", your raise is " + raise * 100 +"% "
				+ "which equates to a new salary of $" + newSalary + ".");
	}
}
