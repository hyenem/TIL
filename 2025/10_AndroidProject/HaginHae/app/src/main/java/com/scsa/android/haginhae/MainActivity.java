package com.scsa.android.haginhae;

import android.app.PendingIntent;
import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.nfc.NdefMessage;
import android.nfc.NfcAdapter;
import android.nfc.Tag;
import android.nfc.tech.Ndef;
import android.net.Uri;
import android.os.Bundle;
import android.util.Log;
import android.view.GestureDetector;
import android.view.MotionEvent;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.CalendarView;
import android.widget.ImageView;
import android.widget.ListView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.nio.charset.Charset;
import java.util.Calendar;
import java.util.List;
import java.util.stream.Collectors;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "MainActivity_SCSA";

    private CalendarView calendarView;
    private ScheduleService scheduleService;
    private List<Schedule> scheduleList;
    private String selected = null;


    // ✅ NFC 관련
    private NfcAdapter nfcAdapter;
    private int userId = 1;  // 출석용 사용자 ID

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        calendarView = findViewById(R.id.calendarView);

        findViewById(R.id.todolist).setOnClickListener(v -> {
            Intent intent = new Intent(this, TodoActivity.class);
            startActivity(intent);
        });
        findViewById(R.id.article).setOnClickListener(v -> {
            Intent intent = new Intent(this, ArticleActivity.class);
            startActivity(intent);
        });
        findViewById(R.id.minigame).setOnClickListener(v -> {
            Intent intent = new Intent(this, GameActivity.class);
            startActivity(intent);
        });
        findViewById(R.id.contribute).setOnClickListener(v -> {
            Intent intent = new Intent(this, ContributeActivity.class);
            startActivity(intent);
        });

        ImageView youtubeBtn = findViewById(R.id.youtube);
        youtubeBtn.setOnClickListener(v -> {
            Intent intent = new Intent(Intent.ACTION_VIEW);
            intent.setData(Uri.parse("https://www.youtube.com/@HAGINHAE_official"));
            intent.setPackage("com.google.android.youtube");
            try {
                startActivity(intent);
            } catch (ActivityNotFoundException e) {
                intent.setPackage(null);
                startActivity(intent);
            }
        });

        ImageView instagramBtn = findViewById(R.id.instagram);
        instagramBtn.setOnClickListener(v -> {
            Uri uri = Uri.parse("http://instagram.com/_u/haginhae_official");
            Intent intent = new Intent(Intent.ACTION_VIEW, uri);
            intent.setPackage("com.instagram.android");
            try {
                startActivity(intent);
            } catch (ActivityNotFoundException e) {
                Intent webIntent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://www.instagram.com/haginhae_official/"));
                startActivity(webIntent);
            }
        });
        Button addButton = findViewById(R.id.addButton);
        addButton.setOnClickListener(v -> {
            if (selected == null) {
                // 초기값 없을 경우 오늘 날짜 사용 (앱 처음 실행했을 때 대비)
                Calendar cal = Calendar.getInstance();
                selected = String.format("%04d-%02d-%02d",
                        cal.get(Calendar.YEAR), cal.get(Calendar.MONTH) + 1, cal.get(Calendar.DAY_OF_MONTH));
            }

            Intent intent = new Intent(MainActivity.this, ScheduleEditActivity.class);
            intent.putExtra("selectedDate", selected);
            startActivity(intent);
        });

        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("http://10.10.0.14:8080/api/")
                .addConverterFactory(GsonConverterFactory.create())
                .build();
        scheduleService = retrofit.create(ScheduleService.class);

        // NFC 초기화
        nfcAdapter = NfcAdapter.getDefaultAdapter(this);
        if (nfcAdapter == null) {
            Toast.makeText(this, "NFC 미지원 기기입니다", Toast.LENGTH_SHORT).show();
        }

        fetchSchedules();

        calendarView.setOnDateChangeListener((view, year, month, dayOfMonth) -> {
            selected = String.format("%04d-%02d-%02d", year, month + 1, dayOfMonth);
            showSchedulesForDate(selected);
        });

    }

    private void fetchSchedules() {
        scheduleService.getSchedules().enqueue(new Callback<List<Schedule>>() {
            @Override
            public void onResponse(Call<List<Schedule>> call, Response<List<Schedule>> response) {
                if (!response.isSuccessful() || response.body() == null) {
                    Toast.makeText(MainActivity.this, "서버 응답 실패", Toast.LENGTH_SHORT).show();
                    return;
                }
                scheduleList = response.body();

                // 👉 여기가 핵심!!
                if (selected == null) {
                    Calendar cal = Calendar.getInstance();
                    selected = String.format("%04d-%02d-%02d",
                            cal.get(Calendar.YEAR),
                            cal.get(Calendar.MONTH) + 1,
                            cal.get(Calendar.DAY_OF_MONTH));
                }

                showSchedulesForDate(selected);

                // 선택된 날짜로 캘린더 이동
                String[] parts = selected.split("-");
                Calendar cal = Calendar.getInstance();
                cal.set(Integer.parseInt(parts[0]),
                        Integer.parseInt(parts[1]) - 1,
                        Integer.parseInt(parts[2]));

                calendarView.setDate(cal.getTimeInMillis());
            }

            @Override
            public void onFailure(Call<List<Schedule>> call, Throwable t) {
                Log.d(TAG, "onFailure: "+t.getMessage());
                Toast.makeText(MainActivity.this, "스케줄 불러오기 실패", Toast.LENGTH_SHORT).show();
            }
        });
    }


    private void showSchedulesForDate(String dateString) {
        if (scheduleList == null) {
            Toast.makeText(this, "일정이 아직 불러와지지 않았습니다", Toast.LENGTH_SHORT).show();
            return;
        }
        List<Schedule> filtered = scheduleList.stream()
                .filter(s -> dateString.equals(s.getDate()))
                .collect(Collectors.toList());
        ListView scheduleListView = findViewById(R.id.scheduleListView);
        ArrayAdapter<Schedule> adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, filtered);
        scheduleListView.setAdapter(adapter);
        scheduleListView.setOnItemClickListener((parent, view, position, id) -> {
            Schedule selectedSchedule = filtered.get(position);
            Intent intent = new Intent(MainActivity.this, ScheduleDetailActivity.class);
            intent.putExtra("scheduleId", selectedSchedule.getId());
            startActivity(intent);
        });
    }

    @Override
    protected void onResume() {
        super.onResume();
        refreshScheduleList();

        // ✅ NFC Foreground Dispatch 등록
        if (nfcAdapter != null) {
            Intent intent = new Intent(this, getClass()).addFlags(Intent.FLAG_ACTIVITY_SINGLE_TOP);
            PendingIntent pendingIntent = PendingIntent.getActivity(this, 0, intent, PendingIntent.FLAG_MUTABLE);
            nfcAdapter.enableForegroundDispatch(this, pendingIntent, null, null);
        }
    }

    @Override
    protected void onPause() {
        super.onPause();
        if (nfcAdapter != null) {
            nfcAdapter.disableForegroundDispatch(this);
        }
    }

    private void refreshScheduleList() {
        scheduleService.getSchedules().enqueue(new Callback<List<Schedule>>() {
            @Override
            public void onResponse(Call<List<Schedule>> call, Response<List<Schedule>> response) {
                if (!response.isSuccessful() || response.body() == null) return;
                scheduleList = response.body();

                // 👉 selected 유지
                if (selected == null) {
                    Calendar cal = Calendar.getInstance();
                    selected = String.format("%04d-%02d-%02d",
                            cal.get(Calendar.YEAR), cal.get(Calendar.MONTH) + 1, cal.get(Calendar.DAY_OF_MONTH));
                }

                showSchedulesForDate(selected);

                // 👉 캘린더도 selected로 이동
                String[] parts = selected.split("-");
                Calendar cal = Calendar.getInstance();
                cal.set(Integer.parseInt(parts[0]),
                        Integer.parseInt(parts[1]) - 1,
                        Integer.parseInt(parts[2]));
                calendarView.setDate(cal.getTimeInMillis());
            }

            @Override
            public void onFailure(Call<List<Schedule>> call, Throwable t) {}
        });
    }

    // ✅ NFC 감지 처리 추가
    @Override
    protected void onNewIntent(Intent intent) {
        super.onNewIntent(intent);
        Tag tag = intent.getParcelableExtra(NfcAdapter.EXTRA_TAG);
        if (tag != null) {
            handleNfcScan(tag);
        }
    }

    private void handleNfcScan(Tag tag) {
        try {
            Ndef ndef = Ndef.get(tag);
            if (ndef != null) {
                ndef.connect();
                NdefMessage message = ndef.getNdefMessage();
                String payload = new String(message.getRecords()[0].getPayload(), Charset.forName("UTF-8"));
                String scheduleIdStr = payload.substring(3); // NDEF TextRecord 규격
                Long scannedScheduleId = Long.parseLong(scheduleIdStr);
                ndef.close();

                Log.d(TAG, "NFC 감지된 스케줄 ID: " + scannedScheduleId);
                registerAttendance(scannedScheduleId);
            } else {
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void registerAttendance(Long scheduleId) {
        AttendanceRequest request = new AttendanceRequest(userId, scheduleId, 3);
        scheduleService.voteAttendance(request).enqueue(new Callback<Void>() {
            @Override
            public void onResponse(Call<Void> call, Response<Void> response) {
                Toast.makeText(MainActivity.this, "출석 등록 완료 (NFC)", Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onFailure(Call<Void> call, Throwable t) {
            }
        });
    }
}