# Mac에 brew로 mySQL 설치하기
1. 브루에 프로그램 있는지 검색하기
    ```
    brew search mysql
    ```
    검색해보니까 cask가 아니라 공식적으로 mysql을 제공해주고 있다.
2. sql 설치하기
    ```
    brew install mysql
    ```
3. mysql 서버 실행하기
    ```
    mysql.server start
    ```
4. mysql 서버 설정하기
    ```
    mysql_secure_installation
    ```
    요거 입력하면 보안 설정 어떻게 할지 물어본다! 그냥 영어 잘 읽고 내가 원하는 것 고르면 되는데, 나는 이렇게 했다.
    ```
    Would you like to setup VALIDATE PASSWORD component? : y
    // 검증된 비밀번호 설정 할거냐? 복잡한 비밀번호 제한 걸거냐는 의미
    // 나는 안전한게 더 좋지 않을까 해서 yes함.

    There ar three levels of password validation policy:
    LOW Length >= 8
    MEDIUM Length >= 8, numeric, mixed case, and special characters
    STRONG Length >= 8, numeric, mixed case, special charcters and dictionary
    0=LOW, 1=MEDIUM, 2= STRING : 2
    // 비밀번호 제한 얼마나 까다롭게 할거냐는 뜻
    // 나는 그냥 가장 강하게 STRONG으로 함.

    New password:
    Re-enter new password:
    // 비밀번호 두 번 쳐주면 됨.

    Do you wish to continue with the password provided? : y
    // 진짜 그 비밀번호 쓸거냐는 뜻.

    Remove anonymous user? : y
    // 익명의 사용자를 제거할거냐는 뜻
    // 내 로컬에서 익명의 사용자가 없을 것 같아서 yes힘

    Disallow root login remotely? : y
    // 루트 사용자의 원격 접속을 불허하겠냐는 뜻
    // 이것도 불허하는게 보안에 더 좋을 것 같아서 yes함

    Remove test database and access to it? : y
    // 테스트 데이터 베이스를 지울거냐는 뜻
    // 테스트 데이터 베이스 왠지 필요 없을 것 같아서 yes 함

    Reload privilege tables now? : y
    // 변경된 권한 리로드 할거냐는 뜻
    ```
    다 해놓고 보니까 그냥 뭐 YES girl 이지만,,,

5. mysql에 접속하기
    ```
    mysql -uroot -p
    ```



# Mac에 brew로 mySQL workbench 설치하기
1. brew에서 프로그램 찾아보기
    ```
    brew search mysqlworkbench
    ```
    결과로 cask에 mysqlworkbench가 있었다.
2. brew로 설치하기
    ```
    brew install --cask mysqlworkbench
    ```
얘는 따로 설정해줄게 없어서 간~단하게 끝!!!


# 부수적인 것들
나는 다운 안받았는데,, 어떤 블로그에서 이것도 받으라고 해서 뭔진 모르겠지만 다운받은 것들이 있다. 순서가 중요할수도있는데,, 그냥 일단 제일 마지막에 다운받음,,,ㅋㅋㅋ,,,,, 괜찮은걸까,,,
openssl과 mysql-client

openssl은 뭔가 암호화와 관련이 되어 있는 것 같다. // 이건 이미 다운받아져 있단다. 왜지?
mysql-client 는 웹 어플리케이션이 아니라 VM에서 바로 DB로 접속해야할 경우에 사용한다고 한다,, 잘 몰르겠다,, 그냥 그러려니 하기로했다. 전에 성태오빠가 얘기했던 적이 있던것 같다. 그러려니하고 넘어가는 것도 필요하다고.