# CSS
* Cascading Style Sheets : 폭포 -> 아래가 더 강해 그러니까 아래에서부터 적용된다고 생각하면됨
* 지금은 CSS3를 사용하고 있다.

## CSS를 사용하는 3가지 방법
### External Style Sheet : 외부 참조
* HTML 밖에 CSS를 만들고 HTML에서 불러오기 `<link>`
```
<!DOCTYPE>
<head> //meta data를 넣는 곳 -> 어딘가에서 정보를 가져올 때 여기에 넣기
    <link rel="stylesheet" type="text/css" href="style.scc"/>
</head>
<body>
</body>
```

### Internal Style Sheet : 내부 참조
* HTML 내부에 CSS을 공간 마련해놓기 `<style>`
```
<head>
    <style type="text/css">
        body { margin: 0; padding: 0; }
        p { color : red; }
    </style>
</head>
```    

### Inline Style
* 요소의 태그 안에 속성으로 추가하기
