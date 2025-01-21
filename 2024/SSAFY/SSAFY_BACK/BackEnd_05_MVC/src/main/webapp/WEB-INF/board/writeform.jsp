<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>게시글 등록</title>
</head>
<body>
	<h2>게시글 등록</h2>
	<form action = "board" method="POST">
		<input type="hidden" name="action" value="write">
		
		<label for="title">글 제목</label>
		<input type="text" id = "title" name="title">
		
		<label for="writer">글쓴이</label>
		<input type="text" id="writer" name="writer" value="익명">
		
		<label for="content">글 내용</label>
		<textarea rows="10" cols="30" name="content"></textarea>
		
		<input type="submit">
	</form>
</body>
</html>