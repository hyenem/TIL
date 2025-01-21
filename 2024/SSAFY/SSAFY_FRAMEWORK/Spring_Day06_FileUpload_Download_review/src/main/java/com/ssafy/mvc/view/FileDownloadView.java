package com.ssafy.mvc.view;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.util.Map;

import org.springframework.core.io.Resource;
import org.springframework.core.io.ResourceLoader;
import org.springframework.util.FileCopyUtils;
import org.springframework.web.servlet.view.AbstractView;

import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

public class FileDownloadView extends AbstractView {
	
	private ResourceLoader resourceLoader;
	private FileDownloadView(ResourceLoader resourceLoader) {
		this.resourceLoader = resourceLoader;
	}
	
	
	@Override
	protected void renderMergedOutputModel(Map<String, Object> model, HttpServletRequest request,
			HttpServletResponse response) throws Exception {
		String fileName = (String)model.get("fileName");
		Resource resource = resourceLoader.getResource("classpath:/static/img");
		File file = new File(resource.getFile(), fileName);
		
		fileName = new String(fileName.getBytes("UTF-8"), "ISO-8859-1");
		response.addHeader("Content-Disposition", "");
		response.addHeader("Content-Transfer-Encodig", "binary");
		
		try(FileInputStream fis = new FileInputStream(file);
			OutputStream os = response.getOutputStream();){
			FileCopyUtils.copy(fis, os);
		}
		
	}

}
