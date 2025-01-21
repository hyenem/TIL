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


public class MyFilter2 extends HttpFilter implements Filter {
       
	private FilterConfig fConfig;
	
    public MyFilter2() {
    }

	public void destroy() {
	}

	public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
		System.out.println("서블릿 전2");
		chain.doFilter(request, response);
		System.out.println("서블릿 후2");
	}

	public void init(FilterConfig fConfig) throws ServletException {
		this.fConfig = fConfig;
	}

}
