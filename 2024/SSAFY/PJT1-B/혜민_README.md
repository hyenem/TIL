# 혜민

## 준비 단계
1. 팀 문화
    * 팀 분석
        * 예민한 구석이 없고 적극성이 높은 성향으로 구성이 되어 있음.
        * 한 명의 연장자와 두 명의 동갑인 인원으로 구성되어 있으나 연장자 특유의 부드러운 성향 덕에 위계가 보이지 않는 구성임.
        * 모두가 자신도 모르는 사이에 다른 사람의 기분을 상하게 할까 걱정하는 마음에 공감함.
    * 갈등 관리를 위한 전략
        * 갈등이 생기면 그 자리에서 바로 해결하기.
        * 기분이 나쁘면 솔직히 이야기하고 오해가 아닌지 확인하기.
        * 이야기를 곧이 곧대로 받아들이기. 혼자 넘겨짚지 말기
    * 원활한 협업을 위한 전략
        * 주기적으로 어디까지 했는지, 어떤 걸 하고있는지 공유
            * 불필요하게 업무가 중복되는 경우를 막음
        * 모두의 코드를 알고있기(자기 파트만 알고 있으면 전체적인 흐름을 볼 수 없음)
        * 주변 사람이 집중 중일때는 급한 사항이 아니면 우선 mm으로 남겨두기.

2. git 관리
    * 팀장 정우가 레포 만들어서 관리
    * 각자 정우 레포 포크해와서 자기 레포에 push
    * 이후 정우 레포에 PR보내기

3. 프로그램 발전 수준
    * 제시된 프로그램의 명세 수준에서 크게 벗어나지 않기
    * 심화 수준까지 구현하되, 기본 수준에서 시작해서 시간되는대로 점차 더 구현하기

## ChatGPT를 이용한 클래스다이어그램 그리기
### ChatGPT 전 사전 작업
* 명세서에 주어진 클래스 다이어그램 (정우)
* 클래스와 인터페이스 사이의 관계 표현하기 (은서)
* 명세서에 주어지지 않은 User관련 클래스 다이어그램 구성하기 (혜민)

### ChatGPT 에게 요구한 것
* 프로그램의 요구를 알려주고, 더 나은 클래스 다이어그램이 있는지 물어보기
* 클래스다이어그램을 만들기 위한 planttext 문법 형태로 변환하기


## **개발 단계**
### 내 담당 : 로그인, 로그아웃, 회원가입, 회원정보조회
* User, IUserManager, UserManagerImpl, UserUi, MainUi를 작성하였다.

### User
```java
package com.ssafy.fit.model;

import java.io.Serializable;

public class User implements Serializable {
	private String name;
	private String id;
	private String password;
	private String email;
	
    // 생성자, getter, setter, toString 생략//
	
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

```
* User끼리 비교할 수 있도록 equals()와 hashCode를 재정의함.
    * 이때 key값으로 id를 지정함
    * 동명 이인이 있을 수도 있고, 비밀번호는 같을 수 도 있기 때문
* 파일로 객체를 저장하고 불러들이기 위해서 Serializable 인터페이스를 구현함.

### UserManagerImpl
```java 
package com.ssafy.fit.model.dao;

//import 생략//

public class UserManagerImpl implements IUserManager, Serializable {
	private static final long serialVersionUID = 1L;
	//싱글톤으로 구성
	private List<User> userList = new ArrayList<User>();
	private static UserManagerImpl instance = new UserManagerImpl();
	
	private UserManagerImpl() {}
	
	public static UserManagerImpl getInstance() {
		return instance;
	}
```
* 보안을 위해서 싱글톤 패턴으로 작성

```java
	//회원가입을 위한 addUser
	//기존에 해당 회원이 있으면 false
	//없으면 리스트에 추가하고 true 리턴
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
```
* 회원 가입을 위한 메서드 addUser() : 기존에 없던 user면 userlist에 user를 추가

