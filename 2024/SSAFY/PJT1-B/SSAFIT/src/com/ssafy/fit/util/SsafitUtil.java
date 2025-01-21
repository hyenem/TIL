package com.ssafy.fit.util;

import java.util.Scanner;

public class SsafitUtil {
	private Scanner sc;
	
	// 생성자
	public SsafitUtil() {
        sc = new Scanner(System.in); // Scanner 초기화
    }

    // 문자열 입력
    public String input(String msg) {
        System.out.print(msg);
        return sc.next(); // 문자열 입력받기
    }

    // 정수 입력
    public int inputInt(String msg) {
        System.out.print(msg);
        // 유효한 정수 받을 때 까지 무한루프
        while (!sc.hasNextInt()) {
            sc.next(); // 무효값 제거
            System.out.print("입력 범위를 벗어났습니다." + msg);
        }
        return sc.nextInt();
    }

    public void printLine() {
        System.out.println();
    }

    // 특정 문자 출력
    public void printLine(char ch) {
        System.out.println(ch);
    }

    // 특정 문자를 지정된 길이만큼 반복하여 출력
    public void printLine(char ch, int len) {
        for (int i = 0; i < len; i++) {
            System.out.print(ch); // 특정 문자 반복 출력
        }
        System.out.println();
    }

    // 콘솔 화면을 지우는 메서드 --> 기능을 확실하게 이해 못 함
    public void screenClear() {
        try {
            if (System.getProperty("os.name").contains("Windows")) {
                // Windows에서는 "cls" 명령어 사용
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            } else {
                // Unix 기반 시스템에서는 ANSI escape code 사용
                System.out.print("\033[H\033[2J");
                System.out.flush();
            }
        } catch (Exception e) {
            e.printStackTrace(); // 예외 발생 시 스택 트레이스 출력
        }
    }
}

