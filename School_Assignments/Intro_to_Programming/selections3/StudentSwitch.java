import java.util.*;

public class StudentSwitch {
	public static void main(String[] args) {
		int studentCode = 2;
		String studentType = "";

		// switch on studentCode to determine studentType
		switch (studentCode) {
		case 1:
			studentType = "In state";
			break;
		case 2:
			studentType = "Out of state";
			break;
		case 3:
			studentType = "International";
			break;
		case 4:
			studentType = "Dual enrollment";
			break;
		default:
			studentType = "Other";
			break;
		}

		System.out.println("Code " + studentCode + ": " + studentType);
	}

}
