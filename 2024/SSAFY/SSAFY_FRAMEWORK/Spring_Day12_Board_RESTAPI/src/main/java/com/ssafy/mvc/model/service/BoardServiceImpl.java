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
	public boolean removeBoard(int id) {
		System.out.println("게시글을 삭제합니다.");
		int result = boardDao.deleteBoard(id);
		System.out.println(result);
		
		return result>=1;
	}

	@Override
	@Transactional
	public void modifyBoard(Board board) {
		
		//실제로 수정하고 싶은 id를 가진 게시글을 일단 가지고 와서
		Board tmp = boardDao.selectOne(board.getId());
		if(board.getTitle()!=null) tmp.setTitle(board.getTitle());
		if(board.getContent()!=null) tmp.setContent(board.getContent());
		boardDao.updateBoard(tmp);
	}

	@Override
	@Transactional
	public List<Board> search(SearchCondition condition) {
		return boardDao.search(condition);
	}

}
