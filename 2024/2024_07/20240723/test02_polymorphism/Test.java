package test02_polymorphism;

public class Test {
	public static void main(String[] args) {
		// 인터페이스와 다형성
		// 인터페이스 : 타입으로 사용 가능
		// 해당 인터페이스로 구현한 클래스로 만든 객체를
		// 해당 인터페이스로 참조할 수 있다.
		// 실제 객체의 행위가 일어난다.
		// 해당 인터페이스에 정의되어 있는 내용만 보인다.
		//
		
		AlarmSoutn galaxyPhone = new GalaxyPhone();
		AlarmSoutn iPhone = new IPhone();
		
//		galaxyPhone.
		
		galaxyPhone.playAlarm();
		iPhone.playAlarm();
		
		AlarmSoutn[] phones = {new GalaxyPhone(), new IPhone()};
			for(AlarmSoutn phone : phones) {
				phone.playAlarm();
			}

	}
}
