# git 필기

## commit/push 규칙
* 꼭! 항상! 절대! `add`, `commit` , `push`는 최상단 폴더(`init`한 곳)에서 작업하기

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