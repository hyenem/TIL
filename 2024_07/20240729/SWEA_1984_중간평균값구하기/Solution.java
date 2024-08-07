package SWEA_1984_중간평균값구하기;

import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
            double[] arr = new double[10];
            double sum = 0;
            double max = 0;
            double min = 10000;
        	for (int i = 0; i<10; i++){
                int nextInt = sc.nextInt();
                sum += nextInt;
                max = Math.max(max, nextInt);
                min = Math.min(min,nextInt);
            }
            double ans = (sum-max-min)/8;
            System.out.printf("#%d %.0f\n", test_case, ans);
           
		}
	}
}