```java
	
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
	public boolean matching(String id, String password) {
		if(searchId(id).getPassword().equals(password)) {
			return true;
		}
		return false;
	}
```
* 로그인을 위한 메서드
	* id가 없을 땐 해당 회원이 없음을 출력하고
	* 비밀번호가 맞지 않을 땐 비밀번호가 틀렸음을 출력하고 싶었다.
	* searchId()를 이용하면 그런 id를 갖는 회원이 있는지 없는지 조회할 수 있다. -> "해당 정보의 회원이 없습니다."
	* 그런 id를 갖는 회원이 있다면 searchid로 객체를 받아서 matching을 이용해서 입력받은 password가 맞는지 확인.


```java
	@Override
	public List<User> getList() {
		if (!userList.isEmpty()) {
			for(int i = 0; i<userList.size(); i++) {
				System.out.println(""+(i+1)+" "+userList.get(i).toString());
			}
		}
		return null;
	}
```
* (실제 main 메서드 안에서 사용되지는 않음)
* 관리자용 메서드
	* 지금까지 회원 가입한 모든 회원의 정보를 볼 수 있게하는 메서드
	* 보안에 굉장히 피해를 끼치는 메서드다
	* 그냥 없애는게 맞았을 것 같다,,,,ㅎㅎ,,,


```java
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
}

```
* 회원 정보를 저장하고 로드하기 위한 메서드
	* try catch 문을 이용해서 예외처리함


### UserUi
```java
public class UserUi {
	
	private static SsafitUtil util = new SsafitUtil();
	
	private static User loginUser = null;
	private static UserManagerImpl UserDao = UserManagerImpl.getInstance();
	private static UserUi instance = new UserUi();
	private UserUi() {}
	
	public static UserUi getInstance() {
		return instance;
	}
```
* 싱글톤 패턴으로 작성
* static으로 loginUser을 선언하여, 지금 이 페이지에 로그인하고 있는 사람을 저장함.

```java
	public void service() {
		while(true) {
			if(loginUser == null) {
				System.out.println("------------------------------------------------");
				System.out.println("1. 로그인");
				System.out.println("2. 회원가입");
				System.out.println("3. 이전 화면으로 돌아가기");
				System.out.println("--------------원하는 보기를 입력해주세요.--------------");
				int selection = util.inputInt("");
				if(selection == 1) {
					logIn();
					if(loginUser!=null) break;
				} else if(selection ==2) {
					join();
				} else if(selection ==3) {
					break;
				} else {
					System.out.println("1, 2, 3 중 하나를 선택해주세요.");
				}
			} else {
				System.out.println("------------------------------------------------");
				System.out.println("1. 내정보조회");
				System.out.println("2. 로그아웃");
				System.out.println("3. 이전 화면으로 돌아가기");
				System.out.println("--------------원하는 보기를 입력해주세요.--------------");
				int selection = util.inputInt("");
				if(selection == 1) {
					System.out.println(loginUser.toString());
				} else if(selection ==2) {
					loginUser = null;
				} else if(selection == 3) {
					break;
				} else {
					System.out.println("1, 2, 3 중 하나를 선택해주세요.");
				}
				
			}
		}
	}
```
* while문을 이용해서 행위가 끝났을 때 프로그램이 종료되는 것이 아니라 이 페이지에 남을지 전 페이지로 돌아갈지 선택지를 제시함.


```java
	private void logIn() {
		System.out.println("id 와 password를 입력해주세요");
		String id = util.input("id : ");
		String password = util.input("password : ");
		if(UserDao.searchId(id)!=null) {
			if(UserDao.matching(id, password)){
				loginUser = UserDao.searchId(id);
				System.out.println("로그인 되었습니다.");
			} else {
				System.out.println("비밀번호가 틀렸습니다.");
			}
		} else {
			System.out.println("해당 정보를 가진 회원이 없습니다.");
		}
	}
```
* 로그인 메서드
	* id와 password를 한번에 입력받음
	* id가 없으면 "해당 정보를 가진 회원이 없습니다." 출력
	* password가 틀리면 "비밀번호가 틀렸습니다."출력

