package test05_overriding;

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
	
	
	// 오버로딩
	// - 매개변수만 다르고 이름이 같은 메서드를 여러개 정의할 수 있다.
	
	// 부모에 eat()이라는 메서드가 있지만..
	// 그대로 쓰고 싶지 않고 조금 바꾸고 싶다.
	// 자식 클래스에서 메서드를 재정의할 수 있다.
	// 오버라이딩(재정의)
	// - 반드시 상속 관계에 있을 때 해당.
	// - 부모 클래스에 정의되어 있는 메서드를 자식 클래스에서 재정의한다.
	// - 메서드의 이름, 반환형, 매개변수가 동일해야한다.
	// - @Override 라는 어노테이션으로 좀 더 명확하게 나타낼 수 있다.
	//?? 오버라이딩 되기 전 메서드를 사용할 수는 없을까?
	//?? 오버라이딩의 메모리 사용 방법은?????
	@Override // 태그와 같은 것이다.
	void eat() {
		System.out.println("지식을 먹는다.");
	}
	
	// 오버라이드 아님 오버로드임
	// @Override //하면 오류남
	void eat(int a) {
		System.out.println(a+"만큼 먹는다.");
	}

}
