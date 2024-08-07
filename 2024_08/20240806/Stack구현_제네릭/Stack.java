package Stack구현_제네릭;

import java.util.ArrayList;
import java.util.List;

class Stack<E>{
    List<E> stack = new ArrayList<E>();
    int top =-1;
    
    void push(E i){
        stack.add(i);
        top++;
	}
    
    E pop(){
        E result = stack.get(top);
        stack.remove(top--);
   		return result;
    }
    
    E peek(){
        return stack.get(top);
    }
    
    boolean isEmpty(){
        return top==-1;
    }
}