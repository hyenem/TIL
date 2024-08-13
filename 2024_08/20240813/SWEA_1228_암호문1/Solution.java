package SWEA_1228_암호문1;

import java.util.LinkedList;
import java.util.Scanner;

public class Solution {
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		for(int test_case = 1; test_case <= 10; test_case++)
		{
            int N = sc.nextInt();
            LinkedList<Integer> list = new LinkedList<>();
            for (int i = 0; i<N; i++){
                list.add(sc.nextInt());
            }
            int K = sc.nextInt();
            for (int i = 0; i<K; i++){
                sc.next();
                int idx = sc.nextInt();
                int count = sc.nextInt();
                for (int j = 0; j<count; j++){
                    list.add(idx++, sc.nextInt());
                }
            }
            
            System.out.print("#"+test_case);
            for (int i = 0; i<10; i++){
                System.out.print(" "+list.get(i));
            }
            System.out.println();
		}
	}
}