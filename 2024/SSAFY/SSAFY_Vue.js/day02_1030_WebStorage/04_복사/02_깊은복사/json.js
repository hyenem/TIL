const info = {
  kor: '싸피',
  year: {
    classOf: 2019,
  },
}

const newInfo = JSON.parse(JSON.stringify(info))

newInfo.year.classOf = 2024

console.log(info) // { kor: '싸피', year: { classOf: 2019 } }
console.log(newInfo) // { kor: '싸피', year: { classOf: 2024 } }
console.log(info.year.classOf === newInfo.year.classOf) // 2019 === 2024 false