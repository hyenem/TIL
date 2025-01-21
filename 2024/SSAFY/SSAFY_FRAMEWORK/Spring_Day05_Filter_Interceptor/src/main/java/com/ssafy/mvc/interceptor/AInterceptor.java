package com.ssafy.mvc.interceptor;

import org.springframework.stereotype.Component;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.ModelAndView;

import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

//인터셉터는 HandlerInterceptor를 구현한 클래스
@Component
public class AInterceptor implements HandlerInterceptor {
	@Override
	public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler)
			throws Exception {
		//boolean 반환타입 /true 진행시켜 / false 고만훼
		System.out.println("A: pre");
		return true;
	}
	
	@Override
	public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler,
			ModelAndView modelAndView) throws Exception {
		// 정상적으로 수행이 됐다면 실행, 예외 발생시 미실행
		System.out.println("A: post");
	}
	
	@Override
	public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex)
			throws Exception {
		// view가 전달된 후 실행(무조건 실행) 예외 미발생시 ex=null/예외 발생시 해당 예외 객체
		System.out.println("A: after");
	}
}
