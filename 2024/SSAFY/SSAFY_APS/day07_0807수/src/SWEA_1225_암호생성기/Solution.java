package SWEA_1225_암호생성기;

import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

class Solution{
	public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
		for(int test_case = 1; test_case <= 10; test_case++){
            Queue<Integer> queue = new LinkedList<>();
            int N = sc.nextInt();
            for (int i = 0; i<8; i++){
                queue.offer(sc.nextInt());
            }
            
            int five = 1;
            int frontItem = queue.poll();
            while(frontItem>five){
                frontItem-=five++;
                if(five ==6) five =1;
                queue.offer(frontItem);
                frontItem = queue.poll();
            }
            queue.offer(0);
            
            System.out.print("#"+N+" ");
            for (int i = 0; i<8; i++){
                System.out.print(queue.poll()+" ");
            }
		}
	}
}