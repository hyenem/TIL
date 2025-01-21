package com.ssafy.board.controlboard;

import java.io.IOException;
import java.util.List;

import com.ssafy.board.model.dto.Board;
import com.ssafy.board.model.service.BoardService;
import com.ssafy.board.model.service.BoardServiceImpl;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@WebServlet("/board")
public class BoardController extends HttpServlet{

	private static final long serialVersionUID = 1L;

	private BoardService service = BoardServiceImpl.getInstance();
	private final String prefix = "/WEB-INF/board/";


	@Override
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String action = request.getParameter("action");

		switch(action) {
		case "writeform":
			doWrtieForm(request, response);
			break;
		case "write" :
			doWrite(request, response);
			break;
		case "list":
			doList(request, response);
			break;
		case "detail":
			doDetail(request, response);
			break;
		case "delete":
			doRemove(request, response);
			break;
		case "updateform":
			doUpdateForm(request, response);
			break;
		case "update":
			doUpdate(request, response);
			break;
		default:
			System.out.println("에러페이지로 가라");
			break;
		}
			
	}

	private void doUpdate(HttpServletRequest request, HttpServletResponse response) throws IOException {
		int id = Integer.parseInt(request.getParameter("id"));
		Board board= service.getBoard(id);
		board.setTitle(request.getParameter("title"));
		board.setContent(request.getParameter("content"));
		
		service.modifyBoard(board);
		response.sendRedirect("board?action=list");
		
	}

	private void doUpdateForm(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		int id = Integer.parseInt(request.getParameter("id"));
		Board board = service.getBoard(id);
		request.setAttribute("board", board);
		request.getRequestDispatcher(prefix+"updateform.jsp").forward(request, response);
		
	}

	private void doRemove(HttpServletRequest request, HttpServletResponse response) throws IOException {
		int id = Integer.parseInt(request.getParameter("id"));
		service.removeBoard(id);
		response.sendRedirect("board?action=list");
	}

	private void doDetail(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		int id = Integer.parseInt(request.getParameter("id"));
		
		request.setAttribute("board", service.getBoard(id));

		request.getRequestDispatcher(prefix+"detail.jsp").forward(request, response);
		
	}

	private void doList(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setAttribute("list", service.getList());
		request.getRequestDispatcher(prefix+"list.jsp").forward(request, response);
	}

	private void doWrite(HttpServletRequest request, HttpServletResponse response) throws IOException {
		String title = request.getParameter("title");
		String writer = request.getParameter("writer");
		String content = request.getParameter("content");

		Board board = new Board(title, writer, content);
		
		service.writeBoard(board);
		response.sendRedirect("board?action=list");
	}

	private void doWrtieForm(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.getRequestDispatcher(prefix+"writeform.jsp").forward(request, response);

	}

}
