package QUEUE구현;

import java.util.LinkedList;
import java.util.List;

class Queue<E>{
	List<E> queue = new LinkedList<>();
	int front = -1;
	int rear = -1;
	
	boolean isEmpty() {
		return front==rear;
	}
	
	void enQueue(E item) {
		queue.add(item);
		rear++;
	}
	
	E deQueue() {
		if(!isEmpty()) {
			E res = queue.get(++front);
			return res;
		}
		return null;
	}
	
	E Qpeek() {
		if(!isEmpty()) {
			return queue.get(front+1);
		}
		return null;
	}
	
	int size() {
		return rear-front;
	}
	
	
}

public class Solution {
	public static void main(String[] args) {
		Queue<Character> queue = new Queue<>();
		queue.enQueue('h');
		queue.enQueue('y');
		queue.enQueue('e');
		queue.enQueue('n');
		queue.enQueue('e');
		queue.enQueue('m');
		System.out.println(queue.deQueue());
		System.out.println(queue.deQueue());
		System.out.println(queue.deQueue());
		System.out.println(queue.deQueue());
		System.out.println(queue.deQueue());
		System.out.println(queue.deQueue());
	}
}