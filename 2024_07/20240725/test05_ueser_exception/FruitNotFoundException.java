package test05_ueser_exception;

// CheckedException : Exception 상속
// - 클래스 , 객체생성
// - 생성자
public class FruitNotFoundException extends Exception{
	
	public FruitNotFoundException(String name) {
		super(name + "에 해당하는 과일이 없습니다.!");
	}
}
