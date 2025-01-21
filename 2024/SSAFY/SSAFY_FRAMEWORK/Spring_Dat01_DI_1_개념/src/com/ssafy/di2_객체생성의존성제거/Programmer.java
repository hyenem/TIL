package com.ssafy.di2_객체생성의존성제거;

//컴퓨터 필요해!
public class Programmer {
	private Desktop desktop;
	
	// 객체 생성 의존성을 제거
	public Programmer(Desktop desktop) {
		//프로그래머를 한 명 고용했다면 가지고있는 데스크탑 한 개 줘!
		this.desktop = desktop;
	}
	
	public void coding() {
		System.out.println(desktop.getInfo()+"으로 개발을 합니다.");
	}
}
