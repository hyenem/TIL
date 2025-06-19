package com.haginhae.service;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.haginhae.dto.AttendanceRequest;
import com.haginhae.dto.ContributeResponse;
import com.haginhae.entity.Attendance;
import com.haginhae.entity.Attendance.Status;
import com.haginhae.entity.Member;
import com.haginhae.entity.Schedule;
import com.haginhae.repository.AttendanceRepository;
import com.haginhae.repository.MemberRepository;
import com.haginhae.repository.ScheduleRepository;

import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class ScheduleService {

    private final ScheduleRepository scheduleRepository;
    private final AttendanceRepository attendanceRepository;
    private final MemberRepository memberRepository;

    // 일정 생성
    @Transactional
    public void createSchedule(Schedule schedule, List<AttendanceDTO> attendanceDTOs) {
        scheduleRepository.save(schedule);
        for (AttendanceDTO dto : attendanceDTOs) {
            Member member = memberRepository.findById(dto.memberId())
                    .orElseThrow(() -> new IllegalArgumentException("Member not found"));
            Attendance att = new Attendance();
            att.setSchedule(schedule);
            att.setMember(member);
            
            Status status = dto.status();
            if(status.equals(Status.참여) || status.equals(Status.불확실) || status.equals(Status.불참)) {
            	att.setPlannedStatus(status);
            } else {
            	att.setActualStatus(status);
            }
            attendanceRepository.save(att);
        }
    }

    public List<Schedule> getAllSchedules() {
        return scheduleRepository.findAll();
    }

    public Schedule getScheduleById(Long id) {
        return scheduleRepository.findById(id)
                .orElseThrow(() -> new IllegalArgumentException("Schedule not found"));
    }

    @Transactional
    public void deleteSchedule(Long id) {
        scheduleRepository.deleteById(id);
    }

    @Transactional
    public void voteAttendance(AttendanceRequest request) {
    	Long scheduleId = request.scheduleId();
    	Long memberId = request.memberId();
        Attendance att = attendanceRepository.findByMember_IdAndSchedule_Id(memberId, scheduleId)
                .orElse(Attendance.builder().member(new Member(memberId, null)).schedule(new Schedule(scheduleId, null, null, null, null)).build());
        
        Attendance.Status status = request.status();
        if(status.equals(Status.참여) || status.equals(Status.불확실) || status.equals(Status.불참)) {
        	att.setPlannedStatus(status);
        } else {
        	att.setActualStatus(status);
        }
        attendanceRepository.save(att);
    }

 // 참석 통계 계산 (스타일 개선)
    public List<ContributeResponse> calculateContributions() {
        return memberRepository.findAll().stream()
                .map(member -> {
                    long attendedCount = attendanceRepository.countByMemberAttended(member);
                    return new ContributeResponse(member.getId(), member.getName(), (int) attendedCount);
                })
                .sorted((a, b) -> Integer.compare(b.attendedCount(), a.attendedCount()))
                .collect(Collectors.toList());
    }

    // 내부 DTO
    public record AttendanceDTO(Long memberId, Long scheduleId, Status status) {}



}
