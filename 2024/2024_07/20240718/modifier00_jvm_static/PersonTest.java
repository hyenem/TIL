package modifier00_jvm_static;

public class PersonTest {
    public static void main(String[] args) {
    	System.out.println(Person.pCount);
    	
    	Person p = new Person();
    	p.pCount = 200; // static 변수는 모든 인스턴스가 공유한다.
    	System.out.println(p.pCount); // 노란줄이 뜬다.
    	// 인스턴스를 통해서도 접근은 되지만, 클래스 이름으로 접근하는 것을 권장.
    	
    	
    }
}
