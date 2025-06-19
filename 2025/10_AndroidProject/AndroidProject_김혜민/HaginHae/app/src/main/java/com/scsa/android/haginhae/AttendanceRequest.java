package com.scsa.android.haginhae;

public class AttendanceRequest {
    private int memberId;
    private Long scheduleId;
    private int status;

    public AttendanceRequest(int memberId, Long scheduleId, int status) {
        this.memberId = memberId;
        this.scheduleId = scheduleId;
        this.status = status;
    }

    public int getMemberId() {
        return memberId;
    }

    public Long getScheduleId() {
        return scheduleId;
    }

    public int getStatus() {
        return status;
    }
}
