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
	
	@GetMapping("/login")
	public String loginForm() {
		return"user/loginForm";
	}
	
	@PostMapping("/login")
	public String login(@ModelAttribute User user, HttpSession session) {
		//원래는 UserService를 통해서 로그인 하는게 맞아!
		//id: ssafy, pw:1234이면 통과(유일한 회원이야)ㅏ
		if(user.getId().equals("ssafy") && user.getPw().equals("1234")) {
			session.setAttribute("loginUser", user.getId());
			return "redirect:hello";
		}
		//아래 코드가 동작한다는 것은...
		//로그인에 실패했다는 뜻
		return "redirect:login";
	}
	
	@GetMapping("/logout")
	public String logout(HttpSession session) {

		session.invalidate();
		
		return "redirect:/";
	}
	
	@GetMapping("/regist")
	public String regist() {
		return "user/regist";
	}
}
