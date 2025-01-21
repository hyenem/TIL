package com.ssafy.mvc.config;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

import com.ssafy.mvc.interceptor.AInterceptor;
import com.ssafy.mvc.interceptor.BInterceptor;
import com.ssafy.mvc.interceptor.CInterceptor;
import com.ssafy.mvc.interceptor.loginInterceptor;

@Configuration
public class WebConfig implements WebMvcConfigurer{
	@Autowired
	private AInterceptor aInterceptor;
	@Autowired
	private BInterceptor bInterceptor;
	@Autowired
	private CInterceptor cInterceptor;
	
	@Autowired
	private loginInterceptor loginInterceptor;
	
	@Override
	public void addInterceptors(InterceptorRegistry registry) {
		registry.addInterceptor(loginInterceptor).addPathPatterns("/regist");
	}
}
