package modifier00_jvm_static;

public class Person {
	
	// static 변수
	// - 클래스(설계도)에 이미 들어있는 변수.
	// - 인스턴스 생성과 무관, 이전에 이미 있다.
	// - 설계도가 메서드 영역에 로딩되는 시점에.
	// - 설계도에 들어있는 것이므로,
	//	 이 설계도로 만드는 모든 인스턴스에 공유된다.
	// - 클래스이름.static변수 : 클래스 이름으로 바로 접근 가능하다.
	static int pCount =100;
	
	// 아래의 변수들은?
	// - 인스턴스 변수, 멤버 변수
	// - non static
	// - 실제 인스턴스가 생성될 때 힙 영역에 만들어짐
	// - 객체 생성 후에, 해당 객체의 이름으로만 접근 가능
	// - this : 각각의 인스턴스가 자기 자신을 가리키는 참조
    String name;
    int age;
    String hobby;
    
    static {
    	pCount = 1000;
    }
    
    public static void main(String[] args) {
//    	name = "Kim"; // static에서는 non-static 접근 불가.
    }
    
    public void info() {
    	pCount = 300; // non-static에서는 static 접근 가능
//    	name = "Kim";
    }
}
