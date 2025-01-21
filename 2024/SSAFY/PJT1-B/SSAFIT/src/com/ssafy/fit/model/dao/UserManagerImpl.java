package com.ssafy.fit.model.dao;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

import com.ssafy.fit.model.User;

public class UserManagerImpl implements IUserManager, Serializable {
	private static final long serialVersionUID = 1L;
	//싱글톤으로 구성
	private List<User> userList = new ArrayList<User>();
	private static UserManagerImpl instance = new UserManagerImpl();
	
	private UserManagerImpl() {}
	
	public static UserManagerImpl getInstance() {
		return instance;
	}
	
	
	//회원가입을 위한 addUser
	//기존에 해당 회원이 있으면 false
	//없으면 리스트에 추가하고 true 리
	@Override
	public boolean addUser(User user) {
		for (int i = 0; i<userList.size(); i++) {
			if(userList.contains(user)) {
				return false;
			}
		}
		userList.add(user);
		return true;
	}
	
	// 로그인을 위한 searchId
	// Id를 찾아서 password랑 비교해주기 위해 사용됨
	@Override
	public User searchId(String id) {
		for(int i = 0; i<userList.size(); i++) {
			if(userList.get(i).getId().equals(id)) {
				return userList.get(i);
			}
		}
		return null;
	}


	@Override
	public List<User> getList() {
		if (!userList.isEmpty()) {
			for(int i = 0; i<userList.size(); i++) {
				System.out.println(""+(i+1)+" "+userList.get(i).toString());
			}
		}
		return null;
	}


	@Override
	public void saveUserData() {
		try(ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("user.dat"))){
			oos.writeObject(this.userList);
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	}

	@Override
	public void loadUserData() {
		File file = new File("user.dat");
		if(file != null) {
			try(ObjectInputStream ois = new ObjectInputStream(new FileInputStream(file))){
				Object o = ois.readObject();
				this.userList = (ArrayList<User>)o;
			} catch (IOException | ClassNotFoundException e) {
			}
		}
		
	}

	@Override
	public boolean matching(String id, String password) {
		if(searchId(id).getPassword().equals(password)) {
			return true;
		}
		return false;
	}
	
	
	

}
