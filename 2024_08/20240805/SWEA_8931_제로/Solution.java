package SWEA_8931_제로;

import java.util.Scanner;
import java.io.FileInputStream;
import java.util.List;
import java.util.ArrayList;


class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		
		for(int test_case = 1; test_case <= T; test_case++)
		{
			int K = sc.nextInt();
			Stack stack = new Stack();
			for(int i = 0; i<K; i++){
				int res = sc.nextInt();
				if(res==0) stack.pop();
				else stack.push(res);
			}
			
			int sum=0;
			while(!stack.isEmpty()){
				sum+=stack.pop();
			}
			System.out.println("#"+test_case+" "+sum);
		}
	}
}

class Stack{
    static List<Integer> stack = new ArrayList<Integer>();
    static int top =-1;
    
    void push(int i){
        stack.add(i);
        top++;
	}
    
    int pop(){
        int result = stack.get(top);
        stack.remove(top--);
   		return result;
    }
    
    int peek(){
        return stack.get(top);
    }
    
    boolean isEmpty(){
        return top==-1;
    }
}
