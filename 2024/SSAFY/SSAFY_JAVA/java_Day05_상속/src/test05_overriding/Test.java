package test05_overriding;

public class Test {
	public static void main(String[] args) {
		//설계도에서 생성자를 하나라도 프로그래머가 정의된다면
		// 컴파일러가 기본 생성자를 만들어주지 않는다.
		Person p = new Person();
		p.eat();
		
		
		Student st = new Student("Park", 28, "Java");
		// 절차(Stack 구조)
		// student 생성자 호출
		// person 생성자 호출
		// object 생성자 호출
		// object 관련 로직 생성 (heap의 가장 밑) -> pop
		// person 관련 로직 생성 (heap의 object 위) -> pop
		// student 관련 로직 생성 (heap의 person 위) -> pop
		// ** super가 항상 제일 위에 나와야함.
		
//		st.study();
		st.super.eat();
		st.eat();
		
	}
	
}
