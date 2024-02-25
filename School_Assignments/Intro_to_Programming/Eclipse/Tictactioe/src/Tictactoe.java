/** File: Tictactoe.java
 * Class: project tictactoe
 * Author: Kyumin Lee
 * Created on: April 8, 2022
 * Last Modified: 
 * Description: 
 * 
 * random bot mode?
 */

import java.util.Scanner;

public class Tictactoe {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		int boardSize = 3;
		String usrValue = "", user1 = "X", user2 = "O";


		String[][] board = new String[3][3];
		boardArr(board,usrValue);
		printArr(board);


	}

	public static String[][] boardArr(String[][] board, String sqr) {
		for (int i = 0; i < board.length; i++) {
			for (int j = 0; j < board.length; j++) {
				board[i][j] = sqr;
			}
		}
		return board;
	}

	public static void printArr(String[][] arr) {
		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr.length; j++) {
				System.out.printf("%s ",arr[i][j]);
			}
			System.out.println();
		}
	}


	/** Determine if the passed board has a winner */
	public static boolean isWon(int[][] board) {
		// check all rows for matches
		for (int i = 0; i < 3; i++)
			if ((board[i][0] == board[i][1])
					&& (board[i][1] == board[i][2])) {
				return true;
			}

		// check all columns for matches
		for (int j = 0; j < 3; j++)
			if ((board[0][j] == board[1][j])
					&& (board[1][j] == board[2][j])) {
				return true;
			}

		// check diagonals
		if ((board[0][0] == board[1][1])
				&& (board[1][1] == board[2][2])) {
			return true;
		}

		if ((board[0][2] == board[1][1])
				&& (board[1][1] == board[2][0])) {
			return true;
		}

		return false;
	}
}