import java.util.Scanner;

public class MoreGem {
	
	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		
		int stage = 0, time = 0, coin = 0, jam = 0, monster = 0;
		
		System.out.print("Enter stage: ");
		stage = input.nextInt();
		System.out.print("Enter time: ");
		time = input.nextInt();
		System.out.print("Enter coin: ");
		coin = input.nextInt();
		System.out.print("Enter jam: ");
		jam = input.nextInt();
		System.out.print("Enter monster: ");
		monster = input.nextInt();
		
		System.out.println();
		
		Gem game1 = new Gem(stage, time, coin, jam, monster);
		game1.gameInfo();
	}
}
