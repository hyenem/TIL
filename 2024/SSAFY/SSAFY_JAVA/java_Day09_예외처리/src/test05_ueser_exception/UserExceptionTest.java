package test05_ueser_exception;

public class UserExceptionTest {
	public static void main(String[] args) {
//		try {
//			method1();
//		} catch (FruitNotFoundException e) {
//			// TODO Auto-generated catch block
//			e.printStackTrace();
//		}
		
		method2();
	}

	private static void method2() {
		throw new FruitNotFoundRuntimeException("귤");
		
	}

	private static void method1() throws FruitNotFoundException{
		// 이 메서드에서 예외가 발생
		// ....
		
		// 예외 직접 발생시킬 때는 throw 키워드 사용.
		throw new FruitNotFoundException("사과");
	}
}
