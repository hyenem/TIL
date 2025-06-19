package com.scsa.android.haginhae;

import java.util.List;

public class Schedule {

    private Long id;
    private String date;
    private String time;
    private String task;
    private List<Attendance> attendances; // 참석자 상태 리스트


    public Schedule(String date, String time, String task) {
        this.date = date;
        this.time = time;
        this.task = task;
    }

    public List<Attendance> getAttendances() {
        return attendances;
    }

    public void setAttendances(List<Attendance> attendances) {
        this.attendances = attendances;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public String getTask() {
        return task;
    }

    public void setTask(String task) {
        this.task = task;
    }

    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }

    @Override
    public String toString() {
        return time + " " + task;
    }
}