package com.ssafy.mvc.model.service;

import java.io.File;
import java.io.IOException;
import java.util.List;
import java.util.UUID;

import org.springframework.core.io.Resource;
import org.springframework.core.io.ResourceLoader;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.multipart.MultipartFile;

import com.ssafy.mvc.model.dao.BoardDao;
import com.ssafy.mvc.model.dto.Board;
import com.ssafy.mvc.model.dto.SearchCondition;

@Service
public class BoardServiceImpl implements BoardService{
	
	private final BoardDao boardDao;
	private final ResourceLoader resourceLoader;
	
	public BoardServiceImpl(BoardDao boardDao, ResourceLoader resourceLoader) {
		this.boardDao = boardDao;
		this.resourceLoader = resourceLoader;
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

	@Override
	public void fileUpload(MultipartFile file, Board board) {
		if(file!=null && file.getSize()>0) {
			try {
				String fileName = file.getOriginalFilename(); //실제 파일 이름
				//확장자를 따로 저장하는 그런 처리가 사실은 필요하다
				String fileId = UUID.randomUUID().toString(); //고유한 이름(확장자 날아가요)
				// 게시글 바구니를 확장시켜서 파일 정보도 저장을 해보자~
				board.setFileId(fileId);
				board.setFileName(fileName);
				
				//어디다가 저장을 할래
				Resource resource = resourceLoader.getResource("classpath:/static/img");
				file.transferTo(new File(resource.getFile(), fileId));
				//////////////////////////////////// 위의 코드까지 정상 수행이 되면,,,
				boardDao.insertBoard(board);
				boardDao.insertFile(board);
			} catch (IllegalStateException e) {
				e.printStackTrace();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}

}
