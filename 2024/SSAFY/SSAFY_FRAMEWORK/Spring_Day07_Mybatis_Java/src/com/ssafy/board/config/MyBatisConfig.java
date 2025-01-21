package com.ssafy.board.config;

import java.io.IOException;
import java.io.InputStream;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

public class MyBatisConfig {
	//공장을 세워서 쓰기 위함이다.....
	private static SqlSessionFactory factory;
	
	static {
		//공장을 세워야하는데 그 자원(설정파일) 위치
		String resource = "mybatis-config.xml";
		try(InputStream inputStream = Resources.getResourceAsStream(resource)){
			factory=new SqlSessionFactoryBuilder().build(inputStream);
			System.out.println("공장 건설 완료");
		} catch (IOException e) {
			System.out.println("공장 건설 실패");
		}
	}
	
	public static SqlSessionFactory getFactory() {
		return factory;
	}
	
}
