package SWEA_2930_힙;

import java.util.Scanner;

public class Solution {
	static int[] arr = new int[(int)Math.pow(10, 5)+1];
	static int size;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case = 1; test_case<=T; test_case++) {
			int N = sc.nextInt();
			size = 0;
			
			System.out.print("#"+test_case);
			for(int i = 0; i<N; i++) {
				if(sc.nextInt()==1) {
					push(sc.nextInt());
				}
				else System.out.print(" "+pop());
			}
			System.out.println();
		}
	}
	
	static void swap(int i, int j) {
		int tmp = arr[i];
		arr[i]=arr[j];
		arr[j]=tmp;
	}
	static void push(int i) {
		arr[++size]=i;
		int ch = size;
		int p = ch/2;
		
		while(ch!=1 && arr[ch]>arr[p]) {
			swap(ch, p);
			ch = p;
			p = ch/2;
		}
	}
	
	static int pop() {
		if (size<=0) return -1;
		int popItem = arr[1];
		arr[1]=arr[size--];
		int p = 1;
		int ch = p*2;
		if(ch+1 <= size && arr[ch+1]>arr[ch]) ch++;
		
		while(ch<=size && arr[ch]>arr[p]) {
			swap(ch,p);
			p = ch;
			ch = p*2;
			if(ch+1 <= size && arr[ch+1]>arr[ch]) ch++;
		}
		return popItem;
	}
}
