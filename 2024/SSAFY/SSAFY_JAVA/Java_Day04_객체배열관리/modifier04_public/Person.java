package modifier04_public;

public class Person {
	
	// public : 모든 위치에서 접근 가능.
    public String name;
    public int age;
    
    public void info() {
        System.out.printf("이름: %s, 나이: %d\n", name, age);
    }
}
