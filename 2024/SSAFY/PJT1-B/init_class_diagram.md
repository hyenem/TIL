* + : public
* - : private
* # : protected
* ~ : default
  
* Class 
* 추상클래스명 {abstract}
* 인터페이스명 <<interface>>

* static => {readonly}
-----

# 클래스 다이어그램

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

