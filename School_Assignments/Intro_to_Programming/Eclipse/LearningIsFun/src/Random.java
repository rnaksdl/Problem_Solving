// Practice

import java.util.Scanner;

class Random{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int userValue, randNum = 0;

        System.out.print("Enter a value between 0-10: ");
        userValue = input.nextInt(0);

        randNum = (int)(System.currentTimeMillis() % 11);

        System.out.println("Random: " + randNum);
        System.out.println("Uservalue :" + userValue);
        
        if (randNum == userValue) {
        	System.out.println("The two numbers are equal.");
        } else {
        	System.out.println("The two Numbers are not equal.");
        }
    }
}