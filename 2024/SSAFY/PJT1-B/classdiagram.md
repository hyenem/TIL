```
+---------------------------+
|        VideoReviewDao     |
+---------------------------+
| + insertReview(VideoReview): int  |
| + selectReview(videoNo: int): List<VideoReview> |
+---------------------------+

+-----------------------------+
|    VideoReviewDaoImpl       |
+-----------------------------+
| - reviewNo: int {readonly}  |
| - videoReviewDb: Map<Integer, List<VideoReview>> |
| - instance: VideoReviewDaoImpl {readonly, static} |
+-----------------------------+
| + getInstance(): VideoReviewDaoImpl {static} |
| + insertReview(VideoReview): int |
| + selectReview(videoNo: int): List<VideoReview> |
+-----------------------------+

+---------------------------+
|        VideoDao           |
+---------------------------+
| + selectVideoByNo(no: int): Video |
| + selectVideo(): List<Video> |
+---------------------------+

+-----------------------------+
|    VideoDaoImpl             |
+-----------------------------+
| - list: List<Video>         |
| - instance: VideoDaoImpl {readonly, static} |
+-----------------------------+
| + getInstance(): VideoDaoImpl {static} |
| + selectVideo(): List<Video> |
| + selectVideoByNo(no: int): Video |
+-----------------------------+

+---------------------------+
|        VideoReview        |
+---------------------------+
| - videoNo: int            |
| - reviewNo: int           |
| - nickName: String        |
| - content: String         |
+---------------------------+
| + getVideoNo(): int       |
| + setVideoNo(videoNo: int): void |
| + getReviewNo(): int      |
| + setReviewNo(reviewNo: int): void |
| + getNickName(): String   |
| + setNickName(nickName: String): void |
| + getContent(): String    |
| + setContent(content: String): void |
+---------------------------+

+---------------------------+
|        Video              |
+---------------------------+
| - videoNo: int            |
| - title: String           |
| - description: String     |
+---------------------------+
| + getVideoNo(): int       |
| + setVideoNo(videoNo: int): void |
| + getTitle(): String      |
| + setTitle(title: String): void |
| + getDescription(): String |
| + setDescription(description: String): void |
+---------------------------+

+---------------------------+
|           User            |
+---------------------------+
| - id: String              |
| - name: String            |
| - password: String        |
| - email: String           |
+---------------------------+
| + User(id: String, name: String, password: String, email: String) |
| + getId(): String         |
| + setId(id: String): void |
| + getName(): String       |
| + setName(name: String): void |
| + getPassword(): String   |
| + setPassword(password: String): void |
| + getEmail(): String      |
| + setEmail(email: String): void |
| + toString(): String      |
+---------------------------+

+---------------------------+
|        IUserManager       |
+---------------------------+
| + searchId(id: String): User |
| + logIn(id: String, password: String): User |
| + logOut(): void          |
| + getList(): String       |
| + addUser(user: User): boolean |
| + saveUserData(file_path: String): void |
+---------------------------+

+-----------------------------+
|        UserManagerImpl      |
+-----------------------------+
| - static final MAX_USER_SIZE: int |
| - userList: Map<String, User> |
| - static instance: UserManagerImpl {static} |
+-----------------------------+
| + getInstance(): UserManagerImpl {static} |
| + searchId(id: String): User |
| + logIn(id: String, password: String): User |
| + logOut(): void            |
| + getList(): String         |
| + addUser(user: User): boolean |
| + saveUserData(file_path: String): void |
+-----------------------------+

+---------------------------+
|        MainUi             |
+---------------------------+
| + service(): void         |
| - exit(): void            |
+---------------------------+


+-----------------------------+
|         VideoUi             |
+-----------------------------+
| - videoDao: VideoDao        |
| - instance: VideoUi {readonly, static} |
+-----------------------------+
| + getInstance(): VideoUi {static} |
| + service(): void           |
| - listVideo(): void         |
| - detail(video: Video): void |
+-----------------------------+

+-----------------------------+
|        VideoReviewUi        |
+-----------------------------+
| - videoReviewDao: VideoReviewDao |
| - instance: VideoReviewUi {readonly, static} |
| - videoNo: int              |
+-----------------------------+
| + getInstance(videoNo: int): VideoReviewUi {static} |
| + service(): void           |
| - listReview(): void        |
| - registReview(): void      |
+-----------------------------+

+---------------------------+
|        SsafitUtil         |
+---------------------------+
| - sc: Scanner {readonly}  |
+---------------------------+
| + input(msg: String): String |
| + inputInt(msg: String): int |
| + printLine(): void       |
| + printLine(ch: char): void |
| + printLine(ch: char, len: int): void |
| + screenClear(): void     |
+---------------------------+

+---------------------------+
|    SsafitApplication      |
+---------------------------+
| + main(args: String[]): void |
+---------------------------+
```

