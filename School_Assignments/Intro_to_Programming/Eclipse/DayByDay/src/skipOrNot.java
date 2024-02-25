
public class skipOrNot {
	public static void main(String[] args) {
  
		int[][][] arr = {
			    {{5, 5}, {5, 5}, {5, 5}, {5, 5}},
			    {{7, 7}, {7, 7}, {7, 7}, {7, 7}},
			    {{8, 30}, {8, 31}, {8, 32}, {8, 33}}};
  
        for (int i = 0; i < arr.length; i++) {
  
            for (int j = 0; j < arr[i].length; j++) {
  
                for (int k = 0; k < arr[i][j].length; k++) {
  
                    System.out.printf("%d ", arr[i][j][k]);
                }
  
                System.out.println();
            }
            System.out.println();
        }
    }
}
