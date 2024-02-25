/** File: PAssign09.java
 * Class: CSCI 1301
 * Author: Kyumin Lee
 * Created on: April 18, 2022
 * Last Modified: April 18, 2022
 * Description: computes stored 2D array with a method and prints according to tis condition
 */

public class PAssign09 {
	public static void main(String[] args) {
		
		// 2D array
		double[][] shippingContainers = {
				{47.19, 39.19, 36.50}, {59.25, 59.25, 54.50}, {47.25, 29.25, 29.50},
				{23.19, 19.20, 19.50}, {17.33, 17.33, 17.50}, {83.19, 47.25, 42.50},
				{23.33, 19.33, 19.50}, {31.25, 23.25, 23.50}, {29.33, 29.33, 24.50},
				{23.19, 23.19, 23.19}, {35.19, 35.19, 30.50}, {47.19, 44.19, 29.50},
				{40.19, 27.88, 20.00}, {59.19, 47.19, 42.50}, {47.19, 47.19, 22.50},
				{39.33, 39.33, 34.50}, {47.25, 29.25, 29.50}, {35.19, 21.19, 16.50},
				{11.33, 11.33, 11.50}, {47.19, 39.19, 29.50}, {47.19, 47.19, 42.50},
				{66.19, 29.20, 25.00}, {57.19, 41.19, 40.50}, {59.25, 59.25, 42.50},
				{71.25, 47.25, 42.50}
		};
		
		//printing method
		printShippable(shippingContainers);
	}

	public static void printShippable(double[][] a2d) {
		// declaring  volume and cm to inch diff
		double volume, c2i = 0.3937007874;
		String info = "";
		
		for (int i = 0; i < a2d.length; i++) {
			// computing volume
			volume = a2d[i][0] * c2i * a2d[i][1] * c2i * a2d[i][2] * c2i;	
			// output according to condition
//			if (volume >= 2000 && volume <= 7000) {
//				System.out.printf("Container %d (%,.2f in^3) can be shipped%n", i, volume);
//			}
			info = String.format("Container %d (%,.2f in^3) can%s be shipped%n", i, volume,(volume >= 2000 && volume <= 7000) ? "" : "'t");
			System.out.print(info);
		}
	}
}
