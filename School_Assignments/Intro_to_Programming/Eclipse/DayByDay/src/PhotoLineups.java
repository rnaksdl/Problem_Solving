import java.util.Scanner;
import java.util.ArrayList;

public class PhotoLineups {

	// TODO: Write method to create and output all permutations of the list of names.
	public static void printAllPermutations(ArrayList<String> permList, ArrayList<String> nameList) {
		ArrayList<String> names = (ArrayList<String>) nameList.clone();
		String tempString;

		if (names.isEmpty()) {
			for (int i = 0; i < permList.size(); i++) {
				System.out.print(permList.get(i));
				if(i != permList.size() - 1) {
					System.out.print(", ");

				}
			}
			System.out.println();
		} else {
			for (int i = 0; i < names.size(); i++) {
				tempString = names.remove(i);
				permList.add(tempString);

				printAllPermutations(permList, names);

				names.add(i, tempString);
				permList.remove(tempString);
			}
		}
	}

	public static void main(String[] args) {
		Scanner scnr = new Scanner(System.in);
		ArrayList<String> nameList = new ArrayList<String>();
		ArrayList<String> permList = new ArrayList<String>();
		String name;
		
		// TODO: Read in a list of names; stop when -1 is read. Then call recursive method.
		name = scnr.next();
		while (!name.equals("-1")) {
			nameList.add(name);
			name = scnr.next();
		}
		printAllPermutations(permList, nameList);
	}
}