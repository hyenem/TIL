package SWEA_4613_러시아국기같은깃발;

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
            int[][] arr=new int[N][3];
            for (int i = 0; i<N; i++){
                String str = sc.next();
                for (int j = 0; j<M; j++){
                    if (str.charAt(j)=='W') arr[i][0]++;
                    else if(str.charAt(j)=='B') arr[i][1]++;
                    else arr[i][2]++;
                }
            }
            int max = 0;
            for (int i = 1; i<N-1; i++){
                for (int j = i+1; j<N; j++){
                    int sum = 0;
                    for (int k = 0; k<i; k++) sum+=arr[k][0];
                    for (int k = i; k<j; k++) sum += arr[k][1];
                    for (int k = j; k<N; k++) sum += arr[k][2];
                    if(max<sum) max = sum;
                }
            }
            System.out.println("#"+test_case+" "+(M*N-max));
        }
	}
}