package class05;

public class PersonTest {
	public static void main(String[] args) {
		
		// 클래스를 가지고 객체를 생성
		// 클래스이름 객체의변수이름 = new 클래스이름()
		
		Person yang = new Person();
		Person hong = new Person();
		
		yang.name = "Yang";
		yang.age = 45;
		yang.hobby = "YouTube";
		
		yang.info();
		
		hong.name = "Hong";
		hong.age = 25;
		hong.hobby = "Golf";
		
		hong.info(); // 그 데이터와 연관된. 메서드.
		
//		info(yang.name, yang.age, yang.hobby);
//		info(hong.name, hong.age, hong.hobby);
		
		//함수를 이용할 때의 문제점은?
		
	}
	

}
