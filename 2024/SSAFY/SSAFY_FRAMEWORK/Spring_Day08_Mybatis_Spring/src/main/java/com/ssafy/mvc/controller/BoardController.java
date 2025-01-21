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
	
	@GetMapping("/delete")
	public String delete(@RequestParam("id") int id) {
		boardService.removeBoard(id);
		return "redirect:list";
	}
	
	@GetMapping("/updateform")
	public String updateform(@RequestParam("id") int id, Model model) {
		//게시글 하나 가지고와서 updateform으로 넘겨야된다.
		//지금은 readboard밖에 없어서,, 이걸로 하긴 하겠지만 이거하면 게시글 조회수 하나 올라감
		//그냥 생 게시글 하나 가져오는거 고민할 필요가 있다.
		Board board = boardService.readBoard(id);
		model.addAttribute("board", board);
		return "board/updateform";
	}
	
	@PostMapping("/update")
	public String update(@ModelAttribute Board board) {
		boardService.modifyBoard(board);
		return "redirect:detail?id="+board.getId();
	}
}