관계도
SsafitApplication <--> MainUi: 양방향 연관 관계
MainUi <--> VideoUi: 양방향 연관 관계
VideoUi --> VideoDao: 집합 관계
VideoDaoImpl --> VideoDao: 구현 관계
VideoDaoImpl --> Video: 집합 관계
VideoUi <--> VideoReviewUi: 양방향 연관 관계
VideoReviewUi --> VideoReviewDao: 집합 관계
VideoReviewDaoImpl --> VideoReviewDao: 구현 관계
VideoReviewDaoImpl --> VideoReview: 집합 관계
MainUi --> UserManagerImpl: 집합 관계
UserManagerImpl --> IUserManager: 구현 관계
UserManagerImpl --> User: 집합 관계

요약
회원 관리 기능 추가: 사용자 정보 관리 및 파일 저장/로드 기능 추가.
싱글톤 패턴: 여러 클래스에서 싱글톤 패턴을 사용하여 인스턴스 관리.
인터페이스와 구현 클래스 분리: 인터페이스와 구현 클래스를 분리하여 코드의 확장성과 유지보수성을 높임.
양방향 연관 관계 및 집합 관계 명시: 클래스 간의 명확한 관계 설정.
유틸리티 클래스 추가: 공통 기능을 별도의 유틸리티 클래스로 분리하여 재사용성을 높임.

--YES

  
  
  
클래스 다이어그램과 관련된 코드를 보고 개선할 사항들을 반영하고, 필요한 클래스 및 메서드를 추가하여 클래스 다이어그램을 완성해 보겠습니다.

### 개선사항 및 추가 사항

1. **VideoReviewDaoImpl 클래스의 메서드 오타 수정**:
   - `+ InsertRevuew(videoReview: VideoReview): int` -> `+ insertReview(videoReview: VideoReview): int`

2. **Video 클래스에 있는 getContent와 setContent 메서드 추가**:
   - `+ getContent(): String`
   - `+ setContent(content: String): void`

3. **User 클래스와 관련된 구현**:
   - IUserManager 인터페이스와 UserImpl 클래스에 대해 추가 설명 및 구현 세부사항 추가

4. **MainUi 클래스에 exit() 메서드의 접근 제한자 변경**:
   - `- exit(): void` -> `+ exit(): void`

5. **VideoReviewUi 클래스의 `instance` 속성 오타 수정**:
   - `- instance: VdeoReviewUi {readonly}` -> `- instance: VideoReviewUi {readonly}`

### 클래스 다이어그램 코드 수정

