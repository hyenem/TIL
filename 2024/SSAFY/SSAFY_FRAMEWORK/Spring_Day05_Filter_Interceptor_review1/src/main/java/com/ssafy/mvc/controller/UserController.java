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
		if(user.getId().equals("ssafy") && user.getPw().equals("1234")) {
			session.setAttribute("loginUser", user.getId());
			return "redirect:hello";
		}
		return "redirect:login";
	}
	
	@GetMapping("/logout")
	public String logout(HttpSession session) {
		session.invalidate();
		
		return "redirect:/";
	}

}
