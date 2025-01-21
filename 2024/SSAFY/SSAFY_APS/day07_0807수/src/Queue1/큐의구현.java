package Queue1;

import java.util.Scanner;

public class 큐의구현 {
	
	// 배열 사이즈가 10이면 10번 삽입할 수 있다.
	static String[] queue = new String[10];
	static int front = -1;
	static int rear = -1;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		for (int i = 0; i<11; i++) {
			System.out.println("삽입할 문자열 입력 :");
			enQueue(sc.next());
		}
		
		System.out.println(size());
		
		while(!isEmpty()) {
			System.out.println(deQueue());
		}
	}
	
	// 공백 상태 확인
	static boolean isEmpty() {
		return front == rear;
	}
	
	// 포화상태 확인
	static boolean isFull() {
		// rear가 배열의 마지막 인덱스를 가리키면 포화상태
		return rear==queue.length-1;
	}
	
	// 삽입
	// 삽입 성공 여부를 반환하려면 boolean타입도 반환 가능
	static boolean enQueue(String item) {
		if(!isFull()) {
			queue[++rear]=item;
			return true;
		}
		return false;
	}
	
	
	//삭제
	static String deQueue() {
		if(!isEmpty()) {
			return queue[++front];
		}
		return null;
	}
	
	//조회
	static String Qpeek() {
		if(!isEmpty()) {
			return queue[front+1];
		}
		return null;
	}
	
	static int size() {
		return rear-front;
	}
	
}
