package com.ssafy.mvc.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.ssafy.mvc.model.dto.Board;
import com.ssafy.mvc.model.dto.SearchCondition;
import com.ssafy.mvc.model.service.BoardService;

@Controller
public class BoardController {
	
	private final BoardService boardService;
	
	public BoardController(BoardService boardService) {
		this.boardService = boardService;
	}
	
	@GetMapping("/list")
	public String list(Model model) {
		//서비스를 통해서 게시글들을 가져와야한다.
		List<Board> boards = boardService.getBoardList();
		model.addAttribute("boards", boards);
		return "board/list";
	}
	
	@GetMapping("/writeform")
	public String writeform() {
		return "board/writeform";
	}
	
	@PostMapping("/write")
	public String write(@ModelAttribute Board board) {
		boardService.writeBoard(board);
		return "redirect:list";
	}
	
	@GetMapping("/detail")
	public String detail(@RequestParam("id") int id, Model model) {
		Board board = boardService.readBoard(id);
		model.addAttribute("board", board);
		return "board/detail";
	}
	
	@GetMapping("/search")
	public String serarch(@ModelAttribute SearchCondition condition, Model model) {
		model.addAttribute("boards", boardService.search(condition));
		return "/board/list";
	}
}
