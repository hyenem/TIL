package SWEA_1966_숫자를정렬하자;

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
            int[] arr = new int[N];
            arr[0]=sc.nextInt();
            for (int i = 1 ; i<N; i++){
                int data = sc.nextInt();
                int j;
                for (j = i-1; j>=0; j--){
                    if(arr[j]<=data) {
                        break;
                    }
                    arr[j+1]=arr[j];
                }
                arr[j+1]=data;
            }
            System.out.print("#"+test_case);
            for (int i = 0; i<N; i++){
                System.out.print(" "+arr[i]);
            }
            System.out.println();
		}
	}
}