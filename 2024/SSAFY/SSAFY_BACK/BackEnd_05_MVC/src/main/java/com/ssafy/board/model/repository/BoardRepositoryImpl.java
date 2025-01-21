package com.ssafy.board.model.repository;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.ssafy.board.model.dto.Board;

public class BoardRepositoryImpl implements BoardRepository {
	
	private static BoardRepository repo = new BoardRepositoryImpl();
	
	private List<Board> list = new ArrayList<>();
	private Map<Integer, Board> boards = new HashMap<>();
	
	private BoardRepositoryImpl() {
		boards.put(1, new Board("SSAFY 완벽가이드", "양띵균", "1학기를 잘 이수하는 방법은,,,"));
	}
	
	public static BoardRepository getInstacance() {
		return repo;
	}
	@Override
	public List<Board> selectAll() {
//		return (List<Board>)boards.values();
//		return list;
		List<Board> tmp = new ArrayList<>();
		for(int i : boards.keySet()) {
			tmp.add(boards.get(i));
		}
		return tmp;
	}

	@Override
	public Board selectOne(int id) {
		//리스트였으면 반복문 돌면서 찾고
		return boards.get(id);
	}

	@Override
	public void insertBoard(Board board) {
		boards.put(board.getId(), board); //ID를 키로해서 맵으로 관리
		list.add(board); //리스트로 목록을 관리
	}

	@Override
	public void updateBoard(Board board) {
		boards.put(board.getId(), board);
	}

	@Override
	public void deleteBoard(int id) {
		boards.remove(id);
		
	}

	@Override
	public void updateViewCnt(int id) {
		Board b = boards.get(id);
		b.setViewCnt(b.getViewCnt()+1);
		
	}

}
