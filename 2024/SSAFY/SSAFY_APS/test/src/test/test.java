package test;

public class test {
	public static void main(String[] args) {
		float n=1;
		for(int i = 365; i>300; i--) {
			n*=i;
			n/=365;
		}
		
		System.out.println(n);
	}
}
