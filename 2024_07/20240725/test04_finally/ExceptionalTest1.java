package test04_finally;

public class ExceptionalTest1 {
	public static void main(String[] args) {
		
		
		// try ... catch ... finally
		int[] nums = {10};
		
		// try ... catch ... finally
		// 1. 정상적으로 실행되는 경우 : 1245
		// 2. 예외 발생 & 처리가 되는 경우 : 1345
		// 3. 예외 발생 & 미처리 되는 경우 : 14비정상적종료
		// 4. 정상 실행 & try문에 return(메서드 종료)이 있는 경우 : 124
		// 5. 예외 발생 & 처리 & catch문에 return이 있는 경우 : 134
		
		
		try {
			System.out.println("1");
			System.out.println(nums[2]); 
//			int i = 1/0;
			System.out.println("2");
//			return; // 메서드를 종료
		} catch (ArrayIndexOutOfBoundsException e) {
			System.out.println("3"); 
			return;
		} finally {
			System.out.println("4");
		}
		System.out.println("5");
	}
}
