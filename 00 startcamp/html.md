# HTML

## Element, 요소
* content의 type을 지정
* Element_name은 표준으로 정의
* 
,,, 작성 안함,, 멍청이 김혜민


## 요소의 종류
### Block level element
* 요소를 넣고 옆 여백에 Margin이 있어서 다음 항목이 아래로 밀려남
* 새로운 행에 표시
* 가로 세로 위치를 자유롭게 움직일 수 있다. (margin을 넣어서)

### Inline level element
* 마진이 없다.
* 가로 세로 위치를 자유롭게 움직일 수 없다. 설정하고 싶으면 block으로 바꿔서 해야한다.


## 영문 대소문 표기법
* Pascal Case -> JihyeOh
* carmel Case -> jihyeOh
* kebob-case -> jihye-oh
* SNAKE_CASE -> JIHYE_OH


## SIMENTIC TAG
* 전부 다 block tag이다.
### header
* 이름, 이미지, 대표하는 글 등을 넣음
### nav bar
* 네비게이션바
* header안에 넣어놓기도 함
### section
### article
* 특정 글을 넣을 때
### aside
### footer
* 사업자 명, 저작권 그런 것들


## Grouping
### `<pre>`
* 기본적으로 모든 엔터, 공백은 인식이 안되지만
* pre 태그 안에서는 공백과 줄바꿈 문자가 보존된다.

### `<ol>`
* Orderd List
* 순서가 있음을 선언하는 태그
* 태그 안에 중첩으로 list 태그 추가하면 그 리스트가 ordered list가 된다.

### `<div>`
* 어떤 태그든 간에 div 태그로 감싸면 그 태그는 block이 된다.
* 겉보기에 block처럼 보이는 것 뿐(임시방편)
* 따라서 최소한으로 사용해야함

### `<a>`
* 어디론가 이동하게 해주는 태그
* `<a href = " URL "> 네이버 </a>` :  네이버라는 글씨에 URL을 걸어줌 하이퍼 링크
* <a href = "https://www.naver.com/"> 네이버 </a>

### `<span>`
* 일반 텍스트를 넣을 때

### `<img>`
* `<img src = " 이미지 경로 " alt = "대체텍스트">`

### `<form>`
* 사용자 입력 Data를 Server로 전송하기 위한 block
```
<form>
    * 서버에 보낼 정보
    * 서버에 보낼 형식 ( method, action )
</form>
```

### `<input>`




* normal flow : 왼쪽에서 오른쪽으로 / 위에서 아래로의 흐름 (vs flexed flow)
