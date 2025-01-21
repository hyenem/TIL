package test02_try_catch;

public class ExceptionalTest5 {
	public static void main(String[] args) {
		try {
			System.out.println("정상코드1");
			System.out.println(nums[2]); // ArrayIndexOutOfBouns..
			int i = 1/0; //Java에서는 숫자를 0으로 나누면 예외 발생 -> ArithmeticExcpetion
			System.out.println("정상코드2");
		} catch (ArrayIndexOutOfBoundsException e) {
			System.out.println(e.getMessage());
			e.printStackTrace();
			// 모든 예외 메세지를 확인할 수 있으면서도
			// 프로그램은 정상종료되었다.
			System.out.println("배열의 인덱스 범위를 벗어났어요.");
		}
	}
}
