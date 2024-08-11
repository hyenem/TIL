# shopDB 실습하기

교재에서 GUI를 이용해서 shopDB를 관리하는 실습이 있길래, 나는 그걸 GUI가 아니라 명령어를 이용해서 쭉 따라가보려고 한다.

## 쿼리란 무엇인가?

> ### Query(질문, 문의하다)
> * 이전에 쿼리는 다른 프로그래밍 언어들과는 다른 대화식 언어라는 사실을 공부했다.
> *  쿼리가 그 하나의 문답이라고 생각을 하면 될 것 같다.
> * `데이터베이스에 정보를 요청하는 일`을 말한다.


## 이전 복습
* 이미 데이터 베이스를 만들고 workbench에 연결하는 방법은 알고 있다.
    ```sql
    CREATE DATABASE shopDB;
    ```
    명령어를 이용해서 데이터 베이스를 만들고, 워크벤치에서 열었다.
    이제 쿼리 창을 이용해서 table을 만들고 자료를 입력해보자.

## table 만들기
* 회원 테이블을 만들어보자
    | 열 이름(한글) | 영문 이름 | 데이터 형식 | 길이 | NULL허용 |
    |:--------:|:--------:|:--------:|:--------:|:--------:|
    |아이디|memberID|문자(CHAR)|8글자(영문)|X|
    |회원 이름|memberName|문자(CHAR)|5글자(한글)|X|
    |주소|memberAddress|문자(CHAR)|20글자(한글)|O|
* 위의 형식을 갖춘 표를 입력하기 위해 쿼리를 아래와 같이 작성했다.
    ```sql
    Use shopDB;

    CREATE table memberTBL(
        memberID CHAR(8) NOT NULL,
        memberName CHAR(5) NOT NULL,
        memberAddress CHAR(20) NULL,
        primary key(memberID)
    );
    ```

<br>

* 이번엔 제품 테이블은 만들어보겠다.
    |열 이름(한글)|영문 이름|데이터 형식|길이|NULL 허용|
    |:------:|:------:|:------:|:------:|:------:|
    |제품 이름|productName|문자(CHAR)|4글자(한글)|X|
    |가격|cost|숫자(INT)|정수|X|
    |제조일자|makeDate|날짜(DATE)|날짜형|O|
    |제조회사|company|문자(CHAR)|5글자(한글)|O|
    |남은 수량|amout|숫자(INT)|정수|X|

* 쿼리를 작성하면 아래와 같다.
    ```sql
    Use shopDB;

    CREATE table productTBL(
        productName CHAR(4) NOT NULL,
        cost INT NOT NULL,
        makeDate DATE NULL,
        company CHAR(5) NULL,
        amount INT NOT NULL,
        primary key(productName)
    )
    ```

## 데이터 입력하기
* INSERT를 이용해서 생성된 테이블에 정보를 넣어보자.
    ```sql
    INSERT INTO shopDB.memberTBL(memberID, memberName, memberAddress)
    VALUES ('Dang', '당탕이', '경기 부천시 중동'), ('Han', '한주연', '인천 남구 주안동'), ('Jee', '지운이', '서울 은평구 중산동'), ('Sang', '상길이', '경기 성남시 분당구'), ('NaoTa', '나오타', '주소불명');

    INSERT INTO shopDB.productTBL(productName, cost, makeDate, company, amount)
    VALUES ('컴퓨터', 10, 20210101, '삼성', 17), ('세탁기', 20, 20220901, 'LG', 3), ('냉장고', 5, 20230201, '대우', 22);

    ```

* 테이블에 정보가 잘 저장되었는지 보려면 `SELECT`문을 사용하면 된다.
    ```sql
    SELECT * FROM memberTBL;
    SELECT * FROM productTBL;
    ```


* 이번엔 `DELETE`문을 이용해서 자료를 지워보자.
    ```sql
    DELETE FROM shopDB.memberTBL
    WHERE memberID = 'NaoTa';
    ```
    다시 `SELECT`문으로 확인해보면 ID가 NaoTa인 행이 지워진 것을 확인할 수 있다.


