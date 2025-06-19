package com.haginhae.controller;

import com.haginhae.dto.AttendanceRequest;
import com.haginhae.dto.ScheduleRequest;
import com.haginhae.entity.Schedule;
import com.haginhae.service.ScheduleService;
import com.haginhae.service.ScheduleService.AttendanceDTO;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequiredArgsConstructor
@RequestMapping("/api")
public class ScheduleController {

    private final ScheduleService scheduleService;

    @PostMapping("/schedules")
    public ResponseEntity<?> createSchedule(@RequestBody ScheduleRequest request) {
        // ① Schedule 엔티티 생성
        Schedule schedule = new Schedule(request.getDate(), request.getTime(), request.getTask());

        // ② AttendanceDTO 리스트 변환
        List<ScheduleService.AttendanceDTO> attendanceDTOs = Optional.ofNullable(request.getAttendances())
        	    .orElse(List.of())
        	    .stream()
        	    .map(ar -> new ScheduleService.AttendanceDTO(
        	        ar.memberId(), ar.scheduleId(), ar.status()))
        	    .toList();

        // ③ 서비스 호출
        scheduleService.createSchedule(schedule, attendanceDTOs);
        return ResponseEntity.ok("생성 완료");
    }

    @GetMapping("/schedules")
    public ResponseEntity<List<Schedule>> getAllSchedules() {
        return ResponseEntity.ok(scheduleService.getAllSchedules());
    }

    @GetMapping("/schedules/{id}")
    public ResponseEntity<Schedule> getScheduleById(@PathVariable Long id) {
        return ResponseEntity.ok(scheduleService.getScheduleById(id));
    }

    @DeleteMapping("/schedules/{id}")
    public ResponseEntity<?> deleteSchedule(@PathVariable Long id) {
        scheduleService.deleteSchedule(id);
        return ResponseEntity.ok("삭제 완료");
    }

    @PostMapping("/attendance")
    public ResponseEntity<?> voteAttendance(@RequestBody AttendanceRequest request) {
        scheduleService.voteAttendance(request);
        return ResponseEntity.ok("투표 완료");
    }
    
    @GetMapping("/attendance/contribute")
    public ResponseEntity<?> getContribute() {
        List res = scheduleService.calculateContributions();
        return ResponseEntity.ok(res);
    }
}
