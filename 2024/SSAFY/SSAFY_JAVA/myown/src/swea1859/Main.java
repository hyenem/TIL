package swea1859;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case = 1; test_case<T+1; test_case++) {
			int N = sc.nextInt();
			int[] arr = new int[N];
			int[] maxIdx = new int[N];
			int point = 0;
			
			for (int i = 0; i<N ; i++) {
				arr[i]=sc.nextInt();
			}
			
			end :for (int i = 0; i<N; i++) {
				for (int j = i+1; j<N; j++) {
					if(arr[i]<arr[j]) continue end;
				}
				maxIdx[point++]=i;
			}
			
			int ans = 0;
			int res = 0;
			for (int j = 0; j<maxIdx[0]; j++) {
				res -= arr[j];
			}
			res += arr[maxIdx[0]]*(maxIdx[0]);
			if (res>0) ans += res;
			
			for(int i = 1; i<point; i++) {
				res = 0;
				for (int j = maxIdx[i-1]+1; j<maxIdx[i]; j++) {
					res -= arr[j];
				}
				res += arr[maxIdx[i]]*(maxIdx[i]-maxIdx[i-1]);
				if (res>0) ans += res;
			}
			
			System.out.println(ans);
		}
	}

}
