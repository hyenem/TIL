package com.ssafy.di3_타입의존성제거;

//스프링컨테이너 맛보기!
//의존관계 역전 맛보기!
public class Test {
	public static void main(String[] args) {
		Desktop desktop = new Desktop();
		Laptop laptop = new Laptop();
		
		//프로그래머가 데스크톱에 대한 의존성을 가지고 있다.
		//다형성!!!
		// 느슨한 결합
		Programmer p = new Programmer(desktop);
		
		p.coding();
	}
}
