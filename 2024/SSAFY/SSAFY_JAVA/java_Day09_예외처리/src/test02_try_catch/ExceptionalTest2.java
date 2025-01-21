package test02_try_catch;

public class ExceptionalTest2 {
	public static void main(String[] args) {
		
		int[] nums = {10};
		//try ... catch ... catch
		// - catch 문은 여러개 올 수 있다.
		
		
		try {
			System.out.println("정상코드1");
			System.out.println(nums[2]); // ArrayIndexOutOfBouns..
			int i = 1/0; //Java에서는 숫자를 0으로 나누면 예외 발생 -> ArithmeticExcpetion
			System.out.println("정상코드2");
//		} catch (ArrayIndexOutOfBoundsException e || ArithmeticException e) {
		} catch (ArrayIndexOutOfBoundsException e) {
			System.out.println("배열의 인덱스 범위를 벗어났어요.");
		} catch (ArithmeticException e) {
			System.out.println("잘못된 계산 식입니다.");
		}
		System.out.println("프로그램 종료");
		
//		try {
//			System.out.println("정상코드1");
//			System.out.println(nums[2]); // ArrayIndexOutOfBouns..
//			int i = 1/0; //Java에서는 숫자를 0으로 나누면 예외 발생 -> ArithmeticExcpetion
//			System.out.println("정상코드2");
//		} catch (Exception e) {
//			System.out.println("배열의 인덱스 범위를 벗어났어요.");
//		} catch (ArithmeticException e) {
//			System.out.println("잘못된 계산 식입니다.");
//		}
//		System.out.println("프로그램 종료");
		// 예외도 다형성이 적영되므로
		// 상속관계에 있을 때에는 자손 먼저 처리해야함.
		
		
	}
}