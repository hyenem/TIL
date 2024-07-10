# git 필기

## commit/push 규칙
* 꼭! 항상! 절대! `add`, `commit` , `push`는 최상단 폴더(`init`한 곳)에서 작업하기

## 내가 지금 사용하고 있는 컴퓨터에서 처음으로 깃 작업을 할 때 한 번 만 하면 되는 작업

### `git config`
* 계정 설정 및 추가
    * `git config --global user.name [나의 username]`
    * `git config --global user.email [나의 github 이메일]`
* 계정 확인
    * `git config --global user.name`
    * `git config --global user.email`
* 만약에 잘못 쓰면 코드 다시 쓰면 덮어쓰기 됨

## 처음으로 깃을 시작할 때 한 번 만 하면 되는 작업

### `git init`

### `git remote`
* `git remote add origin [나의 깃헙의 원격저장소(github) 레포주소]`
* `git remote add origin https://github.com/hyenem/TIL.git`
* `origin`은 별명 자리인데, 보통 통일해서 사용하므로 다른 별명으로 지정하면 합동 프로젝트에서 문제 발생. 무조건 `origin`으로 할것 

* `git remote -v` : 내가 등록한 원격 저장소 레포 주소 확인(view)

* `git remote remove origin` : 등록한 원격저장소 삭제

## working directory에 변동이 있을 때마다 하는 작업

### `git add`

### `git commit`

### `git push`

## 상태확인
### working directory에서
- `git status`
    - `add` 전/후

### staging area에서 (.git)
- `git status`
    - 추적이 되고 있는지만 확인 가능
- `git log`
    - commit 이후에만!!!
    - `git status --oneline`이라고 하면 한 줄로 간결하게 알려줌
    - 항상 내림차순
    * `HEAD`는 내가 바라보고 있는 branch를 의미함