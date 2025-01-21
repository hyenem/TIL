const createBtn = document.querySelector('#create') //등록버튼
const inputTag = document.querySelector('#todo') //입력 창
const ulTag = document.querySelector('#todo-list') //리스트
const btnDone = document.querySelector('#btn-done')
const btnNo = document.querySelector('#btn-no')
const btnAll = document.querySelector('#btn-all')

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
  const content = inputTag.value

  //값이 없다면 경고창
  if (!content.trim()) {
    alert('할일을 입력하세요~~')
  } else {
    const todoItem = {
      todo: content,
      done: false,
    }
    createTodoItem(todoItem)
    inputTag.value = '' //입력 초기화
    inputTag.focus()

    //로컬스토리지에 직접 저장을 하자
    todoList.push(todoItem)
    localStorage.setItem('todoList', JSON.stringify(todoList))
  }
}

const createTodoItem = (todoItem) => {
  //li 태그 생성 후 값 채우기
  const liTag = document.createElement('li')
  const spanTag = document.createElement('span')

  spanTag.innerText = todoItem.todo //todoItem이 가지고 있는 todo 넣기

  liTag.appendChild(spanTag)

  if (todoItem.done == false) {
    const delBtn = document.createElement('a')
    delBtn.classList.add('btn', 'btn-sm', 'btn-danger', 'mx-2')
    delBtn.innerText = 'x'
  
    delBtn.addEventListener('click', () => {
      removeTodo(todoItem.todo)
      delBtn.remove()
    })
    liTag.appendChild(delBtn)
  }else {
    const doneBtn = document.createElement('a')
    doneBtn.classList.add('btn', 'btn-sm', 'btn-success', 'mx-2', 'disabled'), 
    doneBtn.innerText = 'v'
    liTag.append(doneBtn)
  }
  
  ulTag.appendChild(liTag)
}


const removeTodo = (todo) => {
  todoList.forEach(function(aTodo){
    if(aTodo.todo == todo) {
      aTodo.done = true
    }
  })
  event.target.parentElement.classList.add('text-decoration-line-through')

  localStorage.setItem('todoList', JSON.stringify(todoList))
}

const getDoneList = () => {
  return todoList.filter((todoItem) => todoItem.done === true)
}

const getNoList = () => {
  return todoList.filter((todoItem) => todoItem.done === false)
}


createBtn.addEventListener('click', createTodo)

btnDone.addEventListener('click', () => {
  ulTag.innerHTML = null
  getDoneList().forEach(function(aTodo) {
    const li = document.createElement('li')
    li.append(aTodo.todo)
    ulTag.append(li)
  })
})

btnNo.addEventListener('click', () => {
  ulTag.innerHTML = null
  getNoList().forEach(function(aTodo) {
    const li = document.createElement('li')
    li.append(aTodo.todo)
    ulTag.append(li)
  })
})

btnAll.addEventListener('click', () => {
  ulTag.innerHTML = null
  todoList.forEach((todoItem) => {
    createTodoItem(todoItem)
  })
})