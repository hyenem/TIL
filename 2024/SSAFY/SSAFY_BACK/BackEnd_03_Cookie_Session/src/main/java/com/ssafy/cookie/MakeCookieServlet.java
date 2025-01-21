package com.ssafy.cookie;

import java.io.IOException;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@WebServlet("/make")
public class MakeCookieServlet extends HttpServlet{

	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		String key = req.getParameter("key");
		String value = req.getParameter("value");
		System.out.println(key);
		
		//쿠키를 생성해보자
		Cookie cookie = new Cookie(key, value);
		
		//유효시간 결정 : 초단위
		cookie.setMaxAge(60);
		
		//쿠키를 삭제하고 싶다.
//		cookie.setMaxAge(0);
		
		resp.addCookie(cookie);
		resp.sendRedirect(req.getContextPath()+"/02_CookieResult.jsp");
	}
	
	//쿠키를 삭제하는 예시
	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		String name = req.getParameter("name");
		for(Cookie c : req.getCookies()) {
			c.setMaxAge(0);
		}
	}
}
