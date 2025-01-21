package com.ssafy.aop;

public class Test {
	public static void main(String[] args) {
		Programmer p = new Programmer(); //스프링 컨테이너가 빈 등록
		
		PersonProxy px = new PersonProxy();
		px.setPerson(p);
		
		px.coding();
	}
}
