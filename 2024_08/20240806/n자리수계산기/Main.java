package n자리수계산기;

import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

public class Main {
	public static void main(String[] args) {
		System.out.println(evaluate("958*(75+62)-581*2"));
	}
    static Map<Character, Integer> map = new HashMap<>();
    static{
        map.put('+',1);
        map.put('-',1);
        map.put('*',2);
        map.put('/',2);
        map.put('(',0);
    }
	static String postfix(String str) {
		Stack<Character> stack = new Stack<>();
		String result = "";
		for (int i = 0; i<str.length(); i++) {
			char c = str.charAt(i);
			if(c>='0'&& c<='9') result+=c;
			else {
				result+=' ';
				if(c=='(') stack.push(c);
	            else if(c==')'){
	                char popItem = stack.pop();
	                while(popItem!='('){
	                    result+=popItem;
	                    popItem = stack.pop();
	                }
	            } else{
	                while(!stack.isEmpty() && map.get(stack.peek())>=map.get(c)){
	                    char popItem = stack.pop();
	                    if(popItem=='(') break;
	                    result+=popItem;
	                }
	                stack.push(c);
	            }
			}
		}
        while(!stack.isEmpty()){
            result+=stack.pop();
        }
        return result;
	}
	
	static int evaluate(String str) {
		String newStr = postfix(str);
		System.out.println(newStr);
		Stack<Integer> stack = new Stack<>();
		int i = 0;
		while(i!=newStr.length()) {
			char c = newStr.charAt(i);
			if (c==' ') {
				i++;
				continue;
			}
			else if(c<='9' && c>='0') {
				int res = c-'0';
				i++;
				while(i!=newStr.length()&&newStr.charAt(i)<='9'&&newStr.charAt(i)>='0') {
					res*=10;
					res+=newStr.charAt(i)-'0';
					i++;
				}
				stack.push(res);
			}else {
				i++;
                int num1 = stack.pop();
                int num2 = stack.pop();
                if(c=='+') stack.push(num1+num2);
                else if (c=='-') stack.push(num2-num1);
                else if (c=='*') stack.push(num1*num2);
                else stack.push(num2/num1);
			}
		}
		return stack.pop();
	}
}

