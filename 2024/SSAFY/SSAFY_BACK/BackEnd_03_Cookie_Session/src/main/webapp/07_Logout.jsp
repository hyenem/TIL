<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>로그아웃</title>
</head>
<body>
	<!-- 로그아웃하기 속성지우기, 세션자체 지우기 -->
	<%session.removeAttribute("id");%>
<%-- 	<%session.invalidate(); %> --%>

<!-- 유희!! -->
	<script>
		alert("로그아웃!")
		location.href="index.html"
	</script>
</body>
</html>