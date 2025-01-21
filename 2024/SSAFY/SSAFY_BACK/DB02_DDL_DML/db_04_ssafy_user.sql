# Q1. ssafydb 데이터 베이스 생성 및 사용
CREATE DATABASE IF NOT EXISTS ssafy_db;
USE ssafy_db;

# Q2. ssafy_user 테이블 생성
CREATE TABLE ssafy_user (
	user_num INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(20) NOT NULL,
    user_name VARCHAR(20) NOT NULL,
    user_password VARCHAR(20) NOT NULL,
    user_email VARCHAR(30),
    signup_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

# Q3. INSERT 쿼리를 사용해보자.
-- 모든 칼럼을 입력하겠다.
INSERT INTO ssafy_user
VALUES (4, 'hyenem', '김혜민', '1234', 'gpals0429@naver.com', now());
SELECT * FROM ssafy_user;

-- 원하는 칼럼만 작성 (데이터타입이 다를 수 있으므로 맞춰서 작성)
INSERT INTO ssafy_user (user_id, user_name, user_password)
VALUES ("gpals0429", "혜민", "1234"),
	("gpals0429", "혜민", "123412"),
    ("gpals0429", "혜민", "1234123"),
    ("gpals0429", "혜민", "1234124");
SELECT * FROM ssafy_user;

# Q4. 데이터를 수정해보자
UPDATE ssafy_user
SET user_name = 'anonymous';

UPDATE ssafy_user
SET user_password = 'ssafy'
WHERE user_num = 1;

# Q5. 데이터를 삭제해보자
DELETE FROM ssafy_user
WHERE user_num = 14;

