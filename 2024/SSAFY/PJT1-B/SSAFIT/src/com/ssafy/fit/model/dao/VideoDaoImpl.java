package com.ssafy.fit.model.dao;

import com.ssafy.fit.model.*;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import com.google.gson.Gson;

public class VideoDaoImpl implements VideoDao{
	private List<Video> list = new ArrayList<>();
	private static VideoDaoImpl instance = new VideoDaoImpl();
	private VideoDaoImpl() {}
	
	// Singleton 인스턴스를 반환하는 메소드
	public static VideoDaoImpl getInstance() {
		return instance;
	}
	
	
	// 비디오 목록 반환
	@Override
	public List<Video> selectVideo() {
		try {
			BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream("data/video.json")));
			String str = null;// 한줄씩 읽어오기 위한 임시 변수
			StringBuilder sb = new StringBuilder(); // 한줄씩 읽고 합쳐줘야함
			while ((str = br.readLine()) != null) {
				sb.append(str); // 한줄씩 이어붙이기
			}
			// 해당 while문을 빠져나오면 sb에는 모든 문자열이 저장되어있음
			Gson gson = new Gson();
			
			Video[] listArr = gson.fromJson(sb.toString(), Video[].class); // gson으로 json 파일 변환해서 받은 문자 Video 배열에 삽입
			
			for (Video video : listArr) {
				list.add(video); // Video 배열 내용 list에 추가
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		
		
		return list;
	}
	
	// 비디오 번호로 비디오 선택해서 반환
	@Override
	public Video selectVideoByNo(int no) {
			for (Video video : list) // 검색 할 Video List 가져오기
				if (video.getNo() == no) {// 리스트 내의 no와 검색 대상 no가 동일하면 해당 video 반환
					return video;
				}
		return null;
	}

}
