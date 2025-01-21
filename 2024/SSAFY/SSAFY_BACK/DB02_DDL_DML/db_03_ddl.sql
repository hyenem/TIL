# Q1. ssafy DB를 생성해보자.
CREATE DATABASE ssafy;

# Q2. DB 목록을 조회해보자.
SHOW DATABASES;

# Q3. ssafy DB를 사용해보자.
USE ssafy;

# Q4. ssafy DB를 삭제해보자.
DROP DATABASE IF EXISTS ssafy;

# Q5. 문자집합 설정해보자.
ALTER DATABASE ssafy
DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb3_general_ci;