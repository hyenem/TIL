package SWEA_1873_상호의배틀필드;

import java.util.Scanner;

public class Solution {
	
	static char[][] map;
	static int[] start = new int[2];
	static int H, W;
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case=1; test_case<=T; test_case++) {
			H = sc.nextInt();
			W = sc.nextInt();
			
			map = new char[H][W];
			for(int i = 0; i<H; i++) {
				String str = sc.next();
				for(int j = 0; j<W; j++) {
					map[i][j]=str.charAt(j);
					if(map[i][j]=='^'|| map[i][j]=='v'||
							map[i][j]=='<'|| map[i][j]=='>') {
						start[0]=i;
						start[1]=j;
					}
				}
			}
			
			int N = sc.nextInt();
			String str = sc.next();
			for(int i = 0; i<N; i++) {
				if(str.charAt(i)=='U') U(start);
				else if(str.charAt(i)=='D') D(start);
				else if(str.charAt(i)=='L') L(start);
				else if(str.charAt(i)=='R') R(start);
				else if(str.charAt(i)=='S') S(start);
			}
			
			System.out.print("#"+test_case+" ");
			for(int i = 0; i<H; i++) {
				for(int j = 0; j<W; j++)
					System.out.print(map[i][j]);
				System.out.println();
			}
		}
		
	}
	
	static void U(int[] start) {
		if(start[0]-1>=0 && map[start[0]-1][start[1]]=='.') {
			map[start[0]-1][start[1]]='^';
			map[start[0]][start[1]]='.';
			start[0]--;
			return;
		}
		map[start[0]][start[1]]='^';
	}
	
	static void D(int[] start) {
		if(start[0]+1<H && map[start[0]+1][start[1]]=='.') {
			map[start[0]+1][start[1]]='v';
			map[start[0]][start[1]]='.';
			start[0]++;
			return;
		}
		map[start[0]][start[1]]='v';
	}
	static void L(int[] start) {
		if(start[1]-1>=0 && map[start[0]][start[1]-1]=='.') {
			map[start[0]][start[1]-1]='<';
			map[start[0]][start[1]]='.';
			start[1]--;
			return;
		}
		map[start[0]][start[1]]='<';
	}
	static void R(int[] start) {
		if(start[1]+1<W && map[start[0]][start[1]+1]=='.') {
			map[start[0]][start[1]+1]='>';
			map[start[0]][start[1]]='.';
			start[1]++;
			return;
		}
		map[start[0]][start[1]]='>';
	}
	
	static void S(int[] start) {
		int direction=0;
		if(map[start[0]][start[1]]=='v') direction=1;
		else if(map[start[0]][start[1]]=='<') direction=2;
		else if(map[start[0]][start[1]]=='>') direction=3;
		
		int[] shot = new int[2];
		shot[0] = start[0];
		shot[1] = start[1];
		while(shot[0]>=0 && shot[0]<H
				&& shot[1]>=0 && shot[1]<W
				&& map[shot[0]][shot[1]]!='#'
				&& map[shot[0]][shot[1]]!='*') {
			shot[0]+=dx[direction];
			shot[1]+=dy[direction];
		}
		if(!(shot[0]>=0 && shot[0]<H
				&& shot[1]>=0 && shot[1]<W)) return;
		if(map[shot[0]][shot[1]]=='*') map[shot[0]][shot[1]]='.';
	}
	
}
