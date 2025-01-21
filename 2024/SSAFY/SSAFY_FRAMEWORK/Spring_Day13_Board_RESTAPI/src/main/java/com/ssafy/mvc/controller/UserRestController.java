package com.ssafy.mvc.controller;

import java.util.List;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.ssafy.mvc.model.dto.User;
import com.ssafy.mvc.model.service.UserService;

@RestController
@RequestMapping("/api-user")
public class UserRestController {
	private final UserService userService;
	public UserRestController(UserService userService) {
		this.userService = userService;
	}
	
	//사용자 목록 전체 가져오기
	@GetMapping("/users")
	public ResponseEntity<List<User>> userList(){
		List<User> list = userService.getUserList();
		//사람이 없을 뿐 에러는 아니었다,, 그래서 204정도를 고려해보았다.
		return new ResponseEntity<List<User>>(list, HttpStatus.OK);
	}
	
	
	//사용자 회원가입
	@PostMapping("/users")
	public ResponseEntity<Void> signup(@RequestBody User user){
		userService.signup(user);
		return ResponseEntity.status(HttpStatus.OK).build();
	}
	
	
	//로그인
//	@PostMapping("/login")
//	public ResponseEntity<>
	
	
	//로그아웃
	
	
}
