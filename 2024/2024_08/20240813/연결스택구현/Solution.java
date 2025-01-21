package 연결스택구현;

import java.util.LinkedList;

class Stack<E>{
	LinkedList<E> stack = new LinkedList<E>();
	int top = -1;
	
	boolean isEmpty() {
		return top==-1;
	}
	
	void push(E element) {
		stack.add(++top, element);
	}
	
	E pop() {
		if(isEmpty()) return null;
		return stack.get(top--);
	}
	
	E peek() {
		if(isEmpty()) return null;
		return stack.get(top);
	}
}
public class Solution {
	public static void main(String[] args) {
		Stack<String> stack = new Stack<>();
		stack.push("첫번쨰");
		stack.push("두번쨰");
		stack.push("세번쨰");
		stack.push("네번쨰");
		
		System.out.println(stack.pop());
		System.out.println(stack.pop());
		System.out.println(stack.peek());
		System.out.println(stack.pop());
	}
}