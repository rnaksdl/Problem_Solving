
public class Experiments {
	public static void main(String[] args) {
		calculatePI(3, 22);
	}
	
	public static void calculatePI(int top, int num) {
		
		if(num <= 7) {
			num *= 10;
		}
		top = num / 7;
		num -= top * 7;
		num %= 7;
		System.out.println(top);
		calculatePI(top, num);
	}
}
