const createBtn = document.querySelector('#create') //등록버튼
const inputTag = document.querySelector('#todo') //입력 창
const ulTag = document.querySelector('#todo-list') //리스트
const btnDone = document.querySelector('#btn-done')
const btnNo = document.querySelector('#btn-no')
const btnAll = document.querySelector('#btn-all')

// 할 일이 1개만 있을까...?
let todoList


window.addEventListener('load', function () {
  todoList = localStorage.getItem('todoList')

  if (todoList !== null) {
    todoList = JSON.parse(todoList)
    for (let i = 0; i < todoList.length; i++) {
      createTodoItem(todoList[i])
    }
  } else {
    todoList = []
  }
})


const createTodo = () => {
  // 코드를 작성하세요.


}


const createTodoItem = (todoItem) => {
  // 코드를 작성하세요.


}



const removeTodo = (todo) => {
  // 코드를 작성하세요.


}


const getDoneList = () => {
  // 코드를 작성하세요.


}


const getNoList = () => {
  // 코드를 작성하세요.


}



createBtn.addEventListener('click', createTodo)


btnDone.addEventListener('click', () => {
    // 코드를 작성하세요.


})

btnNo.addEventListener('click', () => {
    // 코드를 작성하세요.


})

btnAll.addEventListener('click', () => {
    // 코드를 작성하세요.


})