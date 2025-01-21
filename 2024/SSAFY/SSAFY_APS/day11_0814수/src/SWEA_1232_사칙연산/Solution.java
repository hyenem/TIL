package SWEA_1232_사칙연산;

import java.util.Arrays;
import java.util.Scanner;
import java.util.Stack;

public class Solution {
	static char[] data;
	static int[][] child;
	static int N;
	static Stack<Float> stack;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		for(int test_case=1; test_case<=10; test_case++) {
			N = sc.nextInt();
			data = new char[N+1];
			child = new int[2][N+1];
			for(int i = 0; i<N; i++) {
				int nowidx = sc.nextInt();
				String nowdata = sc.next();
				if(nowdata.length()==1) data[nowidx]=nowdata.charAt(0);
				else data[nowidx] = (char)(Integer.parseInt(nowdata)+'0');
				String str = sc.nextLine();
				int count = 0;
				int tmpint = 0;
				if(str.length()==0) continue;
				for(int j = 1; j<str.length(); j++) {
					if(str.charAt(j)==' ') {
						child[count][nowidx]=tmpint;
						count++;
						tmpint=0;
					} else {
						tmpint = tmpint*10 + str.charAt(j)-'0';
						if(j==str.length()-1) {
							child[count][nowidx]=tmpint;
							count++;
						}
					}
				}
			}
			stack = new Stack();
			postorder(1);
			System.out.print("#"+test_case+" ");
			System.out.printf("%.0f", stack.pop());
			System.out.println();
		}
	}
	
	static void postorder(int root) {
		if(root>N || root==0) return;
		postorder(child[0][root]);
		postorder(child[1][root]);
		if(data[root]=='+') {
			float num1 = stack.pop();
			float num2 = stack.pop();
			stack.push(num2+num1);
		} else if (data[root]=='-') {
			float num1 = stack.pop();
			float num2 = stack.pop();
			stack.push(num2-num1);
		} else if (data[root]=='*') {
			float num1 = stack.pop();
			float num2 = stack.pop();
			stack.push(num2*num1);
		} else if (data[root]=='/') {
			float num1 = stack.pop();
			float num2 = stack.pop();
			stack.push(num2/num1);
		} else {
			stack.push((float)(data[root]-'0'));
		}
	}
}