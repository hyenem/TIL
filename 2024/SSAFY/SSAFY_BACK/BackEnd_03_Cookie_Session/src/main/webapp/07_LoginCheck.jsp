<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	//화면을 보여줄건 아니야 그래서 HTML 코드는 필요없어
	
	String id = request.getParameter("id");
	String pw = request.getParameter("password");
	
	// id와 pw를 이용하여 실제 유저인지 확인을 해야한다.(DB를 배우고 나서야 명확하게 할 수 있다.)
	// 혹은 Manager라는 걸 통해서 유저 목록을 관리하면서 확인을 해볼 수 있다.
	
	//조건문을 통해서 확인하곗다. ㅠ (임시)
	//"ssafy".equals(id)가 더 안전 (null point exception)
	if(id.equals("ssafy") && pw.equals("1234")){
		//로그인 성공(어디에 저장?) -> session
		//JSP에서는 session이라는 기본객체가 이미 들어있어!
		session.setAttribute("id", id);
		//Servlet이었다면 session을 가져오는 방법은?
		//쿠키목록을 전부 가져와서 JSESSIONID라는 이름을 가진 쿠키가 있는지 확인하고
		//해당 쿠키를 이용하여 세션ID를 확보하고, 가지고 온다,,,
		HttpSession mySession = request.getSession();
		
		//Main.jsp 페이지 이동을 할건데,,,(리다이렉트-> id, password 보안 유지를 위해)
		//1. 포워딩
		request.getRequestDispatcher("08_Main.jsp").forward(request, response);
		//2. 리다이렉트
		response.sendRedirect("08_Main.jsp");
	} else {
		//로그인 실패
		response.sendRedirect("07_LoginForm.jsp");
	}
	
%>
