package com.ssafy.mvc.controller;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import com.ssafy.mvc.model.dto.User;

@Controller
public class RestController1 {
	
	//반환타입이 문자열이라면... 뷰 리졸버가 -> Hello REST API.jsp 를 찾는다.
	@GetMapping("/rest1/test1")
	public String test1() {
		return "Hello REST API";
	}
	@GetMapping("/rest1/test2")
	@ResponseBody
	public String test2() {
		return "Hello REST API";
	}
	
	@GetMapping("/rest1/test3")
	@ResponseBody
	public Map<String, String> test3() {
		//키:벨류
		Map<String, String> data = new HashMap<>();
		data.put("id", "ssafy");
		data.put("password", "1234");
		return data; // 잭슨이 알아서 바꿔준다(JSON으로)
	}
	
	@GetMapping("/rest1/test4")
	@ResponseBody
	public User test4() {
		User user = new User("ssafy", "1234", "김싸피");
		return user;
	}
	@GetMapping("/rest1/test5")
	@ResponseBody
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
