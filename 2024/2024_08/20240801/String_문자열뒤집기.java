import java.util.Arrays;

public class String_문자열뒤집기 {
	public static void main(String[] args) {
		
		//java에서는 문자열 읽기는 가능, 특정 위치에 문자 쓰기x
		String str = new String("algorithm");
		
		char[] charArr = new char[str.length()];
		for (int i = 0; i< str.length(); i++) {
			charArr[i]= str.charAt(i);
		}
		
		System.out.println(Arrays.toString(charArr));
		
		//1. 새로운 배열을 만들어서 뒤집기
		char[] nextArr = new char[charArr.length];
		
		for (int i = 0; i<charArr.length; i++) {
			nextArr[charArr.length-1-i]=charArr[i];
		}
		
		System.out.println(Arrays.toString(nextArr));
		
		//2. 원본 배열에서 swap
		char[] charArr2 = str.toCharArray();
		System.out.println(Arrays.toString(charArr2));
		
		String nextStr = "";
		
		for (int i = 0; i<charArr2.length; i++) {
			nextStr += charArr2[i];
		}
		//문자열 더하는 과정 반복마다 새로운 문자열 객체 생성
		
		System.out.println(nextStr);
		
		int N = charArr2.length;
		for(int i =0; i<N/2; i++) {
			char tmp = charArr2[i];
			charArr2[i]=charArr2[N-1-i];
			charArr2[N-1-i]=tmp;
		}
		
		System.out.println(charArr2);
	}
}
