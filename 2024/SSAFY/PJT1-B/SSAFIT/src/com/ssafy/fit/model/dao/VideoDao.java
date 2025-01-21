package com.ssafy.fit.model.dao;

import com.ssafy.fit.model.*;

import java.io.IOException;
import java.util.List;

public interface VideoDao {
	
	List<Video> selectVideo() throws IOException; // 비디오 리스트 출력
	Video selectVideoByNo(int no);
	
}
