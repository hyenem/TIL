package test03_throws;

public class ThrowTest2 {
	// UncheckedException과 throws
	// - 컴파일러가 예외처리를 강제하지 않음.
	// - UnchechedException에게 throws는 아.무.런 의미가 없다.
	// 의미를 찾으려고 하지 말 것
	// - throws: 이번만 한 번 봐줄게
	//	UnchechedException : 예외를 처리 하든 말든 원래 봐주는 애
	// 예외가 실행중에 발생하면, 프로그래머의 자율에 맡김.
	
	public static void main(String[] args) {
		method1();
	}

	private static void method1() {
		try {
			method2();			
		} catch(ArithmeticException e) {
			System.out.println("method1에서 처리합니다.");
		}
	}

	private static void method2() {
		int i = 1/0; //ArithmeticException(UncheckedException)이 발생할 수 있음.
	}
}
