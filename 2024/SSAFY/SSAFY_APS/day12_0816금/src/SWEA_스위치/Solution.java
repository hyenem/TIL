package SWEA_스위치;

import java.util.Arrays;
import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] arr = new int[N];
		for(int i = 0; i<N; i++) {
			arr[i]=sc.nextInt();
		}
		
		int K = sc.nextInt();
		for(int i = 0; i<K; i++) {
			if(sc.nextInt()==1) {
				int index = sc.nextInt();
				for(int j = 1; j<=N/index; j++) {
					arr[index*j-1]=1-arr[index*j-1];
				}
			} else {
				int nowNum =sc.nextInt()-1;
				arr[nowNum]=1-arr[nowNum];
				
				int left = nowNum-1;
				int right = nowNum+1;
				while(left>=0 && right<N && arr[left]==arr[right]) {
					arr[left]=1-arr[left--];
					arr[right]=1-arr[right++];
				}
			}
		}
		
		for(int i=0 ; i<N/20+1; i++) {
			for(int j=0; j<20; j++) {
				if(i*20+j>=N) return;
				System.out.print(arr[i*20+j]+" ");
			}
			System.out.println();
		}
	}
}
