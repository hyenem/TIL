package test03_inheritance;

// 상속을 할 때는 extends 키워드를 사용.
public class Student extends Person {

	String major;
	
	void study() {
		System.out.println("공부를 합니다.");
	}
}
