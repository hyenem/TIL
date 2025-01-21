import java.util.Arrays;

public class Stack_스택의구현 {
	static String[] stack = new String[100];
	static int top=-1;
	
	static boolean isEmpty() {
		return top==-1;
	}
	
	static boolean isFull() {
		return top == stack.length-1;
	}
	
	static void push(String item) {
		if(isFull()) {
			System.out.println("스택이 가득 찼습니다.");
			return;
		}
		stack[++top]=item;
	}
	
	static String pop() {
		if(isEmpty()) {
			System.out.println("스택이 비어있습니다.");
			return null;
		}
		return stack[top--];
	}
	
	static String peek() {
		if(isEmpty()) {
			System.out.println("스택이 비어있습니다.");
			return null;
		}
		return stack[top];
	}
	
	public static void main(String[] args) {
		push("고양이");
		push("쥐");
		push("토끼");
		
		while(!isEmpty()) {
			String item = pop();
			System.out.println(item);
		}
		
		for(int i = 0; i<101; i++) {
			push(i+" ");
		}
	}
}
