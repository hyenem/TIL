package Heap;

public class Tree_최소힙 {
	static int[] heap = new int[100];
	static int heapSize = 0;
	
	public static void main(String[] args) {
		heapPush(20);
	}
	
	static void swap(int i, int j) {
		int tmp = heap[i];
		heap[i]=heap[j];
		heap[j]=tmp;
	}
	
	static void heapPush(int data) {
		// 1. 완전이진트리 마지막에 data 추가
		heap[++heapSize] = data;
		
		int p = heapSize/2;
		int ch = heapSize;
		while(ch!=1 && heap[p]>heap[ch]) {
			// 2. 부모와 비교해서 자식이 더 작으면 swap
			swap(p,ch);
			
			// 3. swap 이후의 인덱스 갱신
			ch = p;
			p = ch/2;
		}
	}
	static int heapPop() {
		// 1. 루트에 있는 데이터 저장
		int popItem = heap[1];
		
		// 2. 마지막 노드를 루트로 옮긴다.
		heap[1] = heap[heapSize--];
		
		// 3. 자식과 부모를 비교하여 swap 반복
		// 자식이 부모보다 작으면 swap
		// 둘 이상이면 더 작은 자식과 swap
		int p = 1;
		int ch = p*2;
		if(ch+1<=heapSize && heap[ch]>heap[ch+1]) {
			ch++;
		}
		
		while(ch<=heapSize && heap[ch]<heap[p]) {
			swap(p,ch);
			
			//4. swap 이후 index 갱신
			p = ch;
			ch = p*2;
			if(ch+1<=heapSize && heap[ch]>heap[ch+1]) {
				ch++;
			}
		}
		return popItem;
	}
}
