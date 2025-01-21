package swea1493;

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int test_case = 1; test_case<T+1; test_case++) {
			int N = sc.nextInt();
			int M = sc.nextInt();
			int xN = 0;
			int NLevel = 0;
			int xM = 0;
			int MLevel = 0;
			
			for (int i = 0; i<200; i++) {
				if (N<=(i*(i+1))/2) {
					xN=N-(i*(i-1))/2;
					NLevel = i;
					break;
				}
			}
			for (int i = 0; i<200; i++) {
				if (M<=(i*(i+1))/2) {
					xM=M-(i*(i-1))/2;
					MLevel = i;
					break;
				}
			}
			
			int x = xN + xM;
			int y = NLevel-xN+MLevel-xM;
			int sum = x+y;
			System.out.println("#"+test_case+" "+((sum*(sum+1))/2+x));
		}
	}
}
