package com.ssafy.board.test;

import com.ssafy.board.model.dao.BoardDao;
import com.ssafy.board.model.dao.BoardDaoImpl;

public class Test {
	public static void main(String[] args) {
		BoardDao dao = BoardDaoImpl.getInstance();
		System.out.println(dao.selectOne(6));
	}
}
