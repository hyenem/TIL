package SWEA_1209_Sum;

import java.util.Scanner;

public class Solution {

	static int max;
	static int[][] arr;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		for (int test_case = 0; test_case < 10; test_case++) {
			int T = sc.nextInt();
			arr = new int[100][100];
			for (int i = 0; i < 100; i++) {
				for (int j = 0; j < 100; j++) {
					arr[i][j] = sc.nextInt();
				}
			}
			
			max = 0;
			int sum1 = 0;
			int sum2 = 0;
			for (int i = 0; i < 100; i++) {
				rowSum(i);
				colSum(i);
				sum1 += arr[i][i];
				sum2 += arr[i][99 - i];
			}

			max = Math.max(Math.max(sum1, sum2), max);
			System.out.println("#"+T+" "+max);
		}
	}

	static void colSum(int col) {
		int sum = 0;
		for (int i = 0; i < 100; i++) {
			sum += arr[i][col];
		}
		max = Math.max(sum, max);
	}

	static void rowSum(int row) {
		int sum = 0;
		for (int i = 0; i < 100; i++) {
			sum += arr[row][i];
		}
		max = Math.max(sum, max);
	}
}