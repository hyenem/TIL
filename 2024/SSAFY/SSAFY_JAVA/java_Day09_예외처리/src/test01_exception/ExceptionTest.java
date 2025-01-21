package test01_exception;

public class ExceptionTest {
	public static void main(String[] args) {
		
		// 1. Unchecked Exception.
		// - RuntimeException
		// - 저장하는 순간 => 이클립스에서 컴파일 수행
		// - 컴파일 시점에 확인하지 않았다.
		// - 컴파일 자체는 완료가 되었다.
		// - 일단 실행은 되었음.
		// - 컴파일러가 예외처리를 강제하지 않음.
		int[] nums = {10};
		System.out.println(nums[2]);
		
		// 2. Checked Exception
		// - Exception 의 자손 중에서 RuntimeException의 자손이 아닌 애들.
		// - 빨간 줄.
		// - 저장은 했는데 빨간 줄 => 컴파일 자체가 수행되지 않았다.
		// - 실행될 수 없다.
		// - 컴파일러가 예외처리를 강제하고 있다.
		// - 예외 처리 방법은???
//		Class.forName("Hello"); // 해당하는 이름의 클래스가 있다면, 메모리에 로드해라.
//		Thread.sleep(1000); // 프로그램을 일시 정지

	}
}
