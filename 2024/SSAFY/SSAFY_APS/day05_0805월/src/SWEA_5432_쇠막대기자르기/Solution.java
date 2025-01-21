package SWEA_5432_쇠막대기자르기;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Stack{
	List<Character> stack = new ArrayList<Character>();
	int top = -1;
	
	void push(char c) {
		stack.add(c);
		top++;
	}
	
	char pop() {
		char result = stack.get(top);
		stack.remove(top--);
		return result;
	}
}

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case = 1; test_case<T+1; test_case++) {
			int ans = 0;
			Stack stack = new Stack();
			String str = sc.next();
			for (int i = 0; i<str.length(); i++) {
				if(str.charAt(i)=='(') stack.push('(');
				else {
					if(str.charAt(i-1)=='(') ans+=stack.top;
					else ans++;
					stack.pop();
				}
			}
			System.out.println("#"+test_case+" "+ans);
		}
	}
}