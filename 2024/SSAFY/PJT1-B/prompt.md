# 1

너는 클래스다이어그램 30년차 전문가야. 우리는 제공되는 영상정보 데이터 파일을 기반으로 필요한 정보를 파싱 처리한 후 영상정보를 제공하는 목록 화면과 영상에 대한 리뷰를 관리하는 프로그램을 구현하려고 해. 먼저 클래스 다이어그램을 만들기 위해 너의 도움이 필요해. 아래 클래스다이어그램을 보고 기본 기능을 구현하려고 하는데, 자세한 기능은 아래 설명과 같아.

1) 기본 기능
 영상에 대한 리뷰 관리 프로그램은 영상목록화면에서 영상을 선택한 후 
선택한 영상과 관련된 리뷰 목록, 등록 기능을 제공한다.

2) 추가 기능 
위 기본 기능 구현 후, 회원가입 및 가입한 회원 정보를 보여주는 목록 화면을 
구현한다. 프로그램을 종료 시 가입한 회원의 정보를 파일로 저장하고 프로그램 시작 시 파일에 저장되어 있는 회원의 정보를 로딩한다. 회원정보는 아이디, 이름, 비밀번호, 이메일을 필수로 하고 이외의 정보들은 필요에 따라서 추가한다.

기본 기능과 추가 기능을 구현하고자 하는데, 아래 클래스다이어그램을 보고 개선사항이 있으면 알려주고, 개선사항을 반영해 다시 결과를 출력해줘. 빠뜨린 클래스나 속성, 메소드가 있다면 추가하고 알려줘. 항상 도와줘서 고마워.


```
VideoReviewDao <<interface>>
패키지: com.ssafy.fit.model.dao
~ insertReview(videoReview: VideoReview) : int
~ selectReview(videoNo: int) : List<VideoReview>

Class VideoReviewDaoImpl
패키지: com.ssafy.fit.model.dao
- reviewNo: int {readonly}
- videoReviewDb: Map<Integer, List<VideoReview>>
- instance: VideoReviewDaoImpl{readonly}
- VideoReviewDaoImpl()
+ getInstance(): VideoReviewDaoImpl {readonly} `???`
+ InsertRevuew(videoReview: VideoReview): int
+ selectReview(videoNo: int List <VideoReview>) 

Clas VideoReview
패키지: com.ssafy.fit.model
- videoNo: int
- reviewNo: int
- nickName: String
- content: String
+ getVideoNo(): int
+ setVideoNo(videoNo: int): void
+ getNickName(): String
+ setNickName(nickName: String) : void
+ getReviewNo(): int
+ setReviewNo(reviewNo: int): void
+ content에 대한 getter, setter


Class SsafitUtil
패키지: com.ssafy.fit.util
- sc: Scanner{readonly}
- SsafitUtil()
+ input(msg: String): String
+ inputInt(msg: String): int
+ printLine(): void
+ printLine(ch: char): void
+ printLine(ch: char, len: int)
+ screenClear(): void

Class MainUi
패키지: com.ssafy.fit.ui
+ service(): void
- exit(): void

Class VideoUi
패키지: com.ssafy.fit.ui
속성
- videoDao: VideoDao
- instance: VideoUI {readonly}
메서드
- VideoUI()
+ getInstance(): VideoUi
+ service(): void
- listVideo(): void
- detail(video): void
설명: 비디오 관련 사용자 인터페이스를 제공하는 클래스입니다.


VideoReviewUi
패키지: com.ssafy.fit.ui
속성
- videoReviewDao: VideoReviewDao
- instance: VdeoReviewUi {readonly}
- videoNo: int
메서드
+ getInstance(videoNo: int): VideoReviewUi
+ service(): void
- listReview(): void
- registReview(): void
설명: 비디오 리뷰 관련 사용자 인터페이스를 제공하는 클래스입니다.

SsafitApplication
패키지: com.ssafy.fit.test
메서드: main(args: String[]): void
설명: 메인 어플리케이션 클래스로, 프로그램 시작점을 나타냅니다.

VideoDao (인터페이스)
패키지: com.ssafy.fit.model.dao
메서드
~ selectVideoByNo(no: int): Video
~ selectVideo(): List<Video>
설명: Video 데이터 액세스 객체의 인터페이스입니다.

VideoDaoImpl
패키지: com.ssafy.fit.model.dao
속성: 
- list: List<Video>
- instance: VideoDaoImpl {readonly}
메서드
- VideoDaoImpl()
+ getInstance(): VideoDaoImpl
+ selectVideo(): List <Video>
+ selectVideoByNo(no: int): Video
설명: VideoDao 인터페이스를 구현한 클래스입니다. Video 데이터를 리스트로 관리합니다.

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
상속 관계와 구현 관계는 아래와 같아.
```
1. SsaiftApplication 클래스와  MainUi 클래스는 서로 양방향연관 관계입니다.
2. MainUi 클래스와 VideoUi 클래스는 서로 양방향 연관관계입니다.
3. VideoUi 클래스와 VideoDao 인터페이스는 집합관계입니다.
4. VideoDaoImpl 클래스는 VideoDao 인터페이스를 구현합니다.
5. Video 클래스와 VideoDaoImpl 클래스는 집합관계입니다.
6. VideoUi 클래스와 VideoReviewUi 클래스는 서로 양방향연관 관계입니다.
7. VideoReviewUi 클래스와 VideoReviewDao 인터페이스는 집합관계입니다.
8. VideoReviewDaoImpl클래스가 VideoReviewDao 인터페이스를 구현합니다.
9. VideoReviewDaoImpl 클래스와 VideoReview 클래스는 집합관계입니다.
```