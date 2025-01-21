package com.ssafy.board.model.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

import com.ssafy.board.model.dto.Board;
import com.ssafy.board.util.DBUtil;

//싱글턴으로 관리
public class BoardDaoImpl implements BoardDao {

	private DBUtil util = DBUtil.getInstance();
	/////////////////////////////////////////
	private static BoardDao dao = new BoardDaoImpl();

	private BoardDaoImpl() {
	}

	public static BoardDao getInstance() {
		return dao;
	}
	///////////////////////

	@Override
	public List<Board> selectAll() {
		List<Board> list = new ArrayList<>();
		String sql = "SELECT * FROM board";
		Connection conn = null;
		Statement stmt = null;
		ResultSet rs = null;
		try {
			conn = util.getConnection();
			stmt = conn.createStatement();
			rs = stmt.executeQuery(sql);

			while (rs.next()) {
				Board board = new Board();
				board.setId(rs.getInt("id"));
				board.setWriter(rs.getString("writer"));
				board.setTitle(rs.getString("title"));
				board.setContent(rs.getString("content"));
				board.setViewCnt(rs.getInt("view_cnt"));
				board.setRegDate(rs.getString("reg_date"));
				list.add(board);
			}

		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			util.close(rs, stmt, conn);
		}

		return list;
	}

	@Override
	public Board selectOne(int id) {
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
//		String sql = "SELECT * FROM board WHERE id="+id; //이런식으로 작성하거나....
		String sql = "SELECT * FROM board WHERE id=?";
		Board board = null;
		try {
			conn = util.getConnection();
			pstmt = conn.prepareStatement(sql);

			pstmt.setInt(1, id); // 인덱스는 1부터 시작!
			rs = pstmt.executeQuery();
			board = new Board();
			while (rs.next()) {
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
		// 해당 id에 게시글 없어도... 껍데기를 만들어 두었다. 문법상 이슈는 없어서...
		return board;
	}

	@Override
	public void insertBoard(Board board) {
		Connection conn = null;
		PreparedStatement pstmt = null;

		// 생각보다 너무 불편해...
//		String sql = "INSERT INTO board (title, writer, content) VALUES('"+board.getTitle()+"'.....";
		String sql = "INSERT INTO board (title, writer, content) VALUES(?,?,?)";

		try {
			conn = util.getConnection();

//			conn.setAutoCommit(false);

			pstmt = conn.prepareStatement(sql);

			pstmt.setString(1, board.getTitle());
			pstmt.setString(2, board.getWriter());
			pstmt.setString(3, board.getContent());

			int result = pstmt.executeUpdate();

//			System.out.println(result);

//			conn.commit();
//			conn.rollback();

		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			util.close(pstmt, conn);
		}

	}

	@Override
	public void deleteBoard(int id) {
		Connection conn = null;
		PreparedStatement pstmt = null;

		String sql = "DELETE FROM board WHERE id=?";

		try {
			conn = util.getConnection();
			pstmt = conn.prepareStatement(sql);

			pstmt.setInt(1, id);
			int result = pstmt.executeUpdate();

		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			util.close(pstmt, conn);
		}
	}

	@Override
	public void updateBoard(Board board) {
		Connection conn = null;
		PreparedStatement pstmt = null;
		
		String sql = "UPDATE board SET title=?, content=? WHERE id=?";
		
		try {
			conn = util.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, board.getTitle());
			pstmt.setString(2, board.getContent());
			pstmt.setInt(3, board.getId());
				
			pstmt.executeUpdate();
			
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			util.close(conn, pstmt);
		}

	}

	@Override
	public void updateViewCnt(int id) {
		Connection conn = null;
		PreparedStatement pstmt = null;
		
		String sql = "UPDATE board SET view_cnt=view_cnt+1 WHERE id=?";
		
		try {
			conn = util.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setInt(1, id);
			pstmt.executeUpdate();
			
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			util.close(conn, pstmt);
		}

	}

}
