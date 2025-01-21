package test02_try_catch;

public class ExceptionalTest1 {
	public static void main(String[] args) {
		
		int[] nums = {10};
		//try ... catch
		
		// 1. 예외가 발생했고 성공적으로 처리되었을 때(catch문을 만났을 때)
		//		 1 (2) 4 5
		// 2. 예외가 발생했는데 성공적으로 처리되지 못했을 때 (catch문을 못만났을 때)
		//		1 (2- 비정상적 종료)
		// 3. 예외가 발생하지 않았을 때
		//		1 2 3 5
		
		try {
			System.out.println("정상코드1");
			System.out.println(nums[2]); // (2)예외 발생 가능한 코드
			System.out.println("정상코드2");
		} catch (ArrayIndexOutOfBoundsException e) {
			// try 문에서 발생한 예외가 이 catch과 만날 수 있는 경우는
			// catch문에서 매개변수 타입으로 정한 예외와 일치하거나 그 자손일때
			// Exception 클래스 쓰면 전체를 다 커버할 수 있음
			System.out.println("배열의 인덱스 범위를 벗어났어요."); // (4) 예외처리 코드
		}
		System.out.println("프로그램 종료");//(5) 외부 정상 코드
	
//		try {
//			System.out.println("정상코드1");
//			System.out.println(nums[2]); // (2)예외 발생 가능한 코드
//			System.out.println("정상코드2");
//		} catch (ArithmeticException e) {
//			System.out.println("배열의 인덱스 범위를 벗어났어요."); // (4) 예외처리 코드
//		}
//		System.out.println("프로그램 종료");//(5) 외부 정상 코드
		
		try {
			System.out.println("정상코드1");
			System.out.println(nums[0]); // (2)예외 발생 가능한 코드
			System.out.println("정상코드2");
		} catch (ArithmeticException e) {
			System.out.println("배열의 인덱스 범위를 벗어났어요."); // (4) 예외처리 코드
		}
		System.out.println("프로그램 종료");//(5) 외부 정상 코드
	}
}
