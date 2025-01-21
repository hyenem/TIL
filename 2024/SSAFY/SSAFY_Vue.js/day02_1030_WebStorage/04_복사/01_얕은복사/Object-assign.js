let info = { kor: '싸피' }
let newInfo = Object.assign({}, info)

newInfo.kor = 'ㅆㅏㅍㅣ'

console.log(info)             // { kor: '싸피' }
console.log(info === newInfo) // false

// assign()은 2차원 객체(중첩)의 깊은 복사가 안됨


// 해결 
info = {
  kor: '싸피',
  eng: {
    upper: 'ssafy',
  },
}

newInfo = Object.assign({}, info)

newInfo.eng.upper = 'SSAFY'

console.log(info)    // { kor: '싸피' , eng: {upper: 'SSAFY'}}
console.log(newInfo) // { kor: '싸피' , eng: {upper: 'SSAFY'}}


console.log(info === newInfo) // false
console.log(info.eng.upper === newInfo.eng.upper) // true

/*  
  info 내부에 있는 eng의 value인 {upper: 'ssafy'}도 결국 객체이기 때문에 얕은 복사 
  Object.assign() 메서드의 한계
*/

