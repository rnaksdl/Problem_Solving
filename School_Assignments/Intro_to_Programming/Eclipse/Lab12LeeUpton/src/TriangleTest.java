/**
 * File: Triangle.java Class: CSCI 1301 Author: Adrian Quinones and Kyumin Lee
 * Created on: April 22, 2022 Description: Create a stronger triangle object.
 *
 */

public class Triangle {

	// declare new variables
	private double sideA, sideB, sideC;
	private static double largestInitialArea = 0;
		
	
	// default no argument constructor
	public Triangle() {
		setSideA(3);
		setSideB(4);
		setSideC(5);
		checkInitialArea();
	}

	// object constructor
	public Triangle(double newSideA, double newSideB, double newSideC) {
		setSideA(newSideA);
		setSideB(newSideB);
		setSideC(newSideC);
		checkInitialArea();

	}

	// Get Side A
	public double getSideA() {
		return sideA;
	}

	// Set Side A
	public double setSideA(double sideA) {
		if (sideA > 0) {
			this.sideA = sideA;
		}
		return sideA;
	}

	// Get Side B
	public double getSideB() {
		return sideB;
	}

	// Set Side B
	public double setSideB(double sideB) {
		if (sideB > 0) {
			this.sideB = sideB;
		}
		return sideB;
	}

	// Get Side C
	public double getSideC() {
		return sideC;
	}

	// Set Side C
	public double setSideC(double sideC) {
		if (sideC > 0) {
			this.sideC = sideC;
		}
		return sideC;
	}
	
	public static double getLargestInitialArea() {
		return largestInitialArea;
	}
	
	public void checkInitialArea() {
		if (getArea() > largestInitialArea) {
			largestInitialArea = getArea();
		}
	}

	// Calculate area of triangle object
	public double getArea() {
		double semiPerimeter = (sideA + sideB + sideC) / 2;
		return Math.sqrt(semiPerimeter * (semiPerimeter - sideA) * (semiPerimeter - sideB) * (semiPerimeter - sideC));
	}

	// Calculate perimeter of triangle object
	public double getPerimeter() {
		return sideA + sideB + sideC;

	}
	
	//Side A: sideAValue Side B: sideBValue Side C: sideCValue Area: areaValue Perimeter:perimeterValue
	public String getInfo() {
		String info = String.format("Side A: %.2f Side B: %.2f Side C: %.2f Area: %.2f Perimeter: %.2f", sideA, sideB, sideC, getArea(), getPerimeter());
		return info;
	}
}

public class TriangleTest {
	public static void main(String[] args) {
	Triangle tri1 = new Triangle(3, 4, 5);
	Triangle tri2 = new Triangle(1, 1, 1);
	Triangle tri3 = new Triangle(2.5, 4.6, 3.2);
	System.out.println(tri1.getInfo());
	System.out.println(tri2.getInfo());
	System.out.println(tri3.getInfo());
	}
}