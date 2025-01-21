
public class String_atoi_itoa {
	public static void main(String[] args) {
		
		String strNum = "-52304";
		System.out.println(0+strNum);
		
		
		// 문자열 -> 정수
		int num = Integer.parseInt(strNum);
		System.out.println(0+num);
		
		int result = atoi(strNum);
		System.out.println(result);
		
		
		// 정수 -> 문자열
		
		int intVar = 324;
		String intStr = String.valueOf(intVar);
		System.out.println(intStr);
		
		System.out.println(itoa(1234));

	}
	
	static int atoi(String str) {
		int N = str.length();
		int num = 0;
		if (str.charAt(0)=='-') {
			for (int i = 1; i<N; i++) {
				char c = str.charAt(i);
				if('0'<=c && c<='9') {
					num = (num*10)+c-'0';
				} else {
					return -99999999;
				}
			}
			return num*(-1);
		} else {
			for (int i = 0; i<N; i++) {
				char c = str.charAt(i);
				if('0'<=c && c<='9') {
					num = (num*10)+c-'0';
				} else {
					return -99999999;
				}
			}
			return num;
		}
	}
	
	static String itoa(int num) {
		String str = "";
		while (num!=0) {
			str = (num%10)+str;
			num /= 10;
		}
		return str;
	}
}
