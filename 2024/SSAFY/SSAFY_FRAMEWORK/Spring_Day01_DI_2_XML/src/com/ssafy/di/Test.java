package com.ssafy.di;

import java.util.Scanner;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.GenericXmlApplicationContext;

public class Test {
	public static void main(String[] args) {
		
		ApplicationContext context = new GenericXmlApplicationContext("applicationContext2.xml");
		
		System.out.println("1");
		Programmer p = context.getBean("programmer", Programmer.class);
		Desktop desktop = (Desktop)context.getBean("desktop");
		p.setComputer(desktop);
		
		System.out.println("2");
		p.coding();
		
		//싱글톤으로 관리(스코프 설정 따로 안하면 디폴
		Desktop d2 = context.getBean("desktop", Desktop.class);
		System.out.println(desktop == d2);
		
	}
}