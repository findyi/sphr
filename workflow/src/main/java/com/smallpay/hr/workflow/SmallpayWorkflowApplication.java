package com.smallpay.hr.workflow;

import org.activiti.engine.IdentityService;
import org.activiti.engine.identity.Group;
import org.activiti.engine.identity.User;
import org.springframework.beans.factory.InitializingBean;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class SmallpayWorkflowApplication {

	public static void main(String[] args) {
		SpringApplication.run(SmallpayWorkflowApplication.class, args);
	}
}