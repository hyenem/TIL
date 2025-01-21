package com.ssafy.fit.ui;

import com.ssafy.fit.util.*;
import com.ssafy.fit.model.*;
import com.ssafy.fit.model.dao.VideoDaoImpl;
import com.ssafy.fit.model.dao.VideoReviewDaoImpl;


import java.io.IOException;
import java.util.List;

public class VideoUi {
	private VideoDaoImpl videoDao = VideoDaoImpl.getInstance();
	private static VideoUi instance = new VideoUi();
	
	private VideoUi() {}
	
	// Singleton 인스턴스 반환
	public static VideoUi getInstance() {
		return instance;
	}
	
	SsafitUtil util = new SsafitUtil();
	MainUi main = new MainUi();
	VideoReviewUi vreview = VideoReviewUi.getInstance();
	VideoReviewDaoImpl vrimpl = VideoReviewDaoImpl.getInstance();
	List<Video> videos = videoDao.selectVideo();
	
	
	public void service() {
		
		util.printLine('-', 30);
		System.out.println("전 체  " + videos.size() + "개");
		util.printLine('-', 30);
		listVideo();
	}
	
	public void listVideo() {
				
		for(Video v : videos) {
			System.out.println(v.getNo() + "  " + v.getPart() + "  " + v.getTitle());
		}
		util.printLine('-', 30);
		System.out.println("1. 영상상세");
		System.out.println("0. 이전으로");
		int selection = util.inputInt("실행할 메뉴를 선택해주세요. : ");
		if(selection == 1) {
			int num = util.inputInt("상세 확인 할 영상 번호를 선택해주세요. : ");
			detailVideo(num);
		} else if (selection == 0) {
			main.service();
		}
		util.printLine('-', 30);
	}
	

    public void detailVideo(int num) { // 입력받은 숫자에 따라 영상 상세로 이동
        Video video = videoDao.selectVideoByNo(num);
        if (video != null) {
            util.printLine('-', 30);
            System.out.println("번호 : " + video.getNo());
            System.out.println("제목 : " + video.getTitle());
            System.out.println("운동 : " + video.getPart());
            System.out.println("영상 URL : " + video.getUrl());
            util.printLine('-', 30);
            util.printLine('-', 30);
            List<VideoReview> review = vrimpl.selectReview(num); //리뷰리스트 가져오기
            System.out.println("영상리뷰 : " + review.size());
            util.printLine('-', 30);
            for (VideoReview v : review) {
                System.out.println(v.getReviewNo() + "  " + v.getNickName() + "  " + v.getContent());
            }
            util.printLine('-', 30);
            System.out.println("1. 리뷰등록");
            System.out.println("0. 이전으로");
            util.printLine('-', 30);
            int selection = util.inputInt("실행할 메뉴를 선택해주세요. : ");
            if (selection == 1) {
        		VideoReviewUi reviewUi = VideoReviewUi.getInstance();
        		reviewUi.service(num);
            } else if (selection == 0) {
                service();
            }
        } else {
            System.out.println("해당 번호의 영상이 없습니다.");
            return;
        }
    }
}
}
