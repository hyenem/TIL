package SWEA_1215_회문1;

import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		for (int T = 1; T<11; T++) {
			int N = sc.nextInt();
			String[] arr = new String[8];
			for (int i = 0; i<8; i++) {
				arr[i]=sc.next();
			}
			
			int count = 0;
			for (int i = 0; i<8; i++) {
				end: for (int j = 0; j<9-N; j++) {
					for (int k = 0; k<N/2; k++) {
						if(arr[i].charAt(j+k)!=arr[i].charAt(j+N-1-k)) {
							continue end;
						}
					}
					count++;
				}
			}
			
			for (int i = 0; i<8; i++) {
				end: for (int j = 0; j<9-N; j++) {
					for (int k = 0; k<N/2; k++) {
						if(arr[j+k].charAt(i)!=arr[j+N-1-k].charAt(i)) {
							continue end;
						}
					}
					count++;
				}
			}
			
			System.out.println("#"+T+" "+count);
		}
	}
}