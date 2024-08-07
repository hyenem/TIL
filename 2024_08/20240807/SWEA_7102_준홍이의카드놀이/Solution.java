package SWEA_7102_준홍이의카드놀이;

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
            int N = sc.nextInt();
            int M = sc.nextInt();
            
            int min = Math.min(M,N);
            int max = Math.max(M,N);
            
            System.out.print("#"+test_case);
            for (int i = min+1; i<max+2; i++){
                System.out.print(" "+i);
            }
            System.out.println();
		}
	}
}