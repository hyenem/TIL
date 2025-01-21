package com.ssafy.mvc.controller;

import org.springframework.core.io.ResourceLoader;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class FileController {

	
	@GetMapping("/download") // fileName이라고 했지만,, 실제론 fileId
	public String fileDownload(@RequestParam("fileName") String fileName, Model model) {
		model.addAttribute("fileName", fileName);
		return "fileDownloadView";
	}
}
