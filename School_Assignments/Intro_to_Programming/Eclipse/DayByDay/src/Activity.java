import java.io.*;
import java.util.Scanner;

/**
 * 
 * (cmd + shift + o)
 * @author kyukyu
 *
 *public static String f2s(String s) throws IOException {
		File inputFile = new File(s);
		Scanner input = new Scanner(inputFile);
		String context = "";
		while (input.hasNext()) {
		context += input.nextLine();
		}
		return context;
		}
 */


public class Activity {
	public static String copyFile(String file) {
		File file1 = new File(file);
		
		try (
			Scanner input = new Scanner(file1);
		){
			String output = "";
			while(input.hasNext()) {
				output += file;
				return output;
			}
		} catch (Exception ex) {
			ex.printStackTrace();
		}
		return null;
	}
}