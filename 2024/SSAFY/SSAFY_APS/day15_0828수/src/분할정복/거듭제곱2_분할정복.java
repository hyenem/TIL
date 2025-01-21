package 분할정복;

public class 거듭제곱2_분할정복 {
	public static void main(String[] args) {
		int C = 2;
		int N = 10;
		
		System.out.println(pow(C, N));
		System.out.println(pow2(C, N));
	}
	
	static int pow(int C, int N) {
		//기저조건
		if(N==1) return C;
		//재귀부분 : 짝수인 경우 / 홀수인 경우
		if((N & 1) == 0) {
			return pow(C, N/2) * pow(C,N/2);
		} else {
			return pow(C, N/2) * pow(C,N/2) * C;
		}
	}

	static int pow2(int C, int N) {
		//기저조건
		if(N==1) return C;
		//재귀부분 : 짝수인 경우 / 홀수인 경우
		int tmp = pow2(C, N/2);
		if((N & 1) == 0) {
			return tmp * tmp;
		} else {
			return tmp * tmp * C;
		}
	}
	
}
