package com.haginhae.repository;


import org.springframework.data.jpa.repository.JpaRepository;

import com.haginhae.entity.Member;

public interface MemberRepository extends JpaRepository<Member, Long> {
}