package com.ssafy.board.model.service;

import java.util.List;

import com.ssafy.board.model.dto.Board;
import com.ssafy.board.model.repository.BoardRepository;
import com.ssafy.board.model.repository.BoardRepositoryImpl;

public class BoardServiceImpl implements BoardService {
	
	private static BoardService service = new BoardServiceImpl();
	private BoardRepository repo = BoardRepositoryImpl.getInstacance();
	
	private BoardServiceImpl () {}
	public static BoardService getInstance() {
		return service;
	}
	
	@Override
	public List<Board> getList() {
		return repo.selectAll();
	}

	@Override
	public Board getBoard(int id) {
		repo.updateViewCnt(id);
		return repo.selectOne(id);
	}

	@Override
	public void writeBoard(Board board) {
		repo.insertBoard(board);
	}

	@Override
	public void modifyBoard(Board board) {
		repo.updateBoard(board);

	}

	@Override
	public void removeBoard(int id) {
		repo.deleteBoard(id);
	}

}
