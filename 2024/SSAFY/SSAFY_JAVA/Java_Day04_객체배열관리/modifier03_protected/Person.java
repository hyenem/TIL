package modifier03_protected;

public class Person {
	
	// protected : 같은 패키지에 있다면 ok
	//			: 다른 패키지에 있다면 기본적으로는 안되지만
	//			  다른 패키지에 있는 클래스가 상속하고 있다면 접근 가능
    protected String name;
    protected int age;
    
    public void info() {
        System.out.printf("이름: %s, 나이: %d\n", name, age);
    }
}
