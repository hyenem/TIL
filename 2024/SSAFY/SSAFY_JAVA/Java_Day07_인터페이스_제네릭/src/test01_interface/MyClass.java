package test01_interface;

// 인터페이스는 그 자체로 객체 생성이 안되므로
// 반드시 일반 클래스에 구현 되어야함!
// 구현 : 클래스 implements 인터페이스
// 상속 : 클래스 extends 상위클래스
//		 인터페이스 extends 인터페이스
public class MyClass implements Myinterface {
	// 1. 인터페이스의 모든 추상 메서드를 구현한다.
	// 2. 추상 클래스로 남는다.
	@Override
	public void method1() {
		System.out.println("method1");
	}

	@Override
	public void method2() {
		System.out.println("method2");
	}
	

}
