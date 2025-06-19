package com.haginhae;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.domain.EntityScan;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;

@SpringBootApplication(scanBasePackages = "com.haginhae")
@EntityScan(basePackages = "com.haginhae.entity")
@EnableJpaRepositories(basePackages = "com.haginhae.repository")

public class HaginhaeServerApplication {

	public static void main(String[] args) {
		SpringApplication.run(HaginhaeServerApplication.class, args);
		
	}

}
