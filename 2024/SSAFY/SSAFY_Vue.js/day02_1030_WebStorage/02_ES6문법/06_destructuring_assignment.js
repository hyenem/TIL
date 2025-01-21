//구조 분해 할당
// let user = {
//   id: "ssafy",
//   name: "송창용",
//   age: 30,
// }

//ES6 이전
// let id = user.id
// let name = user.name
// let age = user.age

// console.log(`${id}님의 이름은 ${name} 이고, 나이는 ${age}살 입니다.`)

//ES6 이후
// let { id, name, age } = user
// console.log(`${id}님의 이름은 ${name} 이고, 나이는 ${age}살 입니다.`)

//함수 객체 리턴
// function getUser() {
//   return {
//     id: "ssafy",
//     name: "한도형",
//     age: 20,
//   }
// }

// let user = getUser()
// let id = user.id
// let name = user.name
// let age = user.age

// ES6
// let { id, name, age } = getUser()
// console.log(`${id}님의 이름은 ${name} 이고, 나이는 ${age}살 입니다.`)

// let member = {
//   id: "admin",
//   name: "관리자",
//   age: 50,
// }

// ES6 이전 직접 대입
// function showMember(member) {
//   console.log("showMember1")
//   console.log("아이디: ", member.id)
//   console.log("이름: ", member.name)
//   console.log("나이: ", member.age)
// }

// ES6 이후 destructuring_assign 적용
// function showMember2({ id, name, age }) {
//   console.log("showMember2")
//   console.log("아이디:", id)
//   console.log("이름:", name)
//   console.log("나이:", age)
// }

// showMember(member)
// showMember2(member)

// let arr = [1, 2, 3, 4]
// let [a, b, c] = arr
// console.log(a)
// console.log(b)
// console.log(c)
