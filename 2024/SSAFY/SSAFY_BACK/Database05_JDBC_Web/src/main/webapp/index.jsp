<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%
	application.setAttribute("root", request.getContextPath());
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>SSAFY 게시판</title>
</head>
<body>
	<h2>Welcome SSAFY Board</h2>
	<a href="board?action=writeform">게시글 등록</a>
	<a href="board?action=list">게시글 목록</a>
	
	
	<!-- 게시글 목록(절대경로) -->
	<ul>
		<li><a href="/Database05_JDBC_Web/board?action=list">목록1</a></li>
		<li><a href="<%=request.getContextPath() %>/board?action=list">목록2</a></li>
		<li><a href="${pageContext.request.contextPath}/board?action=list">목록3</a></li>
		<li><a href="${root}/board?action=list">목록4</a></li>
	</ul>
</body>
</html>