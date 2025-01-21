package com.ssafy.di;

import java.util.Scanner;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.GenericXmlApplicationContext;

public class Test {
	public static void main(String[] args) {
		
		ApplicationContext context = new GenericXmlApplicationContext("applicationContext.xml");
		
		Programmer p = context.getBean("p", Programmer.class);
		p.coding();
		
	}
}
