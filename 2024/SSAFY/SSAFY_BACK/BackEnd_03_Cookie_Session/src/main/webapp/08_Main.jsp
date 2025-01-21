<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>메인화면</title>
</head>
<body>
	<%
		if(session.getAttribute("id")==null){
			response.sendRedirect("07_LoginForm.jsp");			
		} else { %>
			<%=session.getAttribute("id") %>
			<a href="07_Logout.jsp">로그아웃</a>
			<%
		}
	%>
</body>
</html>