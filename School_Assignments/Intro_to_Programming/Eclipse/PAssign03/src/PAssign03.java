/** File: PAssign03.java
 * Class: CSCI 1301
 * Author: Kyumin Lee
 * Created on: Feb 14, 2022
 * Last Modified: Feb 14, 2022
 * Description:  Prompts the user and gets input to determine and compute output
 */ 

import java.util.Scanner;

public class PAssign03 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		//	declare variables for number of drinks and sandwiches
		double drinkNum;
		double sandwichNum;
		
		// declare variables and store value for prices for drinks and sandwiches
		double drinkPrice = 0.5;
		double sandwichPrice = 2.75;
		
		//	prompt the user for number of drinks
		System.out.println("Enter the number of beverages: ");
		drinkNum = input.nextDouble();
		//	outputs based on quantity
		
		while (drinkNum == 0) {
			System.out.println("ERROR: A quantity of zero is not allowed.");
			System.out.println("Enter the number of beverages: ");
			drinkNum = input.nextDouble();
		}
		System.out.println("Ordered: " + drinkNum + " beverages");
		
		//	prompt the user for number of sandwiches
		System.out.println("Enter the number of sandwiches: ");
		sandwichNum = input.nextDouble();
		//	outputs based on quantity
		while (sandwichNum == 0) {
			System.out.println("ERROR: A quantity of zero is not allowed.");
			System.out.println("Enter the number of sandwiches: ");
			sandwichNum = input.nextDouble();
		}
		System.out.println("Ordered: " + sandwichNum + " sandwiches");
		
		//
		if (drinkNum > 0 && sandwichNum > 0) {
			double subtotal = drinkNum * drinkPrice + sandwichNum * sandwichPrice;
			double total = subtotal + subtotal * 0.075;
			System.out.println("The subtotal of " + drinkNum + " beverages and " + sandwichNum + " sandwiches is $" + subtotal + ".");
			System.out.println("With tax, the total is $" + total + ".");
		} else {
			System.out.println("Your order total could not be calculated due to a zero quantity for an item.");
		}
	}
}
