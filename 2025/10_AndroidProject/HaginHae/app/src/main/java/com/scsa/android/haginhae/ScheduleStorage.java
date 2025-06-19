package com.scsa.android.haginhae;

import java.time.LocalDate;
import java.util.*;

public class ScheduleStorage {
    private static final Map<LocalDate, List<String>> scheduleMap = new HashMap<>();

    public static void addSchedule(LocalDate date, String title) {
        scheduleMap.computeIfAbsent(date, k -> new ArrayList<>()).add(title);
    }

    public static void removeSchedule(String title) {
        for (List<String> list : scheduleMap.values()) {
            list.remove(title);
        }
    }

    public static List<String> getSchedulesFor(LocalDate date) {
        return scheduleMap.getOrDefault(date, new ArrayList<>());
    }

    public static Map<LocalDate, List<String>> getAll() {
        return scheduleMap;
    }
}
