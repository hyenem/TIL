package Test02;

import java.util.Arrays;import com.google.gson.Gson;

public class Test1 {
	public static void main(String[] args) {
		
		// 객체 배열
		Person[] arr = new Person[3];
		arr[0] = new Person("Luna", 3);
		arr[1] = new Person("Max", 4);
		arr[2] = new Person("Daisy", 2);
		
		System.out.println(Arrays.toString(arr));
		
		//객체 배열 -> JSON으로 만들기
		
		Gson gson = new Gson();
		String arrStr = gson.toJson(arr);
		System.out.println(arrStr);
	}
}
