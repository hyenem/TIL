package com.haginhae.dto;

import com.haginhae.entity.Attendance;
import com.haginhae.entity.Attendance.Status;

public record AttendanceRequest(
    Long memberId,
    Long scheduleId,
    Attendance.Status status
) {}
