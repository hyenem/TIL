package com.ssafy.mvc.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import jakarta.servlet.http.HttpSession;

@Controller
public class UserController {
	
	@GetMapping("login")
	public String loginForm() {
		return "user/loginForm";
	}
	
	@PostMapping("login")
	public String login(@RequestParam("id") String id, @RequestParam String pw, HttpSession session) {
		//DB에서 로그인 정보 맞는지 채크하고
		session.setAttribute("loginUser", id);
		return "redirect:hello";
	}
	
	@GetMapping("logout")
	public String logout(HttpSession session) {
		session.invalidate();
		return "redirect:/";
	}
}
