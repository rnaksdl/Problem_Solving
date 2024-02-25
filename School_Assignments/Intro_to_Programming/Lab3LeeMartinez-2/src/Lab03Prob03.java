/** 
 * File: Lab 3 Prob 03
 * Class: CSCI 1301
 * @author Jonathan Martinez, Kyumin Lee
 * Created On: Jan 28, 2022
 * Last Modified: Jan 28, 2022
 * Description: create program that prompts user to enter credit hours taken, and total credit hours and prints to screen,
 along with credit hours needed,semesters needed, and years needed for graduation.
 */

// import the java scanner
import java.util.Scanner;
// declare the main method
public class Lab03Prob03 {
public static void main(String [] args ) {
	//input scanner and prompt user for current credit hours
	Scanner input = new Scanner(System.in);
	System.out.print("Enter current accumulated credit hours: ");
	int creditHours = input.nextInt();
	// prompt the user for the total credit hours needed
	System.out.print("Enter total hours needed for undergraduate degree: ");
	int creditTotal = input.nextInt();
	// create variable for credit hours until graduation by subtracting total hours by hours taken
	int creditNeeded = creditTotal - creditHours;
	// create variable for number of semesters needed for graduation by dividing credit hours needed by 15
	double semesterNeeded = creditNeeded / 15.0;
	// create for variable for number of years needed for graduation by dividing semester(s) needed by 2
	double yearNeeded = semesterNeeded / 2.0;
	// create for variable for number of years needed for graduation by dividing semester(s) needed by 3
	double yearNeededSummer = semesterNeeded / 3.0;
	//  create variables for years left, semesters left, and credits left for graduation.
	int yearLeft = creditNeeded / 30;
	int semesterLeft = (creditNeeded % 30) / 15;
	int creditLeft = (creditNeeded % 30) % 15;

	// Display the current taken credit hours
	System.out.println("You have " + creditHours + " credit hour(s).");
	// Display total credit hours needed
	System.out.println("Your degree requires " + creditTotal + " credit hour(s).");	
	// Display the credit hours needed for graduation  
	System.out.println("You have " + creditNeeded + " credit hour(s) until graduation.");
	// Display the semesters needed for graduation
	System.out.println("You have " + semesterNeeded + " semesters (@ 15 credit hours/semester) left until graduation.");
	// Display the years needed until graduation left if only taking 2 semesters per year
	System.out.println("You have " + yearNeeded + " years (@ 2 semesters/year) left until graduation.");
	// Display the years needed until graduation left if taking 3 semesters per year
	System.out.println("You have " + yearNeededSummer + " years (@ 3 semesters/year) left until graduation.");
	// Display the years, semesters, and credit hours (2 semesters/year) needed until graduation
	System.out.println("You have " + yearLeft + " year(s), " + semesterLeft + " semester(s), and " + creditLeft + 
	" credit hour(s) (@ 2 semesters/year) left until graduation.");
	
}
}
