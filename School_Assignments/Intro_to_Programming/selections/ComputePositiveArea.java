/**
 * File: ComputePositiveArea.java
 * @author Christopher Williams
 * Created on: Jun 13, 2017
 * Description: Compute the area of a circle, only if the radius is positive  
 */

public class ComputePositiveArea {

	public static void main(String[] args) {
		double radius = 5.0, area = 0.0;

		if (radius >= 0) {   
			area = radius * radius * 3.14159;

			System.out.println("The area for the "  
					+ "circle of radius " + radius + 
					" is " + area);
		} else {
			System.out.println("No negative radius");
		}

	}

}
