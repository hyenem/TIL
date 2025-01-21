package swea2805;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
			Scanner sc = new Scanner(System.in);
			int T;
			T=sc.nextInt();
			for(int test_case = 1; test_case <= T; test_case++)
			{
	            int N = sc.nextInt();
	            int[][] arr = new int[N][N];
	            for (int i = 0; i<N; i++){
	                String str = sc.next();
	                for (int j = 0; j<N; j++){
	                    arr[i][j] = str.charAt(j)-'0';
	                }
	            }
	            
	            int sum = 0;
	            for (int i = 0; i<N/2; i++){
	                for (int j = N/2-i; j<N/2+i+1; j++){
	                    sum+=arr[i][j];
	                }
	            }
	            for (int i = 0; i<N; i++){
	                sum += arr[N/2][i];
	            }
	            for (int i = 0; i<N/2; i++){
	                for (int j = N/2-i; j<N/2+i+1; j++){
	                    sum+=arr[N-i-1][j];

	                }
	            }
				System.out.println("#"+test_case+" "+sum);
		}
	}
}
