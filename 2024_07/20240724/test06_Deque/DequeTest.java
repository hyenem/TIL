package test06_Deque;

import java.util.ArrayDeque;
import java.util.Deque;

public class DequeTest {
	public static void main(String[] args) {
		// Deque
		// - Deque : 인터페이스
		// - 구현체 : ArrayDeque, LinkedList
		// - 양쪽 끝에서 자유롭게 자료의 추가, 삭제 가능
		
		// 객체배열관리 실습 : array <= 실제로 배열을 가지고 리스트를 만들어본 것
		// 중간에 삭제, 중간에 추가,,,, 
		// 중간에서 삭제, 추가가 빈번하게 일어날 때 불리함.
		// array : 조회는 가장 빠르다.
		
		// LinkedList : 조회는 느리다. 삭제&추가는 빠르다
		
		Deque<String> deque = new ArrayDeque<>();
		
		deque.addFirst("alice");
		deque.addFirst("luna");
		deque.addLast("max");
		deque.addFirst("daisy");
		
		System.out.println(deque);
		
		System.out.println(deque.removeLast());
		System.out.println(deque.removeLast());
		System.out.println(deque.removeFirst());
		System.out.println(deque.removeFirst());
	}
}
