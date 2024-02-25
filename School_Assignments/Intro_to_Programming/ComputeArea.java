/**
 * File: ComputeArea.java
 * Description: Computer the area of a circle based on a
 * 				hard-coded radius.  
 * 				Circle area:  pi * r^2  
 */

public class ComputeArea {
	public static void main(String[] args) {
		double radius; // Declare radius
		double area; // Declare area

		// Assign a radius
		radius = 20.0; // New value is radius

		// Compute area
		area = radius * radius * 3.14159;

		// Display results
		System.out.println("The area for the circle of radius " +
								radius + " is " + area);
	}
}




