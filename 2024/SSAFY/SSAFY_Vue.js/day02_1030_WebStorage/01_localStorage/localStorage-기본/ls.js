//////// 페이지에 처음 들어왔을 때 
window.addEventListener("load", function () {
  let data = localStorage.getItem("data")
  if (data != null) {
    document.querySelector("#saved > li").innerText = JSON.parse(data)
  } else {
    document.querySelector('#saved > li').innerText = "저장된 내용이 없습니다."
  }
})




//////// 등록 #create 

// 1. 등록 버튼 선택(접근)


// 2. 등록 버튼에 클릭 이벤트 추가


// 2-a. input 태그  || input 아이디 선택 


// 2-b. input에서 가져온 value를 json문자열으로 바꾸기


// 2-c. localStorage에 "data" 이름으로 값 추가


// (중요) 2-d. input태그의 value값 초기화






//////// 조회 #read 
// 코드를 작성하세요.









//////// 삭제 #delete 
// 코드를 작성하세요.





