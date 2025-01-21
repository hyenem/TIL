package com.ssafy.aop;

public class OuchException extends RuntimeException{
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	public void handleException() {
		System.out.println("병원이나 가자 😥( ´･･)ﾉ(._.`)");
	}
}
	