import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

public class Stack2_계산기 {
	public static void main(String[] args) {
		int result = evaluate("(6+5*(2-8)/2)");
		System.out.println(result);
	}
	
	static Map<Character, Integer> map = new HashMap<>();
	static {
		map.put('+', 1);
		map.put('-', 1);
		map.put('*', 2);
		map.put('/', 2);
		map.put('(', 0);
	}
	
	static String infixToPostfix(String infix) {
		
		
		String postfix = "";
		Stack<Character> stack = new Stack<>();
		
		for(int i = 0; i<infix.length(); i++) {
			char c = infix.charAt(i);
			if(c<='9' && c>='0') {
				postfix += c;
			} else if (c=='(') {
				stack.push(c);
			} else if (c==')') {
				char popItem = stack.pop();
				while(popItem!='(') {
					postfix += popItem;
					popItem = stack.pop();
				}
			} else {
				while(!stack.isEmpty() && map.get(stack.peek())>=map.get(c)) {
					char popItem = stack.pop();
					if(popItem =='(') break;
					else postfix+=popItem;
				}
				stack.push(c);
			}
		}
		while(!stack.isEmpty()) {
			postfix += stack.pop();
		}
		return postfix;
	}
	
	static int evalPostfix(String postfix) {
		
		Stack<Integer> stack = new Stack<>();
		
		for(int i =0; i<postfix.length();i++){
			char c = postfix.charAt(i);
			
			if(c>='0' && c<='9') {
				stack.push(c-'0');
			} else {
				int num1 = stack.pop();
				int num2 = stack.pop();
				
				if(c=='+') {
					stack.push(num2+num1);
				} else if(c=='-') {
					stack.push(num2-num1);
				} else if (c=='*') {
					stack.push(num2*num1);
				} else {
					stack.push(num2/num1);
				}
			}
		}
		return stack.pop();
	}
	
	static int evaluate(String expression) {
		String postfix = infixToPostfix(expression);
		return evalPostfix(postfix);
	}
}
