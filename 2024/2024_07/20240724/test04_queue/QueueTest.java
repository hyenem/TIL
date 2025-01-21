package test04_queue;

import java.util.LinkedList;
import java.util.Queue;

public class QueueTest {
	public static void main(String[] args) {
		// Queue
		// - FIFO
		// - Queue 인터페이스
		// - LinkedList를 구현체로 사용

		Queue<Integer> queue = new LinkedList<>();
		
		// 값을 추가
		queue.offer(1);
		queue.offer(2);
		queue.offer(3);
		
		//queue.offer(), queue.add() : 둘다 추가
		// 예외 처리에서 차이가 있을 수 있음
		
		// 값을 하나씩 꺼내기
		System.out.println(queue.poll());
		System.out.println(queue.poll());
		System.out.println(queue.poll());
		
		while(!queue.isEmpty()) {// 큐가 비어있지 않다면
			System.out.println(queue.poll());
		}
	}
}
