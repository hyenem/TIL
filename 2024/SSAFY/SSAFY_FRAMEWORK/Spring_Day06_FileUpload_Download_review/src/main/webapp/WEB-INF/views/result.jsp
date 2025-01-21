<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h2>${fileName}</h2><br>
	<a href="/img/${fileName}">${fileName}</a>
	<br>
	<img src="/img/${fileName}">
	<br>
	
	<a href="/download?fileName=${fileName}">파일 다운로드</a>
</body>
</html>