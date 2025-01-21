package SWEA_2383_점심식사시간;

import java.util.ArrayList;
import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case=1; test_case<=T; test_case++) {
			int N = sc.nextInt();
			ArrayList<int[]> people = new ArrayList<>();
			ArrayList<int[]> stair = new ArrayList<>();
			for(int i = 0; i<N; i++) {
				for(int j = 0; j<N; j++) {
					int tmp = sc.nextInt();
					if(tmp==1) people.add(new int[] {i, j});
					else if(tmp!=0) stair.add(new int[]{i, j, tmp});
				}
			}
			
			int ans = Integer.MAX_VALUE;
			//비트마스크로 팀나누기
			for(int com = 0; com<(1<<people.size()); com++) {
				int tmpans = 0;
				for(int stairnum = 0; stairnum<2; stairnum++) {
					int[] acc = new int[2*N];
					int[] thisStair = stair.get(stairnum);
					for(int i = 0; i<people.size(); i++) {
						if((com&(1<<i))==(stairnum<<i)) {
							int[] person = people.get(i);
							int distance = Math.abs(thisStair[0]-person[0])+Math.abs(thisStair[1]-person[1]);
							acc[distance]++;							
						}
					}

					int[] res = new int[3];
					int count = 0;
					
					for(int i = 0; i<2*N; i++) {
						for(int j = 0; j<acc[i]; j++) {
							res[count%3] = Math.max(res[count%3], i)+thisStair[2];
							count++;
						}
					}
					tmpans=Math.max(Math.max(res[0], res[1]), Math.max(res[2], tmpans));
				}
				ans=Math.min(ans, tmpans);
			}
			System.out.println("#"+test_case+" "+(ans+1));
		}
	}
}
