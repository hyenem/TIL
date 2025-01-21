<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>EL</title>
</head>
<body>
	<!-- URL에 쿼리시트링을 작성해서 봤다. -->
	<%=request.getParameter("id")%> <br>
	${param.id}<br>
	
	== : <%=request.getParameter("id") == "ssafy"%><br>
	equals() : <%=request.getParameter("id").equals("ssafy")%><br>
	
	==(EL) : ${param.id == "ssafy"} <br>
	equals() (EL) : ${param.id eq "ssafy"}
</body>
</html>