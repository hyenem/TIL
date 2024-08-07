package class08;

class Dog {
	
	String name;
	int age;
	
	// 생성자에도 매개변수가 올 수 있다.
	
	// 주로 맴버필드를 초기화하는데 사용한다.
	// 프로그래머가 생성자를 하나라도 만든다면,
	// 컴파일러는 기본 생성자를 추가하지 않는다.
	// 기본 생성자는 웬만하면 만드는게 좋다.(상속)
	Dog(){
	}
	
	
	//생성자 오버로딩
	Dog(String name, int age){
		//this.를 통해 구별한다.
		//this : 객체(인스턴스) 나자신을 가리키는 참조값 != 설계도 아님
		this.name = name;
		this.age = age;
	}
	
	Dog(String name){
//		this.name = name;
//		this.age = 5;
		this(name, 5); //내가 이미 가지고 있는 생성자를 호출
		// 제양사항: 반드시 생성자 본문에서 첫줄에 위치
	}
	
	Dog(int a){
		this("무명", age);
	}
	
	Dog eat() {
		System.out.println("사료를 먹고....");
		return this;
	}
	
	void drink() {
		System.out.println("물을 마신다.");
	}
}
