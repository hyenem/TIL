package com.ssafy.di4_의존성주입;

import java.util.Scanner;

public class Test {
	public static void main(String[] args) {
		Desktop desktop = new Desktop();
		Laptop laptop = new Laptop();
		

//		Programmer p = new Programmer(desktop);
		
		Programmer p2 = new Programmer();
		p2.setComputer(laptop);
		
		p2.coding();
		
		Scanner sc = new Scanner(System.in);
		
		Programmer p3 = new Programmer();
		while(true) {
			p3.setComputer(ComputerFactory.getComputer(sc.next()));
			p3.coding();
		}
	}
}
