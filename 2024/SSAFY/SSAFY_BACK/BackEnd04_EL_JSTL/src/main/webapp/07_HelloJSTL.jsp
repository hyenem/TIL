<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>JSTL</title>
</head>
<body>
	<h2>c:out</h2>
	<c:out value="Hello JSTL1"></c:out><br>
	<c:out value="Hello JSTL2"/><br>
	
	<hr>
	<h2>c:set</h2>
	<c:set var="name" value="yang"/> ${name}<br>
	<c:set var="name2">yang2</c:set> ${name2}<br>
	
	<c:set var="person" value="<%=new com.ssafy.dto.Person() %>"/>
	<c:set target="${person}" property="name" value="yang3"/>
	${person}<br>
	
	
</body>
</html>