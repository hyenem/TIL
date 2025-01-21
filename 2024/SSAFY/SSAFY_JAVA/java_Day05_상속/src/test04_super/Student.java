package test04_super;

// 상속을 할 때는 extends 키워드를 사용.
public class Student extends Person {

	String major;
	
	//아무런 생성자도 선언하지 않은 상태
	// => 컴파일러가 기본생성자 Student(){}를 만들어 둠
	// => Student(){} 안에 super();가 생략되어있음
	// => super()가 정의 되지 않으면(다른 생성자를 추가해서 기본 생성자를 없애면) 에러가 남.
	
	//빈 공간에서 ctrl + spacebar
	public Student() {
//		super(); // 생성자 내부에는 기본적으로 super();가 생략됨
		// 프로그래머가 명시적으로 super()을 호출하지 않아도 기본적으로 호출함.
		// 프로그래머가 명시적으로 super()을 호출하면 기본적으로 super()을 호출하지 않음.
	}
	
	// 마우스 우클릭 -> Source -> Generate Constructor ..
	public Student(String major) {
		super(); // 자동으로, 생략되어있는 super을 넣어준다
		this.major = major;
	}
	
	public Student(String name, int age, String major) {
//		super(); // super은 하나만 쓸 수 있다.
		super(name, age);
		this.major = major;
		// super가 무조건 먼저! object까지 가야지 instance가 생성됨.
	}
	
	
	void study() {
		super.eat();
		System.out.println("공부를 합니다.");
	}
	
	

}
