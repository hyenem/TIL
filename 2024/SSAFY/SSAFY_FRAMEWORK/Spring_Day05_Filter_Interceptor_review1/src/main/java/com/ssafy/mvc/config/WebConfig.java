package com.ssafy.mvc.config;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.InterceptorRegistration;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

import com.ssafy.mvc.interceptor.AInterceptor;
import com.ssafy.mvc.interceptor.BInterceptor;
import com.ssafy.mvc.interceptor.CInterceptor;
import com.ssafy.mvc.interceptor.UserInterceptor;

@Configuration
public class WebConfig implements WebMvcConfigurer{
	
//	@Autowired
//	private AInterceptor aInterceptor;
//	@Autowired
//	private BInterceptor bInterceptor;
//	@Autowired
//	private CInterceptor cInterceptor;
	
	@Autowired
	private UserInterceptor userInterceptor;
	
	@Override
	public void addInterceptors(InterceptorRegistry registry) {
//		registry.addInterceptor(aInterceptor).addPathPatterns("/hello");
//		registry.addInterceptor(bInterceptor).addPathPatterns("/hello");
//		registry.addInterceptor(cInterceptor).addPathPatterns("/hello");
		
		registry.addInterceptor(userInterceptor).addPathPatterns("/regist");
	}
}
