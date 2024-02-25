
public class BubbleSort {
	
	public static void main(String[] args) {
		
		// array with 10 random intvalues
		int[] arr = new int[10];
		for (int i = 0; i < 10; i++) {
			arr[i] = (int)(Math.random()*11);
		}
		
		for (int i = 0; i < arr.length; i++) {
			System.out.printf("%d%s", arr[i], (i != 9) ? ", " : "");
		}
		
		System.out.println();		
		System.out.println();

		bubbleSort(arr);
		
		for (int i = 0; i < arr.length; i++) {
			System.out.printf("%d%s", arr[i], (i != 9) ? ", " : "");
		}
		
	}
	
	public static void bubbleSort(int[] arr) {
		int bubble;
		for (int i = 0; i < arr.length; i++) {
			for (int j = i + 1; j < arr.length; j++) {
				if (arr[i] < arr[j]) {
					bubble = arr[j];
					arr[j] = arr[i];
					arr[i] = bubble;
				}
			}
		}
	}
}
