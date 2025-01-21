package SWEA_1213_String;

import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		for (int test_case = 1; test_case<11; test_case++) {
			int T = sc.nextInt();
			String search = sc.next();
			String line = sc.next();
			int ans = 0;
			end:for (int i = 0; i<line.length()-search.length()+1; i++) {
				for (int k = 0; k<search.length(); k++) {
					if(line.charAt(i+k)!=search.charAt(k)) continue end;
				}
				ans++;
			}
			
			System.out.println("#"+T+" "+ans);
		}
	}
}