
public class Circle {
	
	
	double radius = 1.0;

	Circle(double newRadius) {
		radius = newRadius;
	}
	
	double getDiameter() {
		return 2 * radius;
	}
	
	double getArea() {
		return Math.PI * radius * radius;
	}
	
	double getPerimeter() {
		return Math.PI * radius * 2.0;
	}
}
