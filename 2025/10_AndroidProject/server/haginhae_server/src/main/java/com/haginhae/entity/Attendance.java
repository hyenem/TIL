package com.haginhae.entity;


import com.fasterxml.jackson.annotation.JsonBackReference;
import com.fasterxml.jackson.annotation.JsonIgnore;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity
@Getter
@Setter
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class Attendance {
    @Id
    @GeneratedValue
    private Long id;

    @ManyToOne
    @JoinColumn(name = "schedule_id")
    @JsonBackReference
    private Schedule schedule;

    @ManyToOne
    private Member member;

    @Enumerated(EnumType.STRING)
    private Status plannedStatus;

    @Enumerated(EnumType.STRING)
    private Status actualStatus;

    public enum Status {
        참여, 불확실, 불참, 참석, 불참함
    }
}
