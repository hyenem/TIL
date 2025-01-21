package SWEA_1859_백만장자프로젝트;

import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case = 1; test_case<=T; test_case++) {
			int N = sc.nextInt();
			long[] arr = new long[N];
			for (int i =0; i<N; i++) {
				arr[i]=sc.nextLong();
			}
			
			long ans = 0;
			long tmpAns =0;
			int acc = 0;
			end: for(int i = 0; i<N; i++) {
				for (int j = i+1; j<N; j++) {
					if(arr[i]<arr[j]) {
						acc++;
						tmpAns-=arr[i];
						continue end;
					}
				}
				tmpAns += acc*arr[i];
				if(tmpAns>0) ans+=tmpAns;
				acc=0;
				tmpAns=0;
			}
			
			System.out.println("#"+test_case+" "+ans);
		}
	}
}