package com.ssafy.board.test;

import java.util.List;

import org.apache.ibatis.session.SqlSession;

import com.ssafy.board.config.MyBatisConfig;
import com.ssafy.board.model.dao.BoardDao;
import com.ssafy.board.model.dto.Board;

public class Test {
	public static void main(String[] args) {

//		try(SqlSession session = MyBatisConfig.getFactory().openSession(true)){
//			BoardDao dao = session.getMapper(BoardDao.class);
//			Board board = dao.selectOne(1);
//			System.out.println(board);
//		}
//		try(SqlSession session = MyBatisConfig.getFactory().openSession(true)){
//			BoardDao dao = session.getMapper(BoardDao.class);
//			Board board = new Board("이제는 알아야해1", "양띵균", "싱글턴을 모르면... 이제는 곤란하다.");
//			dao.insertBoard(board);
//		}
//		try(SqlSession session = MyBatisConfig.getFactory().openSession(true)){
//			BoardDao dao = session.getMapper(BoardDao.class);
//			dao.deleteBoard(3);
//		}
//		try(SqlSession session = MyBatisConfig.getFactory().openSession(true)){
//			BoardDao dao = session.getMapper(BoardDao.class);
//			dao.updateViewCnt(2);
//		}
		try(SqlSession session = MyBatisConfig.getFactory().openSession(true)){
			BoardDao dao = session.getMapper(BoardDao.class);
			Board board = dao.selectOne(1);
			board.setTitle("이제는 곤란해-BackEnd01 Sevlet");
			dao.updateBoard(board);
		}
		
		try(SqlSession session = MyBatisConfig.getFactory().openSession(true)){
			List<Board> boards = session.selectList("com.ssafy.board.model.dao.BoardDao.selectAll");
			for(Board board:boards) {+
				
				System.out.println(board);
			}
		}
	}
}
