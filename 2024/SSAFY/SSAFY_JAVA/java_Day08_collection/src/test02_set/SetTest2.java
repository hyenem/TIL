package test02_set;

import java.util.HashSet;
import java.util.Set;

public class SetTest2 {
	public static void main(String[] args) {
		Set<Person> set = new HashSet<Person>();
		
		set.add(new Person("luna", 3));
		set.add(new Person("luna", 3));

		// set에는 한 사람? 아니면 두 사람?
		// set이 같다고 판단하는 기준 : hashcode 가 같으면서 equals값도 같아야함.
		System.out.println(set);
		
		
		//
		
	}
}
