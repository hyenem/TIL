package Queue1;

import java.util.LinkedList;
import java.util.Queue;

public class 큐API {
	
	public static void main(String[] args) {
		Queue<Integer> queue = new LinkedList<>();
		
		// 삽입
		queue.add(1); // 추가될 수 없는 상황이 오면 예외를 발생
		queue.offer(1); // 추가될 수 없는 상황이 오면 false를 반환
		System.out.println(queue);
		
		// 삭제
		queue.remove(); // 삭제될 수 없으면 예외 발생
		queue.poll(); // 삭제될 수 없으면 return null;
		System.out.println(queue);
		
		queue.poll();
		
		// 조회
		queue.element(); // 예외 발생
		queue.peek(); // return null;
	}
	
}
