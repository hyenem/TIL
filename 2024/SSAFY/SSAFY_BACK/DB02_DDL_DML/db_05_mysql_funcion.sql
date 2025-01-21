# Q1. 숫자관련 함수 사용
-- 2의 3제곱
SELECT pow(2, 3) AS '2**3'
FROM dual; -- 가짜 문법용 테이블

-- 8 나누기 3의 나머지
SELECT mod(8,3) AS '8%3';

-- 최대값, 최솟값
SELECT greatest(10, 20, 30, 40, 50), least(10, 20, 30, 40, 50);

-- 반올림
SELECT round(3.14159265358979,3);

# Q2. 문자 관련 함수
-- 아스키 코드값 얻기
SELECT ascii('a'), ascii('A'), ascii('0');

-- concat 메서드를 써보자.
SELECT concat('3번 유저의 이름은', user_name, '입니다.')
FROM ssafy_user
WHERE user_num = 3;

-- id의 길이가 6인 직원의 이름을 조회
SELECT *
FROM ssafy_user
WHERE length(user_id)=6;

-- 김싸피
SELECT length('김싸피');
SELECT length('🚗');
SELECT char_length('김싸피');

-- 문자열 변경
SELECT replace('Hello ssafy', 'ssafy', 'hyenem');

-- 문자열 인덱스
SELECT instr('hello ssafy', 'ssafy');
-- db에서는 인덱스가 1부터 시작


-- 모든 직원의 이름 3자리조회
SELECT substr(user_name, 1, 3)
FROM ssafy_user;

-- LPAD RPAD
SELECT lpad('SSAFY', 10, '*');
SELECT rpad('SSAFY', 10, '*');

-- REVERSE
SELECT reverse('거꾸로');

# Q3. 날짜 관련함수

-- 2초 더하기
SELECT addtime('2024-09-26 10:47:50', '10');

-- 날짜차이
SELECT datediff('2024-12-31', now());

-- 오늘은?
SELECT now();

# Q4. 트랜잭셕 사용해보기
-- 오토커밋 해제
SET autocommit = 0;

USE ssafy;
CREATE TABLE test_table(
	val VARCHAR(2)
);

START TRANSACTION;
INSERT INTO test_table VALUES ('S');
INSERT INTO test_table VALUES ('S');
INSERT INTO test_table VALUES ('A');
INSERT INTO test_table VALUES ('F');
INSERT INTO test_table VALUES ('Y');
INSERT INTO test_table VALUES ('A');
SELECT * FROM test_table;

COMMIT;
ROLLBACK;