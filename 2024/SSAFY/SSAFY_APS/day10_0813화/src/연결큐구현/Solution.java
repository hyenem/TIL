package 연결큐구현;

import java.util.LinkedList;

class Queue<E>{
	LinkedList<E> queue = new LinkedList<>();
	int front = -1;
	int rear = -1;
	
	boolean isEmpty() {
		return front==rear;
	}
	
	void enQueue(E element) {
		queue.add(++rear, element);
	}
	
	E deQueue() {
		if(isEmpty()) return null;
		return queue.get(++front);
	}
	
	E peek() {
		if(isEmpty()) return null;
		return queue.get(front);
	}
}

public class Solution {
	public static void main(String[] args) {
		Queue<Integer> queue = new Queue<>();
		
		queue.enQueue(1);
		queue.enQueue(2);
		queue.enQueue(3);
		queue.enQueue(4);
		queue.enQueue(5);
		
		System.out.println(queue.deQueue());
		System.out.println(queue.deQueue());
		System.out.println(queue.deQueue());
		System.out.println(queue.peek());
		System.out.println(queue.deQueue());
		System.out.println(queue.deQueue());
		System.out.println(queue.deQueue());
		System.out.println(queue.deQueue());
		System.out.println(queue.deQueue());
	}
}