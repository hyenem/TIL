package com.ssafy.mvc.controller;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.ssafy.mvc.model.dto.User;

@RestController //ResponseBody 자동으로 붙는 것
@RequestMapping("/rest2")
public class RestController2 {
	
	//반환타입이 문자열이라면... 뷰 리졸버가 -> Hello REST API.jsp 를 찾는다.
	@GetMapping("/test1")
	public String test1() {
		return "Hello REST API";
	}
	@GetMapping("/test2")
	public String test2() {
		return "Hello REST API";
	}
	
	@GetMapping("/test3")
	public Map<String, String> test3() {
		//키:벨류
		Map<String, String> data = new HashMap<>();
		data.put("id", "ssafy");
		data.put("password", "1234");
		return data; // 잭슨이 알아서 바꿔준다(JSON으로)
	}
	
	@GetMapping("/test4")
	public User test4() {
		User user = new User("ssafy", "1234", "김싸피");
		return user;
	}
	
	@GetMapping("/test5")
	public List<User> test5() {
		List<User> user = new ArrayList<>();
		user.add(new User("ssafy", "1234", "김싸피"));
		user.add(new User("ssafy", "1234", "김싸피"));
		user.add(new User("ssafy", "1234", "김싸피"));
		user.add(new User("ssafy", "1234", "김싸피"));
		user.add(new User("ssafy", "1234", "김싸피"));
		user.add(new User("ssafy", "1234", "김싸피"));
		return user;
	}
}
