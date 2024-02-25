import java.util.Scanner; 

public class GuessNumber {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		// Generate a random number to be guessed
		int number = (int)(Math.random() * 101);

		int guess = -1; // force loop to execute once
		while (guess != number) {
			// Prompt the user to guess the number
			System.out.println("Guess a number between 0 and 100: ");
			guess = input.nextInt();

			if (guess == number)
				System.out.println("Yes, the number is " + number);
			else if (guess > number)
				System.out.println("Your guess is too high");
			else
				System.out.println("Your guess is too low");
		} // End of loop
	}
}