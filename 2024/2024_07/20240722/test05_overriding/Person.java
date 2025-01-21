package test05_overriding;

// extends 키워드를 명시하지 않으면
// 사실은 Object 클래스를 상속받고 있는 것임.
public class Person {
	String name;
	int age;
	
	//권장 : 기본생성자는 만들어주는 것이 좋다.
	public Person(){
		// super();가 생략되어있다.
		// Object 클래스의 생성자를 호출하고 있다.
	}
	
	// 부모 클래스에서 매개변수가 있는 생성자를 만들었더니
	// 경고가 뜸!
	public Person(String name, int age){
		this.name = name;
		this.age = age;
	}
	
	void eat() { 
		System.out.println("음식을 먹는다.");
	}
}
