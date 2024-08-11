package SWEA_1289_원재의메모리복구;

import java.util.Scanner;

class Solution
{
	public static void main(String[] args){
        Scanner sc= new Scanner(System.in);
        int T =sc.nextInt();
        for (int test_case = 1; test_case<T+1; test_case++){
            int sum = 0;
            String str = 0+sc.next();
            for (int i = 1; i<str.length(); i++){
                if(str.charAt(i-1)!=str.charAt(i)) sum++;
            }
            System.out.println("#"+test_case+" "+sum);
        }
    }
}