package com.haginhae.dto;

import java.util.List;

public class ScheduleRequest {
    private String date;
    private String time;
    private String task;
    private List<AttendanceRequest> attendances;

    // 반드시 getter 생성
    public String getDate() { return date; }
    public String getTime() { return time; }
    public String getTask() { return task; }
    public List<AttendanceRequest> getAttendances() { return attendances; }
}
