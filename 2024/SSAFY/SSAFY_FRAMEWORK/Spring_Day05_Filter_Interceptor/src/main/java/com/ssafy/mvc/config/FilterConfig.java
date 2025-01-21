package com.ssafy.mvc.config;

import org.springframework.boot.web.servlet.FilterRegistrationBean;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import com.ssafy.mvc.filter.MyFilter;

import jakarta.servlet.FilterRegistration;

@Configuration
public class FilterConfig {
	@Bean
	public FilterRegistrationBean<MyFilter> myfilter(){
		FilterRegistrationBean<MyFilter> registrationBean = new FilterRegistrationBean<>();
		
		registrationBean.setFilter(new MyFilter()); // 어떤 필터를,,
		registrationBean.addUrlPatterns("/hello");  // 어떤 경로로,,
		registrationBean.setOrder(1);				// 어떤 순서로,,
		
		return registrationBean;
	}
}
