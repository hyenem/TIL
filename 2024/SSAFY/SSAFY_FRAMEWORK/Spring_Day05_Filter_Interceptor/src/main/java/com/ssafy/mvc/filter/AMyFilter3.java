package com.ssafy.mvc.filter;

import java.io.IOException;

import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

import jakarta.servlet.Filter;
import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.ServletRequest;
import jakarta.servlet.ServletResponse;


////단점 : 경로를 지정할 수 없다.(모든 요청에 대해서 필터가 동작)
@Component
//@Order(3) //오더 어노테이션 통해서 순서지정 가능
//		  //숫자는 정수 범위면 가능(주로 양수를 사용)
//		  // 숫자가 낮을수록 먼저 동작
public class AMyFilter3 implements Filter {

	@Override
	public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
			throws IOException, ServletException {
		System.out.println("서블릿 전3");
		chain.doFilter(request, response);
		System.out.println("서블릿 후3");
	}

}
