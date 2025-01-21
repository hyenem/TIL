# Day4_SQL의 분류
## DML
* Data Manipulation Language : 데이터 조작 언어
* 데이터를 조작(선택, 삽입, 수정, 삭제)하는 데 사용하는 언어
* 사용하는 대상은 테이블의 행이다. 따라서 DML을 사용하기 위해서는 이전에 테이블이 정의되어 있어야 한다.
* `SELECT`, `INSERT`, `UPDATE`, `DELETE`이 여기에 해당한다.
* 또 트렌젝션을 발생시키는 SQL도 여기에 해당한다.
    * 트렌젝션일나 테이블의 데이터를 변겨할 때 실제 테이블에 완전히 적용하지 않고, 임시로 적용시키는 것을 말한다.

## DDL
* Data Definition Language : 데이터 정의 언어
* 데이터베이스 테이블, 뷰, 인덱스 등의 데이터베이스 개체를 생성/삭제/변경하는 역할을 한다.
* `CREATE`, `DROP`, `ALTER` 등이다.
* DDL은 트렌젝션을 발생시키지 않기 때문에 되돌림(ROLLBACK)이나 완전 적용(COMMIT)을 시킬 수 없다.

## DCL
* Data Control Language : 데이터 제어 언어
* 사용자에게 어떤 권한을 부여하거나 뺴앗을 때 주로 사용하는 구문이다.
* `GRANT`, `REVOKE`, `DENY`가 여기에 해당한다.