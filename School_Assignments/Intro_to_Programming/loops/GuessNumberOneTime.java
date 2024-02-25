import java.util.Scanner;

public class GuessNumberOneTime {
	public static void main(String[] args) {
		// Generate a random number to be guessed
		int number = (int)(Math.random() * 101);

		Scanner input = new Scanner(System.in);

		// Prompt the user to guess the number
		System.out.println("Guess a number between 0 and 100: ");
		int guess = input.nextInt();

		if (guess == number)
			System.out.println("Yes, the number is " + number);
		else if (guess > number)
			System.out.println("Your guess is too high");
		else 
			System.out.println("Your guess is too low");    
	}
}