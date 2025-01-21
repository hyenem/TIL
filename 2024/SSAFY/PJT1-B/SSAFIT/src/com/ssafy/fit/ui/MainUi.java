package com.ssafy.fit.ui;


import com.ssafy.fit.model.dao.IUserManager;
import com.ssafy.fit.model.dao.UserManagerImpl;
import com.ssafy.fit.util.SsafitUtil;

public class MainUi {
	UserUi userui = UserUi.getInstance();
	VideoUi videoui = VideoUi.getInstance();
	SsafitUtil util = new SsafitUtil();
	UserManagerImpl usermanager = UserManagerImpl.getInstance();
	
	public void service() {
		System.out.println("---------SSAFIT과 함께 건강을 지켜요!---------");
		while(true) {
			System.out.println("실행할 메뉴를 선택해주세요.");
			System.out.println("1. 로그인/로그아웃");
			System.out.println("2. 게시판 보기");
			System.out.println("3. 종료");
			System.out.println("---------------------------------------");
			int selection = util.inputInt("실행할 메뉴를 선택해주세요. : ");
			if(selection == 1) {
				userui.service();
			} else if (selection ==2) {
				videoui.service();
			} else if (selection ==3) {
				exit();
			}
			
		}
		
	}
	
	public void exit() {
		usermanager.saveUserData();
		System.exit(0);
	}
}
