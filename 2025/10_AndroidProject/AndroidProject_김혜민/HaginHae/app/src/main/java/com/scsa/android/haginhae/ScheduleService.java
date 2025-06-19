package com.scsa.android.haginhae;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.DELETE;
import retrofit2.http.GET;
import retrofit2.http.POST;
import retrofit2.http.Path;

public interface ScheduleService {

    // 일정 등록
    @POST("schedules")
    Call<Void> createSchedule(@Body Schedule schedule);

    // 전체 일정 조회
    @GET("schedules")
    Call<List<Schedule>> getSchedules();

    // 특정 일정 상세 조회
    @GET("schedules/{id}")
    Call<Schedule> getScheduleById(@Path("id") Long id);

    // 일정 삭제
    @DELETE("schedules/{id}")
    Call<Void> deleteSchedule(@Path("id") Long id);

    // 참석 투표 등록
    @POST("attendance")
    Call<Void> voteAttendance(@Body AttendanceRequest attendance);

    @GET("attendance/contribute")
    Call<List<Contribute>> getContributions();

}
