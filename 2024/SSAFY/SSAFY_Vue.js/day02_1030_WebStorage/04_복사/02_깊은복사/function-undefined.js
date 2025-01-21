const info = {
  kor: '싸피',
  year: {
    classOf: 2019,
  },
  myFunc: function() {
    console.log('?')
  }
}

const newInfo = JSON.parse(JSON.stringify(info))

console.log(newInfo.myFunc) // undefined

