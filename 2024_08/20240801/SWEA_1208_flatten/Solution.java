package SWEA_1208_flatten;

import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		for (int test_case = 1; test_case < 2; test_case++) {

			int N = sc.nextInt();
			int[] count = new int[100];

			for (int i = 0; i < 100; i++) {
				count[sc.nextInt() - 1]++;
			}

			int min = 0;
			int max = 99;
			for (int i = 0; i < 100; i++) {
				if (count[i] != 0) {
					min = i;
					break;
				}
			}
			for (int i = 0; i < 100; i++) {
				if (count[99 - i] != 0) {
					max = 99 - i;
					break;
				}
			}

			for (int i = 0; i < N; i++) {
				if (max == min)
					break;
				if (count[min] == 0) {
					min++;
				}
				if (count[max] == 0) {
					max--;
				}
				count[min]--;
				count[min + 1]++;
				count[max]--;
				count[max - 1]++;
			}
			if (count[min] == 0) {
				min++;
			}
			if (count[max] == 0) {
				max--;
			}

			System.out.println("#" + test_case + " " + (max - min));
		}
	}
}