package com.ssafy.jdbc.test;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

import com.ssafy.board.model.dto.Board;

public class JdbcTest {
	public JdbcTest() {
		try {
			Class.forName("com.mysql.cj.jdbc.Driver");
			System.out.println("드라이버 로딩 성공!");
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
	}
	
	public static void main(String[] args) {
		JdbcTest db = new JdbcTest();
		for(Board b : db.selectAll()) {
			System.out.println(b);
		}
	}
	
	private List<Board> selectAll(){
		List<Board> list = new ArrayList<>();
		try {
			Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/ssafy_board?serverTimezone=UTC", "ssafy", "ssafy");
			Statement stmt = conn.createStatement();
			String sql = "SELECT * FROM board";
			ResultSet rs = stmt.executeQuery(sql);
			while(rs.next()) {
				Board board = new Board();
				board.setId(rs.getInt("id"));
//				board.setId(rs.getInt(1));
				board.setWriter(rs.getString("writer"));
				board.setTitle(rs.getString("title"));
				board.setContent(rs.getString("content"));
				board.setViewCnt(rs.getInt("view_cnt"));
				board.setRegDate(rs.getString("reg_date"));
				list.add(board);
			}
			rs.close();
			stmt.close();
			conn.close();
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return list;
	}
}
