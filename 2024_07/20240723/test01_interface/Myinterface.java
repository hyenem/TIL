package test01_interface;

// 키워드 : interface => 인터페이스
public interface Myinterface {
	
	// 인터페이스에서는 변수 선언 앞에
	// public static final 이 생략되어 있는 것임.
	// => 인터페이스의 모든 변수는 사실 상수(static)
	// static => 인터페이스 이름으로 접근
	// 클래스에서도 static은 클래스 이름으로 접근
	// 인스턴ㅅ 이름으로 접근하고 싶지만...(권장하지 않음)
	
	/*public static final*/int MEMBER_1 = 10;
	public static final int MEMBER_2 = 20;
	
	// 모든 메서드가 추상메서드
	// 모든 메서드 선언 앞에 사실은 public abstract가 생략되어 있는 것임.
	void method1();
	public abstract void method2();
	
	default void method3() {
		System.out.println("default method!");
	}
	
	static void method4() {
		System.out.println("interface static method!!");
	}
}
