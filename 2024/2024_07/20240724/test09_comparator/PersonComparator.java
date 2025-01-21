package test09_comparator;

import java.util.Comparator;

// 2. Comparator를 구현한다.
//		-제네릭 : 비교대상의 타입을 적어준다
public class PersonComparator implements Comparator<Person>{

	@Override
	public int compare(Person o1, Person o2) {
		return o1.age - o2.age;//순서대로 빼면 오름차순
				//거꾸로 빼면 내림차순
	}

}
