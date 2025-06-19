package com.haginhae.repository;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import com.haginhae.entity.Attendance;
import com.haginhae.entity.Attendance.Status;
import com.haginhae.entity.Member;

public interface AttendanceRepository extends JpaRepository<Attendance, Long> {

	Optional<Attendance> findByMemberIdAndScheduleId(Long memberId, Long scheduleId);
	// JPQL 또는 메서드 네이밍 기반으로 추가
	Optional<Attendance> findByMember_IdAndSchedule_Id(Long memberId, Long scheduleId);
	@Query("SELECT COUNT(a) FROM Attendance a WHERE a.member = :member AND a.actualStatus = com.haginhae.entity.Attendance.Status.참석")
	int countByMemberAttended(@Param("member") Member member);

}