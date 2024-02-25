import java.util.Scanner;

public class InputAndOutput {
	
	public static void main(String[] args) {
		
		int[] arr = {30, 1, 29, 49, 33};
		
		insertionSort(arr);
		
		
		for (int i = 0; i < arr.length; i++) {
			System.out.printf("%d, ", arr[i]);
		}
	}

	public static int[] insertionSort(int[] arr) {
				
		for (int i = 1; i < arr.length; i++) {
			int temp = arr[i];
			for (int j = i - 1; j >= 0 && temp < arr[j]; j--) {
				
				arr[j + 1] = arr[j];
				arr[j + 1] = temp;
				for (int k = 0; i < arr.length; i++) {
					System.out.printf("%d, ", arr[i]);
				}
			}
		}
		return arr;
		
	}
}
