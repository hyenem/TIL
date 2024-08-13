# Day3_SELECT문 정복하기
### 기본적인 WHERE절
* 
    ```sql
    SELECT * FROM usertbl WHRER name = '김혜민';
        -- 이름이 김혜민인 모든 열을 가져온다는 뜻
    ```

### BETWEEN ... `AND`와 `IN()` 그리고 `LIKE`
* 연속적인 조건에 대해서는 아래와 같이 찾을 수 있다.
    ```sql
    SELECT userID, Name FROM usertbl WHERE birthYear >= 1970 AND height >= 182;
        -- usertbl에서 생년이 1970이상이고 키가 182이상인 행의 userID와 Name을 가져온다는 뜻

    SELECT name, height FROM usertbl WHERE height BETWEEN 180 AND 183;
        -- usertlb에서 키가 180이상 183이하인 사람의 name과 height를 가져온다는 뜻
    ```
* 연속적이지 않고 이산적인 값에 대해서는 아래와 같이 찾을 수도 있다.
    ```sql
    SELECT name, addr FROM usertbl WHERE addr = '경남' OR addr ='전남';
    SELECT name, addr FROM usertbl WHERE addr IN ('경남', '전남');
    ```
* 특정 내용을 포함하는 문자열을 검색하기 위해선 아래와 같이 할 수 있다.
    ```sql
    SELECT name, height FROM usertbl WHERE name LIKE '김%';
        -- %은 무엇이든 허용한다는 뜻이다.
        -- 즉, 위와 같이 쓰면 '김'으로 시작하는 모든 이름을 검색한다는 뜻이다.
    SELECT name, height FROM usertbl WHERE name LIKE '_종신';
        -- _은 %와 달라 한 글자만 매칭한다는 뜻이다.
    ```
* 참고
    * `%`나 `_`가 문자열의 제일 앞에 들어오는 것은 MySQL의 성능에 나쁜 영향을 끼칠 수 있다.
    * 열에 인덱스가 있더라도 인덱스를 사용하지 않고 전체 데이터를 검색하게 되기 때문이다.

### `ANY`/`ALL`/`SOME` 그리고 서브쿼리(SubQuery, 하위쿼리)
* 서브쿼리란 쿼리문 안에 또 쿼리문이 들어 있는 것을 얘기한다.
    ```sql
    SELECT name, height FROM usertbl
        WHERE height >= (SELECT height FROM usertbl WHRE Name = '김경호');
    ```
* 위와 같이 쓰면 '김경호'씨의 키를 찾은 뒤에 그 키보다 큰 키를 찾아준다.
* 이때, '김경호'씨가 둘이면 어떻게 될까? 김경호씨들의 키가 모두 같으면 모를까, 다르다면 두 개의 수와 비교를 해줘야하므로 애러가 뜬다.
* 이런 문제를 해결하기 위해 사용하는게 `ANY`, `ALL`, `SOME`이다.
    ```sql
    SELECT name, height FROM usertbl
        WHERE height >= ANY (SELECT height FROM usertbl WHERE name = '김경호');
    -- ANY는 그들 중 하나보다만 조건을 만족하면 된다.

    SELECT name, height FROM usertbl
        WHERE height >= ALL (SELECT height FROM usertbl WHERE name = '김경호');
    -- ALL은 그들 모두에 대해서 조건을 만족하면 된다.

     SELECT name, height FROM usertbl
        WHERE height >= SOME (SELECT height FROM usertbl WHERE name = '김경호');
    -- SOME은 ANY와 똑같다고 봐도 된다.
    ```
* 아래 두 가지를 비교해볼까?
    ```sql
    SELECT name, height FROM usertbl
        WHERE height = ANY (SELECT height FROM usertbl WHERE name = '김경호');
    
    SELECT name, height FROM usertbl
        WHERE height IN (SELECT height FROM usertbl WHERE name = '김경호');
    ```
    * 사실상 다를 바가 없다.
    * `= ANY()` 는 `IN()`이랑 같은 것으로 봐도 된다는 것이지.

### 원하는 순서대로 정렬하여 출력 : `ORDER BY`
* 정렬은 기본적으로 오름차순으로 정렬된다.
* 내림차순으로 정렬하려면 열 이름 뒤에 `DESC`라고 적어주면 된다.
    ```sql
    SELECT name, mDate FROM usertbl ORDER BY mDate;
    SELECT name, mDate FROM usertbl ORDER BY mDate DESC;

    SELECT name, height FROM usertbl ORDER BY height DESC, name ASC;
     -- 이렇게 두 가지를 같이 쓰면 우선 앞에거대로 정렬을 하고, 앞의 기준이 같으면 뒤에것 대로 정렬해서 제시한다.
     -- 참고로 name 뒤에 붙어있는 ASC는 기본값이니까 안써줘도 상관 없다.
    
    -- 심지어는 얻으려 하는 열이 아니어도 그 열을 기준으로 정렬할 수 있다. 무슨 말이냐면
    SELECT name FROM usertbl ORDER BY height;
    ```

### 중복된 것은 하나만 남기는 `DISTINCT`
* 해당 열에서 중복된 내용을 제거하고 얻고 싶다면 아래와 같이 쓰면 된다.
    ```sql
    SELECT DISTINCT addr FROM usertbl;
    ```
* 열의 내용 중에 중복을 제거하는 것이기 때문에 열 이름 앞에 `DISTINCT`가 붙는게 자연스럽다.

