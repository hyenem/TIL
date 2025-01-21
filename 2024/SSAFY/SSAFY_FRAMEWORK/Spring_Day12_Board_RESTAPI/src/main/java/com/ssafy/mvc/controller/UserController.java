package com.ssafy.mvc.controller;

import java.net.http.HttpRequest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import com.ssafy.mvc.model.dto.User;
import com.ssafy.mvc.model.service.UserService;

import jakarta.servlet.http.HttpSession;

@Controller
public class UserController {
	
	private final UserService userService;
	
	
//	@Autowired
	public UserController(UserService userService) {
		this.userService = userService;
	}

	@GetMapping("/login")
	public String loginForm() {
		return "user/loginform";
	}
	
	@PostMapping("/login")
	public String login(@ModelAttribute User user, HttpSession session) {
		User tmp = userService.login(user.getId(), user.getPassword());
		//tmp : 정상로그인 -> User정보 / 비정상로그인 -> null
		if(tmp==null) {
			//로그인 화면으로 보내!
			return "redirect:login";
		}
		//아래의 코드가 실행된다는 것은! (로그인이 제대로 OK라는 뜻)
		session.setAttribute("loginUser", tmp.getName());
		return "redirect:list";
	}
	
	//로그아웃
	@GetMapping("/logout")
	public String logout(HttpSession session) {
		session.invalidate();
		return "redirect:list";
	}
	
	//회원가입 -> 실습시간에 만들어볼것
	
	@GetMapping("/users")
	public String userList(Model model) {
		model.addAttribute("userList", userService.getUserList());
		return "/user/adminPage";
	}
}
