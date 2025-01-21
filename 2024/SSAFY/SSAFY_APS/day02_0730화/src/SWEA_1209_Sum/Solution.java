package SWEA_1209_Sum;

import java.util.Scanner;
import java.io.FileInputStream;


class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		for (int test_case=1; test_case<11; test_case++) {
            int T =sc.nextInt();
			int[][] arr = new int[100][100];
			for (int i = 0; i<100; i++) {
				for (int j = 0; j<100; j++) {
					arr[i][j]= sc.nextInt();
				}
			}
			
			int ans = 0;
			int max = 0;
			int sum3 = 0;
			int sum4 = 0;
			for (int i = 0; i<100; i++) {
                int sum=0;
                int sum2=0;
				for (int j = 0; j<100; j++) {
					sum+=arr[i][j];
					sum2+=arr[j][i];
				}
				sum3+=arr[i][i];
				sum4+=arr[i][99-i];
				max = Math.max(sum, sum2);
				if (ans<max) ans = max;
			}
			max = Math.max(sum3, sum4);
			if (ans<max) ans = max;
			
			System.out.println("#"+test_case+" "+ans);
		}
	}
}