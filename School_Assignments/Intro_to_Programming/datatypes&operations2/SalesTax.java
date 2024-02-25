import java.util.Scanner;

public class SalesTax {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		// prompt user for purchase amount
		System.out.print("Enter purchase amount: ");
		double purchaseAmount = input.nextDouble();

		// calculate tax
		double tax = purchaseAmount * 0.07;

		// * 100 / 100 is a hack for two digits, avoid, will not need after Chapter 4
		System.out.println("Sales tax is $" + (int)(tax * 100) / 100.0);

	}
}