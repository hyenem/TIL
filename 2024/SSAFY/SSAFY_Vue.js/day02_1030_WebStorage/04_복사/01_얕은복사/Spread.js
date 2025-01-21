let info = { kor: '싸피' }
let newInfo = Object.assign({}, info)

newInfo.kor = 'ㅆㅏㅍㅣ'

console.log(info)             // { kor: '싸피' }
console.log(info === newInfo) // false
// assign()은 2차원 객체(중첩)의 깊은 복사가 안됨


// 전개 연산자 
info = {
  kor: '싸피',
  eng: {
    upper: 'ssafy',
  },
}

newInfo = { ...info }

newInfo.eng.upper = 'SSAFY'

console.log(info)    // { kor: '싸피' , eng: {upper: 'SSAFY'}}
console.log(newInfo) // { kor: '싸피' , eng: {upper: 'SSAFY'}}


console.log(info === newInfo) // false
console.log(info.eng.upper === newInfo.eng.upper) // true


