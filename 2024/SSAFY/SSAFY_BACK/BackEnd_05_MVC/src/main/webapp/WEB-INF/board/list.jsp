<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>게시글 목록</title>
</head>
<body>
	<table>
		<tr>
			<th>ID</th>
			<th>제목</th>
			<th>쓰니</th>
			<th>조회수</th>
			<th>등록일</th>
		</tr>
		<c:forEach items="${list}" var="board">
			<tr>
				<td>${board.id}</td>
				<td><a href="board?action=detail&id=${board.id}">${board.title }</a></td>
				<td>${board.writer }</td>
				<td>${board.viewCnt }</td>
				<td>${board.regDate }</td>
			</tr>
		</c:forEach>
	</table>
</body>
</html>