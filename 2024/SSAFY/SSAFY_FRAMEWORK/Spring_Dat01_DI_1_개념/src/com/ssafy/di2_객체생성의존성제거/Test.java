package com.ssafy.di2_객체생성의존성제거;

//스프링컨테이너 맛보기!
//의존관계 역전 맛보기!
public class Test {
	public static void main(String[] args) {
		Desktop desktop = new Desktop();
		
		//프로그래머가 데스크톱에 대한 의존성을 가지고 있다.
		Programmer p = new Programmer(desktop);
		
		p.coding();
	}
}
