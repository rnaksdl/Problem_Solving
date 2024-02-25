/**
 * File: ComputeCircumference.java
 * @author Christopher Williams
 * Created on: Jun 6, 2017
 * Description:  Calculate the circumference of a circle 
 * 				 based on a radius  
 */

public class ComputeCircumference {

	public static void main(String[] args) {
		double radius; // Declare radius
		double circumference; // Declare area

		// Assign a radius
		radius = 20.0; 

		// Compute circumference
		circumference = 2 * radius * 3.14159;

		// Display results
		System.out.println("The circumference for the circle of radius " +
					radius + " is " + circumference);

	}


}
