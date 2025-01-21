package com.ssafy.fit.ui;

import com.ssafy.fit.model.VideoReview;
import com.ssafy.fit.model.dao.UserManagerImpl;
import com.ssafy.fit.model.dao.VideoReviewDao;
import com.ssafy.fit.model.dao.VideoReviewDaoImpl;
import com.ssafy.fit.util.SsafitUtil;

public class VideoReviewUi {
    private VideoReviewDao videoReviewDao;
    private static VideoReviewUi instance;

    private SsafitUtil util = new SsafitUtil();

    private VideoReviewUi() {
        videoReviewDao = VideoReviewDaoImpl.getInstance();
    }

    public static VideoReviewUi getInstance() {
        if (instance == null) {
            instance = new VideoReviewUi();
        }
        return instance;
    }

    public void service(int videoNo) {
        while (true) {
            System.out.println("-----------------리뷰 메뉴----------------");
            System.out.println("1. 리뷰 보기");
            System.out.println("2. 리뷰 등록하기");
            System.out.println("3. 종료");
            System.out.println("---------------------------------------");
            int menu = util.inputInt("메뉴를 선택하세요: ");
            switch (menu) {
                case 1:
                    listReview(videoNo);
                    return;
                case 2:
                    registReview(videoNo);
                    return;
                case 3:
                	UserManagerImpl usermanager = UserManagerImpl.getInstance();
                	usermanager.saveUserData();
                    System.out.println("프로그램을 종료합니다.");
                    return;
                default:
                    System.out.println("잘못된 선택입니다. 다시 시도하세요.");
            }
        }
    }

    private void listReview(int videoNo) {
        if (videoReviewDao.selectReview(videoNo).isEmpty()) {
            System.out.println("등록된 리뷰가 없습니다.\n---------------------------------------");
        } else {
            System.out.println("[ 리뷰 ]");
            for (VideoReview review : videoReviewDao.selectReview(videoNo)) {
                System.out.println(review);
            }
            System.out.println("---------------------------------------");
        }
        System.out.println("-----------------메뉴--------------------");
        System.out.println("1. 뒤로 가기");
        System.out.println("2. 종료");
        while (true) {
            int choice = util.inputInt("메뉴를 선택하세요: ");
            switch (choice) {
                case 1:
                    service(videoNo);
                    break;
                case 2:
                    System.out.println("프로그램을 종료합니다.");
                    UserManagerImpl usermanager = UserManagerImpl.getInstance();
                    usermanager.saveUserData();
                    System.exit(0);
                    break;
                default:
                    System.out.println("잘못된 선택입니다. 다시 시도하세요.");
            }
        }
    }

    private void registReview(int videoNo) {
        String reviewContent = util.input("리뷰를 입력하세요: ");
        String nickName = util.input("닉네임을 입력하세요: ");
        VideoReview review = new VideoReview();
        review.setContent(reviewContent);
        review.setNickName(nickName);
        review.setVideoNo(videoNo);

        videoReviewDao.insertReview(review);
        System.out.println("---------------------------------------");
        System.out.println("리뷰가 등록되었습니다.");
        System.out.println("---------------------------------------");
        System.out.println("1. 뒤로 가기");
        System.out.println("2. 종료");
        System.out.println("---------------------------------------");

        while (true) {
            int choice = util.inputInt("메뉴를 선택하세요: ");
            switch (choice) {
                case 1:
                    service(videoNo);
                    break;
                case 2:
                    System.out.println("프로그램을 종료합니다.");
                    UserManagerImpl usermanager = UserManagerImpl.getInstance();
                    usermanager.saveUserData();
                    System.exit(0);
                    break;
                default:
                    System.out.println("잘못된 선택입니다. 다시 시도하세요.");
            }
        }
    }
}
