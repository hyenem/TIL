package test01;

import com.google.gson.Gson;

public class Test2 {
	public static void main(String[] args) {
		Gson gson = new Gson();
		
		String str = "{\"name\":\"Luna\",\"age\":4}";
		
		// 문자열 -> 객체로 변환할 때
		// 자바스크립트는 따로 타입을 지정하지 않았지만,
		// 자바는 타입이 지정되어야 하므로, 타입에 대한 정보를 넣어줘야 함.
		Person obj = gson.fromJson(str, Person.class);
		
		System.out.println(str);
		System.out.println(obj);
		
	}
}
