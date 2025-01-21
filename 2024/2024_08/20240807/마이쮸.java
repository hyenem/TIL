package Queue1;

import java.util.LinkedList;
import java.util.Queue;

class Person {
	int no;
	int cnt;
	
	public Person(int no, int cnt) {
		super();
		this.no = no;
		this.cnt = cnt;
	}
	
}

public class 마이쮸 {
	public static void main(String[] args) {
		Queue<Person> queue = new LinkedList<>();
		int N = 20;
		
		int pNum = 1;

		queue.add(new Person(pNum++, 1));
		while(N>0) {
			Person nowperson = queue.poll();
			N-=nowperson.cnt++;
			if(N<=0) {
				System.out.println(nowperson.no+"번이 마지막 마이쮸를 가져갔습니다.");
				break;
			}
			queue.add(nowperson);
			queue.add(new Person(pNum++, 1));
		}
	}
	
}
