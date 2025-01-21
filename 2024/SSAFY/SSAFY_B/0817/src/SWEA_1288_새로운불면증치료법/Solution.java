package SWEA_1288_새로운불면증치료법;

import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
            String stringN = sc.next();
            int intN = Integer.parseInt(stringN);
            boolean[] visited = new boolean[10];
            int count = 0;
            int kN = 0;
            while(count<10){
                kN+=intN;
                int nowInt = kN;
                while (nowInt>0){
					if(visited[nowInt%10]) {
                        nowInt/=10;
                        continue;
                    }
                    visited[nowInt%10]=true;
                    count++;
                    nowInt/=10;
                }
            }
            System.out.println("#"+test_case+" "+kN);
		}
	}
}