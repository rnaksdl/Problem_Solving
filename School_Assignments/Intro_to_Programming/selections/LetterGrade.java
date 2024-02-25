/**
 * File: LetterGrade.java
 * @author Christopher Williams
 * Created on: Jun 13, 2017
 * Description:  Determine the corresponding letter grade to a numeric grade
 */
public class LetterGrade {

	public static void main(String[] args) {
		double score = 85.2;

		if (score >= 90.0) {
			System.out.print("A");
		} else if (score >= 80.0) {
			System.out.print("B");
		} else if (score >= 70.0) {
			System.out.print("C");
		} else if (score >= 60.0) {
			System.out.print("D");
		} else {
			System.out.print("F");
		}
	}

}
