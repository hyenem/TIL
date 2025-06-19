package com.scsa.android.haginhae;


public class Attendance {
    private Long id;
    private Member member;
    private Status plannedStatus;
    private Status actualStatus;

    public Attendance() {} // 기본 생성자

    public Member getMember() {
        return member;
    }

    public Status getPlannedStatus() {
        return plannedStatus;
    }

    public Status getActualStatus() {
        return actualStatus;
    }

    public enum Status {
        참여, 불확실, 불참, 참석, 불참함
    }
}
