package com.ssafy.mvc.model.service;

import java.util.List;

import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.ssafy.mvc.model.dao.BoardDao;
import com.ssafy.mvc.model.dto.Board;
import com.ssafy.mvc.model.dto.SearchCondition;

@Service
public class BoardServiceImpl implements BoardService{
	
	private final BoardDao boardDao;
	public BoardServiceImpl(BoardDao boardDao) {
		this.boardDao = boardDao;
	}
	
	@Override
	public List<Board> getBoardList() {
		System.out.println("모든 게시글 가지고 왔습니다.");
		return boardDao.selectAll();
	}

	@Override
	@Transactional
	public Board readBoard(int id) {
		System.out.println("글을 읽어옵니다.");
		boardDao.updateViewCnt(id);
		return boardDao.selectOne(id);
	}

	@Override
	@Transactional
	public void writeBoard(Board board) {
		System.out.println("게시글 작성 했습니다.");
		boardDao.insertBoard(board);
	}

	@Override
	@Transactional
	public void removeBoard(int id) {
		// TODO Auto-generated method stub
		
	}

	@Override
	@Transactional
	public void modifyBoard(Board board) {
		// TODO Auto-generated method stub
		
	}

	@Override
	@Transactional
	public List<Board> search(SearchCondition condition) {
		return boardDao.search(condition);
	}

}
