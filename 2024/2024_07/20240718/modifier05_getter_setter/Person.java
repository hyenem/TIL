package modifier05_getter_setter;

public class Person {
    private String name;
    private int age;
    private boolean hungry;
    
    //객체지향 방식(캡술화) 설계를 한다면
    // 기본적으로 멤버 변수는 private(data), 보안을 위해서
    
    // 변수에 접근하는 통로는 메서드를 통해 만들고
    // 메서드는 public으로 열어놓는다.
    // 접근자와 설정자를 쓰면 좋은 점?
    // 값을 변경하거나, 가져오기 전에 사전에 보안 로직 추가 가능;
    
    // 접근자(getter) : 현재 객체의 멤버변수의 값을 반환해주는 함수.
    // 설정자(setter) : 현재 객ㅊ의 멤벼변수의 값을 변경 <= 새로운 값은 매개변수로 받는다.
    
    public int getAge() {
    	return age;
    }
    
    public void setAge(int age) {
    	if (age < 0) {
    		System.out.println("나이는 음수가 될 수 없습니다.");
    		return; // 함수를 여기서 종료하고, 나를 호출한 곳으로 돌아간다.
    	}
    	this.age = age;
    }

    // 우클릭, Source , generate getter setter
	public boolean isHungry() {
		return hungry;
	}

	public void setHungry(boolean hungry) {
		this.hungry = hungry;
	}
    
    
    
}
