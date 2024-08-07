package SWEA_1217_거듭제곱;

import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		for(int test_case = 1; test_case <= 10; test_case++)
		{
			int T = sc.nextInt();
            int num = sc.nextInt();
            int idx = sc.nextInt();
            System.out.println("#"+T+" "+pow(num,idx));
		}
	}
    
    static int pow(int num, int idx){
        if(idx==1) return num;
        return pow(num,idx-1)*num;
    }
}