## 뷰 만들기
* 뷰는 테이블을 보는 관점을 바꾸는 것이다.
* 예를 들어서 회원 정보를 조회해야한다고 해보자. 이미 회원의 데이터로서 주민 번호가 저장되어 있는데, 이것을 조회 가능하다면 개인정보 보안에 큰 문제가 발생한다.
* 그렇다고 주민번호를 제거한 새로운 테이블을 관리하는건, 데이터의 중복이 발생하기 때문에 불안정하고 비효울적이다.
* 따라서 그냥 테이블의 특정 정보만 볼 수 있게 조정하는데, 그 역할을 하는게 View이다.
* 아래와 같은 명령어를 통해서 만들 수 있다.
    ```sql
    Use shopDB;

    CREATE VIEW v_memberTBL
    AS
	    SELECT memberName, memberAddress FROM memberTBL;
    ```
* view는 사실 그냥 `SELECT`문을 생략해 놓은 것으로 봐도 무방하다.
* view를 보는 방법은 그냥 `SELECT`문으로 접근하면 된다. table인지 view인지는 별 상관이 없다.
    ```sql
    SELECT * FROM v_memberTBL;
    ```


## 스토어드 프로시저(Stored Procedure) 만들기
* 스토어드 프로시저는 말 그대로 특정 절차를 저장해뒀다 사용하는 것이다.
* 다른 프로그램 언어들의 함수에 대응되는 개념으로 생각하면 될 것 같다.
* 두 개의 `SELECT`문을 하나의 스토어드 스로시저로 묶어보자.
* 아래 코드와 같다.
    ```
    DELIMITER //
    CREATE PROCEDURE myProc()
    BEGIN
        SELECT * FROM memberTBL WHERE memberName='당탕이';
        SELECT * FROM productTBL WHERE productName = '냉장고';
    END //
    DELIMITER ;
    ```
* 위에서 DELIMITER 의 역할은 구분자를 설정해주는 것이다. 기본적으로 구분자는 콜론(;)으로 되어있다. 그런데 우리는 `CREATE`문을 `SELECT`문 하나가 끝 날때 끝낼 수 없다. `END`까지 가서 `CREATE`문을 끝내야한다. 그런데 중간에 콜론으로 구분되는 명령어가 들어가야하므로 콜론이 구분자이면 안되는 것이다.
* 그래서 처음에 구분자를 `//`로 설정을 한 뒤에 스토어드 프로시저를 만들고 다시 구분자를 `;`로 바궈주는 것이다.
* 스토어드 프로시저를 불러오는 명령어는 `CALL`이다.
    ```sql
    CALL myProc();
    ```


## 트리거 만들기
* 스토어드 프로시저가 특정 행위를 함수화해서 한꺼번에 불러오는 것이라면, 트리거는 내가 특정 행위를 했을 떄 자동으로 실행되는 함수를 만드는 것이다.
* 예를 들어 누군가 회원탈퇴를 했다고 해보자. 그러면 회원 정보를 지울텐데, 나중에 와서 자기가 회원이었는지 아닌지를 확인하겠다고 하면 방법이 없지 않는가? 그래서 deletedmember정보를 보관하는데, 매번 회원을 지울 때 마다 deletedmember정볼르 업데이트 한다고 하면 그것 또한 귀찮고, 한 번이라도 빠트리면 너무 곤란한일이지 않는가?
* 그래서 memberTBL에 삭제가 일어나면 자동으로 deleted memberTBL에 추가가 일어나도록 하고 싶은데, 그 역할이 바로 `트리거`이다.
* 트리거 test를 하기 위해 우선 deletedmemberTBL을 만들어보자.
    ```sql
    CREATE TABLE deletedMemberTBL(
        memberID CHAR(8),
        memberName CHAR(5),
        memberAddress CHAR(20),
        deletedDate Date
    );
    ```
* 이제 트리거를 만들어보자
    ```sql
    DELIMETER //
    CREATE TRIGGER trg_deletedMemberTBL
        AFTER DELETE
        ON memberTBL
        FOR EACH ROW
    BEGIN
        INSERT INTO deletedMemberTBL
            VALUES (OLD.memberID, OLD.memberName, OLD.memberAddress, CURDATE());
    END //
    DELIMETER ;
    ```
* 트리거는 스토어드 프로시저처럼 특별히 명령어로 불러올 필요가 없다. 이제 memberTBL에서 행 하나를 삭제하기만 해도 자동으로 트리거가 발동 되어서 deletedMemberTBL에 지워진 멤버에 대한 정보와 지워진 시간까지 자동으로 삽입될거다! Like a magic~