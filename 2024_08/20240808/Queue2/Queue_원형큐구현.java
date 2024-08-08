package Queue2;

import java.util.Arrays;

public class Queue_원형큐구현 {
	// 데이터를 3개 담을 수 있다. (배열 크기 -1)
	static int N = 4;
	static String[] queue = new String[N];
	static int front, rear;
//	static int size; //	사이즈 변수로 이용하면 덱을 한 칸 비워둘 필요 없음
	
	public static void main(String[] args) {
		enQueue("루나");
		enQueue("데이지");
		enQueue("맥스");
		enQueue("혜민");
		
		System.out.println(size());
		System.out.println(Arrays.toString(queue));
		
		deQueue();
		deQueue();
		deQueue();
		deQueue();
		enQueue("김혜민");
		deQueue();
		System.out.println(size());
		System.out.println(Arrays.toString(queue));
		
	}
	
	// 포화상태 확인
	static boolean isFull() {
		return (N+front-rear)%N==1;
	}
	
	static boolean isEmpty() {
		return front == rear;
	}
	
	static void enQueue(String data) {
		if(isFull()) {
			System.out.println("큐가 가득 찼습니다.");
			return;
		}
		
		rear = (rear+1)%N;
		queue[rear] = data;
//		size++;
	}
	
	//삭제
	static String deQueue() {
		if(isEmpty()) {
			System.out.println("큐가 비었습니다.");
			return null;
		}
		front = (front +1)%N;
//		size--;
		return queue[front];
	}
	
	//조회
	static String Qpeek() {
		if(isEmpty()) {
			System.out.println("큐가 비었습니다.");
			return null;
		}
		return queue[(front+1)%N];
	}
	
	// 데이터 개수
	static int size() {
		return (rear-front+N)%N;
	}
}
