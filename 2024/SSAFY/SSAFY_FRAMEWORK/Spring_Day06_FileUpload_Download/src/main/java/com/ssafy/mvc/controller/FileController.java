package com.ssafy.mvc.controller;

import java.io.File;
import java.io.IOException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.io.Resource;
import org.springframework.core.io.ResourceLoader;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;

@Controller
public class FileController {
	//스프링에서 파일이나 클래스 등 리소스를 로드할때는 resourceloader 인터페이스를 이용해서 가져온다.
	
	private ResourceLoader resourceLoader;
	
	private FileController(ResourceLoader resourceLoader) {
		this.resourceLoader = resourceLoader;
	}
	
	@GetMapping("/singleFileForm")
	public String singlefileform() {
		return "singleFileForm";
	}
	@GetMapping("/multiFileForm")
	public String multifileform() {
		return "multiFileForm";
	}
	
	@PostMapping("/singleFileUpload")
	public String sinlgefileupload(@RequestParam("file") MultipartFile file, Model model) throws IllegalStateException, IOException {
		//파일이 있는지... 검사
		if(file!=null && file.getSize()>0) {
			String fileName = file.getOriginalFilename();
			
			//코드로 저기 있는 img라고 하는 폴더를 가지고 와야겠다.
			Resource resource = resourceLoader.getResource("classpath:/static/img");
			
			file.transferTo(new File(resource.getFile(), fileName));
			
			model.addAttribute("fileName", fileName);
		}
		return "result";
	}
	@PostMapping("/multiFileUpload")
	public String multifileupload(@RequestParam("files") MultipartFile[] files, Model model) throws IllegalStateException, IOException {
		//파일이 있는지... 검사
		for(MultipartFile file : files) {
			System.out.println(file.getOriginalFilename());
		}
		return "result";
	}
	
	@GetMapping("/download")
	public String fileDownload(@RequestParam("fileName") String fileName, Model model) {
		model.addAttribute("fileName", fileName);
		return "fileDownloadView";
	}
}