```java
	private void join() {
		String name = util.input("이름을 입력해주세요. : ");
		String id;
		while(true) {
			id = util.input("id를 입력해주세요 : ");
			if(UserDao.searchId(id)==null) {
				break;
			} else {
				System.out.println("이미 있는 id입니다.");
				System.out.println("다른 id를 입력해주세요.");
				System.out.println();
			}
		}
		String password = util.input("password를 입력해주세요. : ");
		String email = util.input("email 입력해주세요. : ");

		
		boolean result = UserDao.addUser(new User(name, id, password, email));
		if(result) {
			System.out.println("성공적으로 회원가입 되었습니다.");
		} else {
			System.out.println("회원 가입에 실패했습니다.");
		}
	}
}

```
* 회원가입 메서드
	* 이름, id, password, email을 순서대로 받음
	* id는 key가 되므로 중복될 수 없다. 따라서 기존에 있는 id를 사용하는 이에겐 다른 id를 입력하도록 while문을 이용하여 구현
	* 자료들이 순차적으로 잘 입력 되면 userList에 user를 추가


### Main Ui
```java
package com.ssafy.fit.ui;


import com.ssafy.fit.model.dao.IUserManager;
import com.ssafy.fit.model.dao.UserManagerImpl;
import com.ssafy.fit.util.SsafitUtil;

public class MainUi {
	UserUi userui = UserUi.getInstance();
	VideoUi videoui = VideoUi.getInstance();
	SsafitUtil util = new SsafitUtil();
	UserManagerImpl usermanager = UserManagerImpl.getInstance();
	
	public void service() {
		System.out.println("---------SSAFIT과 함께 건강을 지켜요!---------");
		while(true) {
			System.out.println("실행할 메뉴를 선택해주세요.");
			System.out.println("1. 로그인/로그아웃");
			System.out.println("2. 게시판 보기");
			System.out.println("3. 종료");
			System.out.println("---------------------------------------");
			int selection = util.inputInt("실행할 메뉴를 선택해주세요. : ");
			if(selection == 1) {
				userui.service();
			} else if (selection ==2) {
				videoui.service();
			} else if (selection ==3) {
				exit();
			}
			
		}
		
	}
	
	public void exit() {
		usermanager.saveUserData();
		System.exit(0);
	}
}
```
* user 정보 파일로 저장하기
	* 프로그램을 종료하는 exit 메서드에 종료 전에 파일을 출력하게함.

### SsafitApplication
```java
public class SsafitApplication {

	public static void main(String[] args) {
		UserManagerImpl usermanager = UserManagerImpl.getInstance();
		usermanager.loadUserData();
		
		MainUi main = new MainUi();
		main.service();
		
	}

}
```
* 메인 메서드 안에 제일 처음 loadUserData() 메서드를 실행함
	* 프로그램이 실행되자마자 user 정보를 파일에서 읽어와 로드하도록 함.

	

### 클래스 다이어그램이랑 다르게 된 점
* savaUserData 메서드에 파라메터가 없어도 될 것 같다.
* UserImpl 을 Array가 아니라 List로 관리하면 굳이 maxsize를 설정해 놓을 이유가 없을수도?!?!(제거)
* 하나의 user에 여러개의 정보를 저장할게 없으니까 HashMap을 사용하기 보다는 그냥 List로 관리하는게 맞는듯
* login, logout은 UI 클래스에서 구성하는게 나을듯 (Iusermanager에서도 userimpl에서도 제거)
* loaddata를 Iusermanager와 userimpl에 추가해야함


### **개선 방향**
* 시간이 더 있었으면 다른 조원들의 코드 수정을 하면서 '로그인이 되어있으면 글을 작성할때 자동으로 그 User의 정보가 포함 될 수 있도록 (굳이 자기 닉네임을 입력하지 않아도) 하는 기능'을 구현할 수 있었을 것 같다.
* 이름이나 비밀번호를 입력할 때, 특정 조건(이름은 10글자 이하, 비밀번호는 특수문자 포함) 등을 걸어둘 수 있을 것 같다.