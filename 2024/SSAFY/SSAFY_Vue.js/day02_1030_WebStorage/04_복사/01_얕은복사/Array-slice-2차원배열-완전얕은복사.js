const original = [
  [0, 0, 0, 0],
  [1, 1, 1, 1],
  [2, 2, 2, 2],
]

const copied = original.slice()

console.log(JSON.stringify(original) === JSON.stringify(copied)) // true

copied[0][0] = 'SSAFY' // copied의 [0][0] 값 0을 11 변경
copied[2].push('싸피') // cpied의 [2]에 7번 값을 맨 뒤에 추가

console.log(JSON.stringify(original) === JSON.stringify(copied)) // true

console.log(original) // [ [ 'SSAFY', 0, 0, 0 ], [ 1, 1, 1, 1 ], [ 2, 2, 2, 2, '싸피' ] ]
console.log(copied)   // [ [ 'SSAFY', 0, 0, 0 ], [ 1, 1, 1, 1 ], [ 2, 2, 2, 2, '싸피' ] ]


// 중첩구조를 갖고 있는 2차원 배열이라면 얕은 복사
