# MySQL 처음 시작해보기
## 새로운 데이터 배이스 만들기
* 새로운 데이터 베이스 만들기는 MySQL Workbench가 아니라 터미널에서 MySQL을 실행해서 할 수 있다.
* 우선 MySQL을 실행해보자.
    ```
    mysql -u root -p
    ```
* 'testdb'를 생성하고, 잘 생성되었는지 확인해보자.
    ```sql
    CREATE DATABASE testdb;

    SHOW DATABASES;
    ```

## 사용자를 생성하고 권한 부여하기
* 루트 사용자 외에 새로운 사용자를 만들어서 접근할 수 있도록 만들어보자.
    ```sql
    CREATE USER 'hyenem'@'localhost' IDENTIFIED BY 'password';
    ```
* 이제 만든 사용자에게 권한을 부여해보자.
    ```sql
    GRANT ALL ON *.* TO 'hyenem'@'localhost';
    ```
    위의 내용은 모든 모든 데이터베이스의 모든 테이블에 대한 모든 권한을 부여한다는 뜻이다. 정확한 양식은 어떻게 되냐면
    ```sql
    GRANT [권한] ON [database명].[table명] TO [user명]@[server명];
    ```
    이다. [권한] 자리에는 `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`, `INDEX`, `ALTER` 등이 들어갈 수 있다.
* 새로 부여된 권한을 로드해보자.
    ```sql
    FLUSH PRIVILEGES;
    ```
* 유저가 잘 생성되었는지 확인해보려면 아래 명령어를 입력하면 된다.
    ```sql
    SELECT USER, Host FROM mysql.user;
    ```

## MySQL workbench에서 실행해보기
* workbench 연 뒤에 MySQL Connection 에 있는 + 버튼을 누른다.
* Connection Name에 데이터베이스 이름 입력 : testdb
* Username에 접근하고자 하는 계정 입력 : hyenem
* 이후 Schemas탭에 들어가보면 생성된 데이터 베이스 구조를 확인할 수 있다.