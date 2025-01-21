package com.ssafy.di;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Component;

@Component(value="p")
public class Programmer {
	private Computer computer;
	
	public Programmer() {}
	
	@Autowired
	public Programmer(Computer computer) {
		//프로그래머를 한 명 고용했다면 가지고있는 데스크탑 한 개 줘!
		this.computer = computer;
	}
	
	// 설정자를 이용해서 주입
	public void setComputer(@Qualifier("desktop") Computer computer) {
		this.computer = computer;
	}
	
	//메서드를 이용한 주입도 가능하다!!
	
	public void coding() {
		System.out.println(computer.getInfo()+"으로 개발을 합니다.");
	}
}
