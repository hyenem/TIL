package class06;

public class PersonTest {
	public static void main(String[] args) {
		
		// 메서드의 호출: 1. 객체를 생성, 2. .연산자 사용
		Person p = new Person();
		
		// 묵시적 형변환 가능
		p.study((byte)2);
		p.study((short)10);
		p.study('A');
		p.study(10);
		
		// 묵시적 형 변환으로 안된다면?
		// => 메서드 오버로딩으로 설명할 수 있다.
		p.study(10L);
		p.study(10.3f);
		p.study(10.5);
		p.study("10");
	}
	

}
