```
Class User
- name : String
- id : String
- password : String
- email : String
+ constructor User()
+ constructor User(name : String, id:String, password:String, email:String)
+ getName(): String
+ getId() : String
+ getPassword() : Stirng
+ getEmail() : String
+ setName(name : String): void
+ setId(id : String) : void
+ setPassword(password : String) : void
+ setEmail(email : String) : void
+ toString() : String

interface IUserMananger
+abstract searchId(id : String) : User
+abstract logIn(id : String, password : String) : User
+abstract logOut() : void
+abstract getList() : String
+abstract addUser(user : User) : boolean
+abstract saveUserData(file_path : String) : void

class UserImpl
- static final MAX_USER_SIZE : int
- userList : Map<Integer,List<User>>
- static instance : UserImpl
- constructor UserImpl()
+ static getInstance() : UserImpl
+ searchId(id : String) : User
+ logIn(id : String, password : String) : User
+ logOut() : void
+ getList() : String
+ addUser(user : User) : boolean
+ saveUserData(file_path : String) : void
```
