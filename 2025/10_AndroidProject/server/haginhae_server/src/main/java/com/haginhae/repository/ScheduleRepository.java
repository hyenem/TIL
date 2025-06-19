package com.haginhae.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.haginhae.entity.Schedule;

public interface ScheduleRepository extends JpaRepository<Schedule, Long> {

}
