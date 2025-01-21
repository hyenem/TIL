<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h2>등록하는 화면</h2>
	<c:if test="${not empty loginUser}">
		<span>${loginUser }님 반갑습니다.</span>
		<a href="/logout">로그아웃</a>
	</c:if>
</body>
</html>