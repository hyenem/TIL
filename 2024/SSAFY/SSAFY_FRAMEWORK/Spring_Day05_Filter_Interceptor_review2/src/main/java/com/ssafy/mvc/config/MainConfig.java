package com.ssafy.mvc.config;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.web.servlet.FilterRegistrationBean;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import com.ssafy.mvc.filter.AMyFilter;
import com.ssafy.mvc.filter.MyFilter1;
import com.ssafy.mvc.filter.MyFilter2;

@Configuration
public class MainConfig {

	@Autowired
	MyFilter1 myfilter1;
	@Autowired
	MyFilter2 myfilter2;
	@Autowired
	AMyFilter amyfilter;
	
	@Bean
	public FilterRegistrationBean<MyFilter1> myfilter1(){
		FilterRegistrationBean<MyFilter1> registrationBean = new FilterRegistrationBean<>();
		registrationBean.setFilter(myfilter1);
		registrationBean.addUrlPatterns("/*");
		registrationBean.setOrder(1);
		
		return registrationBean;
	}
	@Bean
	public FilterRegistrationBean<MyFilter2> myfilter2(){
		FilterRegistrationBean<MyFilter2> registrationBean = new FilterRegistrationBean<>();
		registrationBean.setFilter(myfilter2);
		registrationBean.addUrlPatterns("/*");
		registrationBean.setOrder(2);
		
		return registrationBean;
	}
	@Bean
	public FilterRegistrationBean<AMyFilter> amyfilter(){
		FilterRegistrationBean<AMyFilter> registrationBean = new FilterRegistrationBean<>();
		registrationBean.setFilter(amyfilter);
		registrationBean.addUrlPatterns("/*");
		registrationBean.setOrder(3);
		
		return registrationBean;
	}
}