### 출력하는 개수를 제한하는 `LIMIT`
* 특정 기준으로 정렬한 뒤에 전체를 다 보는게 아니라 상위 몇 개만 보고 싶을 수도 있다. 그럴때 `LIMIT` 명령어를 사용하면 좋다.
    ```sql
    SELECT emp_no, hire_date FROM employees
        ORDER BY hire_date ASC
        LIMIT 5;
    ```
* 위와 같이 쓰면 오름차순으로 작은 것 부터 5개가 뽑힌다.
* 근데 인제 막 세번째부터 다섯개를 뽑고 싶고 그럴수도 있지 않은가?
    ```sql
    SELECT emp_no, hire_date FROM employees
        ORDER BY hire_date ASC
        LIMIT 3, 5;

    -- 아래도 같은 경우이다.
    SELECT emp_no, hire_date FROM employees
        ORDER BY hire_date ASC
        LIMIT 5 OFFSET 3;
    ```

### 테이블을 복사하는 `CREATE TABLE ... SELECTION`
* 기본 형식은 아래와 같다.
    ```sql
    CREATE TABLE 새로운테이블 (SELECT 복사할열 FROM 기존테이블);
    ```
* 아래와 같이 쓸 수 있다.
    ```sql
    CREATE TABLE buytbl2 (SELECT * FROM buytbl);
    -- 이렇게 하면 buytbl이 전체가 다 복사가 된다.

    CREATE TABLE buytbl3 (SELECT userID, prodName FROM buytbl);
    -- 이렇게 하면 특정 열만 복사할 수 있다.
    ```

### `GROUP BY` 및 `HAVING` 그리고 집계 함수
* 이 내용들은 특정 열의 값에 대한 계산을 할 수 있게 한다.
* 예시를 보면 간단하게 이해할 수 있다.
    ```sql
    SELECT userID, SUM(amout) FROM buytbl GROUP BY userID;

    SELECT userID AS '사용자 아이디', SUM(amout) AS '총 구매 개수'
        FROM buytbl GROUP BY userID;
    ```
    * 위의 내용은 무슨 말이냐면 userID에 대해 그룹화를 해서 그들이 구매한 양을 각각 더하겠다는 말이다. 예를 들어서 김혜민이 과자 2개, 사과 3개를 샀으면 총 5라는 값을 주는 것이다.
    * 아래줄 처럼 쓰면 별칭을 붙여줄 수 있다. 열의 이름을 특별히 지정해주는 것이다.
* 이걸 응용하면 총 구매액을 찾을 수도 있다.
    ```sql
    SELECT userID, SUM(amout*price) AS '총 구매액'
        FROM buytbl GROUP BY userID;
    ```
* 이것 외에도 사용되는 집계 함수들은 아래와 같이 있다.
    | 함수명 | 설명 |
    |:---:|:---:|
    |AVG()|평균을 구한다.|
    |MIN()|최소값을 구한다.|
    |MAX()|최대값을 구한다.|
    |COUNT()|행의 개수를 센다.|
    |COUNT(DISTINCT)|행의 개수를 센다(중복은 1개만 인정)|
    |STDEV()|표준편차를 구한다.|
    |VAR_SAMP()|분산을 구한다.|

* 키가 가장 큰 사람과 가장 작은 사람을 추출하려고 하면 어떻게 해야할까?
    ```sql
    SELECT name, hight
        FROM usertbl
        WHERE height = (SELECT MAX(height) FROM usertbl)
            OR height = (SELECT MIN(height) FROM usertbl);
    ```
* 아래 쿼리에 대해서 생각해보자.
    ```sql
    SELECT userID AS '사용자', SUM(price*amount) AS '총 구매액'
        FROM usertbl
        WHERE SUM(price*amout)>1000
        GROUP BY userID;
    ```
    * 뭔가 느낌적으로 총 구매액이 1000을 초화하는 사람의 테이블이 나올 것 같다.
    * 하지만 사실은 오류가 난다.
    * `WHERE`절에는 절대로 집계함수가 올 수 없다.
* 이걸 해결하기 위한 것이 `HAVING`절이다.
    ```sql
    SELECT userID AS '사용자', SUM(price*amount) FROM usertbl
        GROUP BY userID
        HAVING SUM(price*amount)>1000;
        -- 이후에 추가로 정렬을 해줄수도 있다.
        -- ORDER BY SUM(price*amount) ;
    ```
    * `HAVING`절은 `WHERE`절과 마찬가지로 조건을 제한하는 역할을 하지만 `HAVING`절은 집계함수에 대한 제한이라고 생각하면 된다.
    * `이때 주의할 점!` `HAVING`절은 반드시 `GROUP BY` 다음에 나와야 한다.
* 소집계가 필요할 땐, `ROLLUP`
    ```sql
    SELECT num, groupName, SUM(prince*amount) AS '비용'
        FROM buytbl
        GROUP BY groupName, num
        WITH ROLLUP;
    ```
    * 이걸 실행하면 groupName별로 num에 대한 비용의 소계를 제시하고, 마지막에 전체 총합을 제시해준다.
    * 여기서 만약 num을 뺀다면 어떻게 될까? num이 그룹화의 대상이 아니므로 그룹이름이 같은 경우가 하나로 묶여서 제공 될 것이고, `ROLLUP`에 의해 총계가 나타날 것이다.