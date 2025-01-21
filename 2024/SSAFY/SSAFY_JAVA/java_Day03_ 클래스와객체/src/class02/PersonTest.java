package class02;

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
		
	}
}
