package com.ssafy.filter;

import jakarta.servlet.Filter;
import jakarta.servlet.FilterChain;
import jakarta.servlet.FilterConfig;
import jakarta.servlet.ServletException;
import jakarta.servlet.ServletRequest;
import jakarta.servlet.ServletResponse;
import jakarta.servlet.annotation.WebFilter;
import jakarta.servlet.http.HttpFilter;
import java.io.IOException;


public class MyFilter1 extends HttpFilter implements Filter {
       
	private FilterConfig fConfig;
	
    public MyFilter1() {
    }

	public void destroy() {
	}

	public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
		System.out.println("서블릿 전1");
		String encoding = fConfig.getInitParameter("encoding");
		request.setCharacterEncoding(encoding);
		chain.doFilter(request, response);
		System.out.println("서블릿 후1");
	}

	public void init(FilterConfig fConfig) throws ServletException {
		this.fConfig = fConfig;
	}

}
