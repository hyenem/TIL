package test09_comparator;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

public class SortTest {
	public static void main(String[] args) {
		// 정렬
		// - 순서가 있는 자료구조 : List
		
		List<Person> person = new ArrayList<>();
		
		person.add(new Person("daisy",3));
		person.add(new Person("luna",2));
		person.add(new Person("alice",5));
		
		System.out.println(person);
		
		// 정렬
		// Collections 유틸리티 클래스의
		// sort() 메서드 사용
		
		Collections.sort(person, new PersonComparator()); // 숫자 또는 문자의 오름차순으로 정렬(한글도 됨)
		// 사용자 정의클래스를 사용한 리스크는 기본적으로 정렬할 수 업승ㅁ
		// Comparable 인터페이스 구현 or Comparator 클래스를 정의(Comparator 인텊이스를 구현해서)
		System.out.println(person);
		// 만약 숫자의 리스트였다면 수의 크기의 오름차순으로 정렬
	}
}
