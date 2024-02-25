import java.util.Scanner;

public class ComputeLoan {
	public static void main(String[] args) {   
		// Create a Scanner
		Scanner input = new Scanner(System.in);

		// Enter yearly interest rate
		System.out.print("Enter yearly interest rate, for example 8.25: ");
		double annualInterestRate = input.nextDouble();

		// Obtain monthly interest rate
		double monthlyInterestRate = annualInterestRate / 1200;

		// Enter number of years
		System.out.print(
				"Enter number of years as an integer, for example 5: ");
		int numberOfYears = input.nextInt();

		// Enter loan amount
		System.out.print("Enter loan amount, for example 12000.95: ");
		double loanAmount = input.nextDouble();

		// Calculate payment
		double monthlyPayment = loanAmount * monthlyInterestRate / (1
				- 1 / Math.pow(1 + monthlyInterestRate, numberOfYears * 12));
		double totalPayment = monthlyPayment * numberOfYears * 12;

		// Display results
		// * 100 / 100 is a hack for two digits, avoid, will not need after Chapter 4
		System.out.println("The monthly payment is $" + 
				(int)(monthlyPayment * 100) / 100.0);
		System.out.println("The total payment is $" + 
				(int)(totalPayment * 100) / 100.0);
	}
}