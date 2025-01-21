package com.ssafy.fit.ui;

import com.ssafy.fit.model.User;
import com.ssafy.fit.model.dao.UserManagerImpl;
import com.ssafy.fit.util.SsafitUtil;

public class UserUi {
	
	private static SsafitUtil util = new SsafitUtil();
	
	private static User loginUser = null;
	private static UserManagerImpl UserDao = UserManagerImpl.getInstance();
	private static UserUi instance = new UserUi();
	private UserUi() {}
	
	public static UserUi getInstance() {
		return instance;
	}
	
	public void service() {
		while(true) {
			if(loginUser == null) {
				System.out.println("------------------------------------------------");
				System.out.println("1. 로그인");
				System.out.println("2. 회원가입");
				System.out.println("3. 이전 화면으로 돌아가기");
				System.out.println("--------------원하는 보기를 입력해주세요.--------------");
				int selection = util.inputInt("");
				if(selection == 1) {
					logIn();
					if(loginUser!=null) break;
				} else if(selection ==2) {
					join();
				} else if(selection ==3) {
					break;
				} else {
					System.out.println("1, 2, 3 중 하나를 선택해주세요.");
				}
			} else {
				System.out.println("------------------------------------------------");
				System.out.println("1. 내정보조회");
				System.out.println("2. 로그아웃");
				System.out.println("3. 이전 화면으로 돌아가기");
				System.out.println("--------------원하는 보기를 입력해주세요.--------------");
				int selection = util.inputInt("");
				if(selection == 1) {
					System.out.println(loginUser.toString());
				} else if(selection ==2) {
					loginUser = null;
				} else if(selection == 3) {
					break;
				} else {
					System.out.println("1, 2, 3 중 하나를 선택해주세요.");
				}
				
			}
		}
	}
	
	private void logIn() {
		System.out.println("id 와 password를 입력해주세요");
		String id = util.input("id : ");
		String password = util.input("password : ");
		if(UserDao.searchId(id)!=null) {
			if(UserDao.matching(id, password)){
				loginUser = UserDao.searchId(id);
				System.out.println("로그인 되었습니다.");
			} else {
				System.out.println("비밀번호가 틀렸습니다.");
			}
		} else {
			System.out.println("해당 정보를 가진 회원이 없습니다.");
		}
	}
	
	private void join() {
		String name = util.input("이름을 입력해주세요. : ");
		String id;
		while(true) {
			id = util.input("id를 입력해주세요 : ");
			if(UserDao.searchId(id)==null) {
				break;
			} else {
				System.out.println("이미 있는 id입니다.");
				System.out.println("다른 id를 입력해주세요.");
				System.out.println();
			}
		}
		String password = util.input("password를 입력해주세요. : ");
		String email = util.input("email 입력해주세요. : ");

		
		boolean result = UserDao.addUser(new User(name, id, password, email));
		if(result) {
			System.out.println("성공적으로 회원가입 되었습니다.");
		} else {
			System.out.println("회원 가입에 실패했습니다.");
		}
	}
	
	

}
