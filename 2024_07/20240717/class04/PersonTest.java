package class04;

public class PersonTest {
	public static void main(String[] args) {
		
		// 클래스를 가지고 객체를 생성
		// 클래스이름 객체의변수이름 = new 클래스이름()
		
		Person yang = new Person();
		Person hong = new Person();
		
		yang.name = "Yang";
		yang.age = 45;
		yang.hobby = "YouTube";
		
		hong.name = "Hong";
		hong.age = 25;
		hong.hobby = "Golf";
		
		info(yang.name, yang.age, yang.hobby);
		info(hong.name, hong.age, hong.hobby);
		
		//함수를 이용할 때의 문제점은?
		
	}
	
	public static void info(String name, int age, String hobby) {
		System.out.println("이름은 "+name+"이고, 나이는 "+age+"세입니다.");
		System.out.println("취미는 "+hobby+"입니다.");
	}
}
