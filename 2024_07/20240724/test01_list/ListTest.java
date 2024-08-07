package test01_list;

import java.util.ArrayList;
import java.util.List;
import java.util.jar.Attributes.Name;

public class ListTest {
	
	public static void main(String[] args) {
		// List
		// - 순서도 있고, 중복도 허용
		
		List<String> names = new ArrayList<String>();
		
		// 원소 추가
		names.add("i");
		names.add("e");
		names.add("o");
		names.add("u");
		
		System.out.println(names);
		
		// 리스트가 비어있는지 채크
		System.out.println(names.isEmpty());
		
		// 수정
		names.set(0, "change");
		System.out.println(names);
		
		//조회
		System.out.println(names.get(3));
		
		// 순회
		for(String name : names) {
			System.out.println(name);
		}
		
		// 인덱스를 이용한 삭제
		names.remove(0);
		System.out.println(names);
		
		//값을 이용한 삭제(제일 앞의 값만 삭제됨)
		names.remove("u");
		System.out.println(names);
		
		// 전부 삭제
		names.clear();
		System.out.println(names);
		System.out.println(names.isEmpty());
		
		// 삭제할 때 주의할 점
		// - 중복된 값이 있을 때
		names.add("e");
		names.add("e");
		names.add("u");
		
		System.out.println(names);
		
		// "e"를 다 지우고 싶다.
		// => for 문을 돌면서 순회를 하면서, 일치하는 애들은 전부 지어버린다
		// 하나 삭제하면 인덱스도 변경되고 사이즈도 변경되어버림...
//		for(int i =0; i<names.size(); i++) {
//			if (names.get(i).equals("e")) {
//				names.remove(i);
//			}
//		}
//		System.out.println(names);
		for(int i =names.size()-1; i>=0; i--) {
			if (names.get(i).equals("e")) {
				names.remove(i);
			}
		}
		System.out.println(names);
		
		
		
	}

}
