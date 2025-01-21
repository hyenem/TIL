package com.ssafy.mvc.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.ssafy.mvc.model.dto.User;

import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpSession;

@Controller
public class UserController {
//정석! Service를 의존성 주입 받아야한다.!
	
//	@Autowired
//	private UserService userService;
//	
//	@Autowired
//	public void setUserService(UserService userService) {
//		this.userService=userService;
//	}
//	
//	@Autowired
//	public UserController(UserService userService) {
//		this.userService=userService; 
//	}
	
	@GetMapping("/login")
	public String loginForm() {
		return"user/loginForm";
	}
	
//	@PostMapping("/login")
//	public String login(@RequestParam("id") String id, @RequestParam("pw") String pw){
//		//userService라는 친구를 통해서 실제로 id/pw을 이용하여 DB까지 확인하고 실제 유저가 맞는지 확인해야됨.
//		//세션에 정보를 저장해야됨.
//		System.out.println(id);
//		System.out.println(pw);
//		
//		
////		return "hello";
//		return "redirect:hello";
//	}
	
//	@PostMapping("/login")
//	public String login(@ModelAttribute User user, HttpServletRequest request) {
//		System.out.println(user);
//		//세션에 저장!!
//		
//		HttpSession session = request.getSession();
//		return "redirect:hello";
//	}
	@PostMapping("/login")
	public String login(@ModelAttribute User user, HttpSession session) {
		System.out.println(user);
		//세션에 저장!!
		
//		session.setAttribute("loginUser", user); //이렇게 하면 password까지 같이 저장됨,,
		//지금은 서비스를 구현하지 않아서 넘겨받은 user의 id를 냅다넣었다!
		//하지만 실제로 구현하고 난 뒤!!! 인증받은 정보만을 넣어라~~~~
		session.setAttribute("loginUser", user.getId());
		return "redirect:hello";
	}
	
	@GetMapping("/logout")
	public String logout(HttpSession session) {
		//로그아웃을 하는 방법 2가지
		//1. 세션에서 유저 속성 지우는 작업
		session.removeAttribute("loginUser");
		
		//2. 세션 자체를 초기화
		session.invalidate();
		
		return "redirect:/";
	}
}
