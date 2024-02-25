import java.util.Scanner;

public class Revel {
	public static void main(String[] args) {
		
		double factorial = 1;
		int approx = 0;
		
		for(int i = 1; i <= 5; i++) {
			factorial *= i;
		}
		System.out.println(factorial);
		
	}
}