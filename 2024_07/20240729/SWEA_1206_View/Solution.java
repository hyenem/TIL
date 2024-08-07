package SWEA_1206_View;

import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	public static void main (String[] args){
        Scanner sc = new Scanner(System.in);
        for (int test_case = 1; test_case<11; test_case++){
            int N = sc.nextInt();
            int[] arr = new int[N];
            for (int i = 0; i<N; i++){
                arr[i]=sc.nextInt();
            }
            
            int ans = 0;
            for (int i = 2; i<N-2; i++){
                int Surround = Math.max(Math.max(arr[i-1],arr[i-2]), Math.max(arr[i+1],arr[i+2]));
                if(arr[i]>Surround) {
                    ans+=arr[i]-Surround;
                    i+=2;
                }
            }
            
            System.out.println("#"+test_case+" "+ans);
        }
    }
}