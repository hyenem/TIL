* 시멘틱 태그 종류 : div, span 아님
* position 기본 속성 static
    ```css
    div {
        position: static
    }
    ```
* href: 링크 가져옴
    * a태그
    * css 가져올 때 link 태그 안에 `href`
* js에서 문자열과 숫자열의 연산
    * `+` 연산자는 문자
    * 그 외에는 숫자
    * "100"-2 = 98
    * `"백"-2` : 에러
* 함수를 만드는 방식
    * 선언식 : `function 함수명(){}`
    * 표현식 : `함수명 = function(){}`
* 변수 작성하는 방식 : `var`, `let`, `const`
    * 스코프, 재선언, 재할당
* 화살표함수
* 반복문
    * for A in B
        * B에
        * 객체를 넣으면 key가 나옴
        * 배열을 넣으면 index가 나옴
    * for of
        * 객체엔 안되고, 배열을 넣으면 요소가 나옴
    * forEach
        ```js
        객체.forEach(**function**(element){
         })
        ```
* `<input value="초기값" placeholder="미리보기" disabled>` : inputTag 속성들 보기

* **동적할당 가능**
    ```js
    arr = []

    arr[0] = "진호"
    arr[99] = "엘사킴"
    arr[44] = "윤준이"

    arr.length //100
    arr[10] //undefined
    ```
* 
    ```js
    fucntion ssafy(){}
    arr = [1, true, ssafy(12), "싸피"] //배열에 아무거나 넣어도 되고, 파라매터 추가해도 오류 안남
    arr.pop() // 마지막 원소 삭제
    arr.push() // 마지막에 추가
    arr.unshift() // 만 앞에 추ㅏㄱ
    arr.shift() //맨 앞 삭제
    ```

* flex box
    ```css
    .container {
        display: flex;
        flex-direction: row; //메인축과 cross축
        flex-wrap: wrap;
        flex-flow: row wrap;
        justify-content: start, end, center, space-around, space-between, space-evenly /*이븐리는 양쪽 여백이 다 똑같은 갓 */
        align-items: start, end, center, baseline /*베이스라인은 아래쪽을 기준으로 맞추는 것*/ stretch/*꽉 채우는 것*/
        -> 중앙에 맞추고 싶으면 어떻게 해야해요?
    }
    ```

* js
    * `==` 비교
    * `===` 일치 연산자(타입과 모습이 모두 동일해야함)

* margin, border, padding, box-sizing
    * 값을 넣을 때 시계방향으로 돌아감
    * 값이 하나만 들어가면 상하좌우 다
    * 두개일땐 상하/좌우
    * 세개일땐 상/좌우/하
    * 네개일 땐 상/우/하/좌(시계방향)
* `box-sizing: border-box`: 박스 사이즈가 보더까지 감(마진 필요없어!) border-box 맞는지 알아보기

* 선택자 우선순위
    * *<태그<.<id<!important
* display: none 공간x, 화면x / visibility: hidden 공간o, 화면x
    * html elements엔 있음!!!!

* flex-grow: 부모와 비례해서 크기 늘리기, 줄이기

* div태그에 배경화면을 바꾸고 싶어요. -> **background-image**, **backgrount-color**
* null, undefined, 0, NaN : 차이점
    * null 공간 o, 값 x
    * **undefined** 공간 x
    * NaN: 뭔가 있긴한데 사용할 수 업슴
* form 태그 안에 들어가는 인풋값을 하나로 묶고싶으면 : fieldset
* input 태그 : label
* textarea 태그 : legend

* window 함수 중에서 알림을 주고싶을 때 `alert` / 확인, 취소 값 받고 싶을 때 `confirm`