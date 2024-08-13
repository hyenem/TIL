package doubly;

class Node{
	String data;
	Node prev;
	Node next;
}

class DoublyLinkedList{
	Node head;
	Node tail;
	int size;
	
	public DoublyLinkedList() {
		head = new Node();
		tail = new Node();
		
		head.next = tail;
		tail.prev = head;
	}
	
	//삽입
	void addDat(int i, String data) {
		// 0이면 제일 앞에 삽입
		// size면 제일 뒤에 삽입
		if(i<0 || i>size) {
			System.out.println("삽입할 수 없는 범위입니다.");
			return;
		}
		size++;
		
		Node newNode = new Node();
		newNode.data = data;
		
		Node curr = head;
		for(int k = 0; k<i; k++) {
			curr = curr.next;
		}
		newNode.prev = curr;
		newNode.next = curr.next;
		curr.next.prev = newNode;
		curr.next = newNode;
	}

	// 삭제
	void removeData(int i) {
		//0이면 제일 앞 데이터 삭제
		// size-1이면 제일 뒤 데이터 삭제
		if(i<0 || i>=size) {
			System.out.println("삭제할 수 없는 위치입니다.");
			return;
		}
		size--;
		
		//rmNode는 지역변수이므로 메서드 리턴과 동시에 접근 불가
		Node rmNode = head;
		for(int k = 0; k <= i; k++) {
			rmNode = rmNode.next;
		}
		rmNode.prev.next = rmNode.next;
		rmNode.next.prev = rmNode.prev;
	}
	
	void printReverseAll() {
		Node curr = tail.prev;
		String str = "";
		while(curr!=head) {
			str = "<-"+curr.data +str;
			curr = curr.prev;
		}
		System.out.println(str);
	}
}

public class LinkedList_이중연결리스트 {
	public static void main(String[] args) {
		DoublyLinkedList list = new DoublyLinkedList();
		
		list.addDat(0, "1");
		list.addDat(0, "2");
		list.addDat(0, "3");
		list.addDat(0, "4");
		list.addDat(0, "5");
		list.addDat(0, "6");
		list.printReverseAll();
		
		list.removeData(1);
		list.printReverseAll();
	}
}
