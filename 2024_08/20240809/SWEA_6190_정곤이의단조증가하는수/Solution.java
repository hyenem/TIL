package SWEA_6190_정곤이의단조증가하는수;

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
            int[] arr= new int[N];
            int ans = 0;
            for (int i = 0; i<N; i++){
                arr[i]=sc.nextInt();
            }
            for (int i = 0; i<N-1; i++){
                end: for (int j = i+1; j<N; j++){
                    int now = arr[i]*arr[j];
                    String strnow = Integer.toString(now);
                    for(int k = 1; k<strnow.length(); k++){
                        if(strnow.charAt(k-1)>strnow.charAt(k)) continue end;
                    }
                    if(ans<now) ans = now;
                }
            }
            if (ans ==0) System.out.println("#"+test_case+" "+(-1));
            else System.out.println("#"+test_case+" "+ans);
		}
	}
}