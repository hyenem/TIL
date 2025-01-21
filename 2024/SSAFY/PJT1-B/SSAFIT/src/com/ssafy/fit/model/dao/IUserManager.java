package com.ssafy.fit.model.dao;


import java.util.List;

import com.ssafy.fit.model.User;

public interface IUserManager {
	User searchId(String id);
	public List<User> getList();
	boolean addUser(User user);
	void saveUserData();
	void loadUserData();
	boolean matching(String id, String password);
}
