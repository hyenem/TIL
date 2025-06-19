package com.haginhae.entity;

import java.util.ArrayList;
import java.util.List;

import com.haginhae.service.ScheduleService.AttendanceDTO;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Builder
@Data
@NoArgsConstructor
@AllArgsConstructor
public class ScheduleRequest {
    private String date;
    private String time;
    private String task;
    private List<AttendanceDTO> attendances = new ArrayList<>(); // ✅ 기본값 설정
}