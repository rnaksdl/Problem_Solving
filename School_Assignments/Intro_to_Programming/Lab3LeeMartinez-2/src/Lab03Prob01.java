/** 
 * File: Lab 3 PRob 01
 * Class: CSCI 1301
 * @author Jonathan Martinez, Kyumin Lee
 * Created On: Jan 28, 2022
 * Last Modified: Jan 28, 2022
 * Description: create program that prompts user to enter credit hours taken, and total credit hours and prints to screen
 */

// import the java scanner
import java.util.Scanner;
// declare the main method
public class Lab03Prob01 {
public static void main(String [] args ) {
	//input scanner and prompt user for current credit hours
	Scanner input = new Scanner(System.in);
	System.out.print("Enter current accumulated credit hours: ");
	int creditHours = input.nextInt();
	// prompt the user for the total credit hours needed
	System.out.print("Enter total hours needed for undergraduate degree: ");
	int creditTotal = input.nextInt();
	
	//Show the current and needed total credit hours
	System.out.println("You have " + creditHours + " credit hour(s).");
	System.out.println("Your degree requires " + creditTotal + " credit hour(s).");	
			
}
}
