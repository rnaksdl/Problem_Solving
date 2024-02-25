
public class Rectangle {
	int width = 1, length = 1;
	
	Rectangle(int newW, int newL) {
		width = newW;
		length = newL;
	}
	
	int getArea() {
		return width * length;
	}
	
	int getPeremeter() {
		return width * 2 + length * 2;
	}
	
	double getDiagonal() {
		return Math.sqrt(width * width + length * length); 
	}
}
