package com.ssafy.di;

import java.util.Scanner;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.GenericXmlApplicationContext;

public class Test2 {
	public static void main(String[] args) {
		ApplicationContext context = new GenericXmlApplicationContext("applicationContext2.xml");
		
		Programmer p = context.getBean("programmer", Programmer.class);
		p.coding();
	}
}