<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>상세페이지</title>
</head>
<body>
	<div>${board.title}</div>
	<div>${board.content}</div>
	
	<a href="board?action=delete&id=${board.id}">삭제</a>
	<a href="board?action=updateform&id=${board.id}">수정</a>
</body>
</html>