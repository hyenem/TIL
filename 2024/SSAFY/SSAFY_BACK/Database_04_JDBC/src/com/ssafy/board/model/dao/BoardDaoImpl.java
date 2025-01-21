package com.ssafy.board.model.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.List;

import com.ssafy.board.model.dto.Board;
import com.ssafy.board.util.DBUtil;

public class BoardDaoImpl implements BoardDao {
	
	private DBUtil util = DBUtil.getInstance();
	
	private static BoardDao dao = new BoardDaoImpl();
	private BoardDaoImpl() {}
	public static BoardDao getInstance() {
		return dao;
	}
	
	@Override
	public List<Board> selectAll() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public Board selectOne(int id) {
		
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		Board board = null;
		
		try {
			conn = util.getConnection();
			
//			String sql = "SELECT * FROM board WHERE id="+id;
			String sql = "SELECT * FROM board WHERE id=?";
			pstmt = conn.prepareStatement(sql);
			
			pstmt.setInt(1, id);
			
			rs = pstmt.executeQuery();
			board = new Board();
			while(rs.next()) {
				board.setId(rs.getInt(1));
				board.setWriter(rs.getString(2));
				board.setTitle(rs.getString(3));
				board.setContent(rs.getString(4));
				board.setViewCnt(rs.getInt(5));
				board.setRegDate(rs.getString(6));
			}
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			util.close(rs, pstmt, conn);
		}
		return board;
	}

	@Override
	public void insertBoard(Board board) {
		// 이렇게 쓰면 너무 불편해
		// String sql = "INSERT INTO board (title, writer, content) VALUES('"+board.getTitle()+"'.....";
		 String sql = "INSERT INTO board (title, writer, content) VALUES(?,?,?)";
		
	}

	@Override
	public void deleteBoard(int id) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void updateBoard(Board board) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void updateViewCnt(int id) {
		// TODO Auto-generated method stub
		
	}

}
