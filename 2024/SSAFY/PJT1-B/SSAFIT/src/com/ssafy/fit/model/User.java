package com.ssafy.fit.model;

import java.io.Serializable;

public class User implements Serializable {
	private String name;
	private String id;
	private String password;
	private String email;
	
	public User() {}
	public User(String name, String id, String password, String email) {
		this.name = name;
		this.id = id;
		this.password = password;
		this.email = email;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	@Override
	public String toString() {
		return "이름 : " + name + ", id : " + id + ", password : " + password + ", email :" + email;
	}
	
	// 회원 비교를 위해(회원가입 가능 여부 및 로그인 여부)
	// id가 같은 경우를 같은 회원으로 볼게요.
	@Override
	public boolean equals(Object o) {
		if (o instanceof User) {
			return ((User)o).getId().equals(this.getId());
		}
		return false;
	}
	
	public int hashCode(Object o) {
		if (o instanceof User) {
			return ((User)o).hashCode();
		}
		return o.hashCode();
	}
	
}
