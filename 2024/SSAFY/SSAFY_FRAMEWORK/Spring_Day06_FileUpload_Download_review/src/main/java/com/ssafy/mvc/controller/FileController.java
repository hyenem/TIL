package com.ssafy.mvc.controller;

import java.io.File;
import java.io.IOException;

import org.springframework.core.io.Resource;
import org.springframework.core.io.ResourceLoader;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;

@Controller
public class FileController {
	
	private ResourceLoader resourceLoader;
	private FileController(ResourceLoader resourceLoader) {
		this.resourceLoader = resourceLoader;
	}
	
	@GetMapping("/singleFileUploadForm")
	public String singleFileUploadForm() {
		return "singleFileUploadForm";
	}
	
	@PostMapping("/singleFileUpload")
	public String singlefileupload(@RequestParam("file") MultipartFile file, Model model) throws IllegalStateException, IOException {
		if(file!=null && file.getSize()>0) {
			String fileName = file.getOriginalFilename();
			Resource resource = resourceLoader.getResource("classpath:/static/img/");
			file.transferTo(new File(resource.getFile(), fileName));
			model.addAttribute("fileName", fileName);
		}
		return "result";
	}
	
	@GetMapping("/download")
	public String singlefiledownload(@RequestParam("fileName") String fileName, Model model) {
		model.addAttribute("fileName", fileName);
		return "fileDownloadView";
	}
}
