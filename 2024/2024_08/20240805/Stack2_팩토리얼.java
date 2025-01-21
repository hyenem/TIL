
public class Stack2_팩토리얼 {
	public static void main(String[] args) {
		System.out.println(factorial1(10));
		System.out.println(factorial2(10));
	}
	
	static int factorial1(int N) {
		int result = 1;
		for (int i = 1; i<=N; i++) {
			result*=i;
		}
		return result;
	}
	
	static int factorial2(int N) {
		if(N==0) return 1;
		return factorial2(N-1)*N;
	}
}