```plaintext
class SsaiftApplication {
    +main(args: String[]): void
}

class MainUi {
    +service(): void
    +exit(): void
}

class SsaiftUtil {
    -sc: Scanner
    +input(msg: String): String
    +inputInt(msg: String): int
    +printLine(): void
    +printLine(ch: char): void
    +screenClear(): void
}

interface VideoDao {
    +selectVideoByNo(no: int): Video
    +selectVideo(): List<Video>
}

class VideoDaoImpl implements VideoDao {
    -list: List<Video>
    -instance: VideoDaoImpl
    +getInstance(): VideoDaoImpl
    +selectVideo(): List<Video>
    +selectVideoByNo(no: int): Video
}

class Video {
    -no: int
    -title: String
    -part: String
    -url: String
    +getNo(): int
    +setNo(no: int): void
    +getTitle(): String
    +setTitle(title: String): void
    +getPart(): String
    +setPart(part: String): void
    +getUrl(): String
    +setUrl(url: String): void
    +getContent(): String
    +setContent(content: String): void
    +toString(): String
}

class VideoUi {
    -videoDao: VideoDao
    -instance: VideoUi
    +getInstance(): VideoUi
    +service(): void
    -listVideo(): void
    -detail(video): void
}

class VideoReview {
    -videoNo: int
    -reviewNo: int
    -nickName: String
    -content: String
    +getVideoNo(): int
    +setVideoNo(videoNo: int): void
    +getNickName(): String
    +setNickName(nickName: String): void
    +getReviewNo(): int
    +setReviewNo(reviewNo: int): void
    +getContent(): String
    +setContent(content: String): void
}

interface VideoReviewDao {
    +insertReview(videoReview: VideoReview): int
    +selectReview(videoNo: int): List<VideoReview>
}

class VideoReviewDaoImpl implements VideoReviewDao {
    -reviewNo: int
    -videoReviewDb: Map<Integer, List<VideoReview>>
    -instance: VideoReviewDaoImpl
    +getInstance(): VideoReviewDaoImpl
    +insertReview(videoReview: VideoReview): int
    +selectReview(videoNo: int): List<VideoReview>
}

class VideoReviewUi {
    -videoReviewDao: VideoReviewDao
    -instance: VideoReviewUi
    -videoNo: int
    +getInstance(videoNo: int): VideoReviewUi
    +service(): void
    -listReview(): void
    -registReview(): void
}

class User {
    -name: String
    -id: String
    -password: String
    -email: String
    +User(name: String, id: String, password: String, email: String)
    +getName(): String
    +getId(): String
    +getPassword(): String
    +getEmail(): String
    +setName(name: String): void
    +setId(id: String): void
    +setPassword(password: String): void
    +setEmail(email: String): void
    +toString(): String
}

interface IUserManager {
    +searchId(id: String): User
    +logIn(id: String, password: String): User
    +logOut(): void
    +getList(): List<User>
    +addUser(user: User): boolean
    +saveUserData(filePath: String): void
}

class UserManagerImpl implements IUserManager {
    -static final MAX_USER_SIZE: int
    -userList: Map<Integer, List<User>>
    -static instance: UserManagerImpl
    +UserManagerImpl()
    +static getInstance(): UserManagerImpl
    +searchId(id: String): User
    +logIn(id: String, password: String): User
    +logOut(): void
    +getList(): List<User>
    +addUser(user: User): boolean
    +saveUserData(filePath: String): void
}

SsaiftApplication <--> MainUi
MainUi <--> VideoUi
VideoUi -> VideoDao
VideoDaoImpl --|> VideoDao
VideoDaoImpl *-- Video
VideoUi <--> VideoReviewUi
VideoReviewUi -> VideoReviewDao
VideoReviewDaoImpl --|> VideoReviewDao
VideoReviewDaoImpl *-- VideoReview
IUserManager <|.. UserManagerImpl
```

### 설명

- **SsaiftApplication** 클래스는 프로그램의 시작점으로 메인 메서드를 포함합니다.
- **MainUi** 클래스는 사용자 인터페이스를 제공하며, 프로그램 서비스와 종료 기능을 제공합니다.
- **SsaiftUtil** 클래스는 유틸리티 메서드를 제공하여 사용자 입력, 화면 출력 등을 담당합니다.
- **VideoDao** 인터페이스는 비디오 데이터를 접근하기 위한 메서드를 정의합니다.
- **VideoDaoImpl** 클래스는 `VideoDao` 인터페이스를 구현하며, 비디오 데이터를 리스트로 관리합니다.
- **Video** 클래스는 비디오의 속성과 관련된 메서드를 포함합니다.
- **VideoUi** 클래스는 비디오 관련 사용자 인터페이스를 제공합니다.
- **VideoReviewDao** 인터페이스는 비디오 리뷰 데이터를 접근하기 위한 메서드를 정의합니다.
- **VideoReviewDaoImpl** 클래스는 `VideoReviewDao` 인터페이스를 구현하며, 비디오 리뷰 데이터를 관리합니다.
- **VideoReview** 클래스는 비디오 리뷰의 속성과 관련된 메서드를 포함합니다.
- **VideoReviewUi** 클래스는 비디오 리뷰 관련 사용자 인터페이스를 제공합니다.
- **User** 클래스는 사용자 정보를 관리합니다.
- **IUserManager** 인터페이스는 사용자 데이터를 관리하기 위한 메서드를 정의합니다.
- **UserManagerImpl** 클래스는 `IUserManager` 인터페이스를 구현하며, 사용자 데이터를 관리합니다.

이제 이 다이어그램을 통해 프로그램을 구현할 수 있습니다. UML 도구를 사용하여 이 다이어그램을 시각화하면 개발에 큰 도움이 될 것입니다.
