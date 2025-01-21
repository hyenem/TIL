package modifier01_private;

public class Person {
	
	// 자기 자신만 접근 가능하다.
    private String name;
    private int age;
    
    // 멤버 메서드: 자기 자신..
    public void info() {
    	name = "Kim"; // 자기 자신의 것.
        System.out.printf("이름: %s, 나이: %d\n", name, age);
    }
}
