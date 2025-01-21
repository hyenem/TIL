const original = [
  {
    kor: '싸피',
    eng: 'SSAFY',
  },
  'SSAFY',
]

const copied = original.slice()

console.log(JSON.stringify(original) === JSON.stringify(copied)) // true

copied[0].kor = 'ㅆㅏㅍㅣ' // '싸피'를 'ㅆㅏㅍㅣ'로 변경
copied[1] = 'ssafy'     // 'SSAFY' 를 'ssafy'로 변경

console.log(JSON.stringify(original) === JSON.stringify(copied)) // false

console.log(original) // [ { kor: 'ㅆㅏㅍㅣ', eng: 'SSAFY' }, 'SSAFY' ]
console.log(copied)   // [ { kor: 'ㅆㅏㅍㅣ', eng: 'SSAFY' }, 'ssafy' ]

/* 얕은 복사 - reference
  copied[0].kor = 'ㅆㅏㅍㅣ'
  중첩구조를 갖고 있는 2차원 배열이라면 얕은 복사가 진행되서 
  original과 copied의 kor value가 모두 'ㅆㅏㅍㅣ' 로 변경됨
*/

/* 깊은 복사 - primitive
  copied[1] = 'ssafy' 
  1차원 배열의 원소값은 기본적으로 깊은 복사를 수행
  original 에는 `SSAFY`가 그대로 있고 copied의 값만 변경됨
*/
