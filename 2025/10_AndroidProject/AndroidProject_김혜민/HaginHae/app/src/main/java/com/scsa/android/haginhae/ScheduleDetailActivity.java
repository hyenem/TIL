package com.scsa.android.haginhae;

import android.app.AlertDialog;
import android.app.PendingIntent;
import android.content.Intent;
import android.nfc.NdefMessage;
import android.nfc.NdefRecord;
import android.nfc.NfcAdapter;
import android.nfc.Tag;
import android.nfc.tech.Ndef;
import android.os.Bundle;
import android.os.Parcelable;
import android.util.Log;
import android.widget.Button;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.nio.charset.Charset;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class ScheduleDetailActivity extends AppCompatActivity {

    private static final String TAG = "ScheduleDetailActivity_SCSA";

    private TextView txtTitle, txtTime, txtDate;
    private ListView attendanceListView;
    private Button btnVoteO, btnVoteTriangle, btnVoteX, btnDelete, nfcButton;
    private ScheduleService service;
    private int userId = 1;

    private Long scheduleId;
    private boolean waitingForNfc = false;

    private NfcAdapter nfcAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_schedule_detail);

        txtTitle = findViewById(R.id.txtTitle);
        txtTime = findViewById(R.id.txtTime);
        txtDate = findViewById(R.id.txtDate);
        attendanceListView = findViewById(R.id.attendanceListView);
        btnVoteO = findViewById(R.id.btnVoteO);
        btnVoteTriangle = findViewById(R.id.btnVoteTriangle);
        btnVoteX = findViewById(R.id.btnVoteX);
        btnDelete = findViewById(R.id.btnDelete);
        nfcButton = findViewById(R.id.writeNfc);

        scheduleId = getIntent().getLongExtra("scheduleId", -1);
        Log.d(TAG, "onCreate: " + scheduleId);
        if (scheduleId == -1) {
            Toast.makeText(this, "잘못된 접근입니다", Toast.LENGTH_SHORT).show();
            finish();
            return;
        }

        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("http://10.10.0.14:8080/api/")
                .addConverterFactory(GsonConverterFactory.create())
                .build();

        service = retrofit.create(ScheduleService.class);

        service.getScheduleById(scheduleId).enqueue(new Callback<Schedule>() {
            @Override
            public void onResponse(Call<Schedule> call, Response<Schedule> response) {
                if (response.isSuccessful() && response.body() != null) {
                    Schedule schedule = response.body();
                    txtTitle.setText(schedule.getTask());
                    txtDate.setText(schedule.getDate());
                    txtTime.setText(schedule.getTime());
                    attendanceListView.setAdapter(new AttendanceAdapter(ScheduleDetailActivity.this, schedule.getAttendances()));
                } else {
                    Toast.makeText(ScheduleDetailActivity.this, "불러오기 실패", Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void onFailure(Call<Schedule> call, Throwable t) {
                Toast.makeText(ScheduleDetailActivity.this, "서버 오류", Toast.LENGTH_SHORT).show();
            }
        });

        btnVoteO.setOnClickListener(v -> submitAttendance(scheduleId, 0));
        btnVoteTriangle.setOnClickListener(v -> submitAttendance(scheduleId, 1));
        btnVoteX.setOnClickListener(v -> submitAttendance(scheduleId, 2));

        btnDelete.setOnClickListener(v -> {
            new AlertDialog.Builder(this)
                    .setTitle("일정 삭제")
                    .setMessage("정말 삭제하시겠습니까?")
                    .setPositiveButton("삭제", (dialog, which) -> {
                        service.deleteSchedule(scheduleId).enqueue(new Callback<Void>() {
                            @Override
                            public void onResponse(Call<Void> call, Response<Void> response) {
                                Toast.makeText(ScheduleDetailActivity.this, "삭제 완료", Toast.LENGTH_SHORT).show();
                                finish();
                            }

                            @Override
                            public void onFailure(Call<Void> call, Throwable t) {
                                Toast.makeText(ScheduleDetailActivity.this, "삭제 실패", Toast.LENGTH_SHORT).show();
                            }
                        });
                    })
                    .setNegativeButton("취소", null)
                    .show();
        });

        // ✅ NFC 준비
        nfcAdapter = NfcAdapter.getDefaultAdapter(this);
        if (nfcAdapter == null) {
            Toast.makeText(this, "NFC 미지원 기기입니다", Toast.LENGTH_SHORT).show();
            nfcButton.setEnabled(false);
        }

        nfcButton.setOnClickListener(v -> {
            waitingForNfc = true;
            Toast.makeText(this, "NFC를 태그해주세요", Toast.LENGTH_SHORT).show();
        });
    }

    private void submitAttendance(Long scheduleId, int status) {
        AttendanceRequest vote = new AttendanceRequest(userId, scheduleId, status);
        service.voteAttendance(vote).enqueue(new Callback<Void>() {
            @Override
            public void onResponse(Call<Void> call, Response<Void> response) {
                Toast.makeText(ScheduleDetailActivity.this, "투표 완료", Toast.LENGTH_SHORT).show();
                recreate();
            }

            @Override
            public void onFailure(Call<Void> call, Throwable t) {
                Toast.makeText(ScheduleDetailActivity.this, "투표 실패", Toast.LENGTH_SHORT).show();
            }
        });
    }

    // ✅ Foreground Dispatch (앱이 화면에 있을 때 NFC 우선 수신)
    @Override
    protected void onResume() {
        super.onResume();
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

    // ✅ 태그 감지 처리
    @Override
    protected void onNewIntent(Intent intent) {
        super.onNewIntent(intent);
        if (!waitingForNfc) return;

        Tag tag = intent.getParcelableExtra(NfcAdapter.EXTRA_TAG);
        if (tag != null) {
            writeNfcTag(tag, scheduleId);
        }
    }

    private void writeNfcTag(Tag tag, Long scheduleId) {
        NdefMessage message = new NdefMessage(new NdefRecord[]{
                NdefRecord.createTextRecord("ko", String.valueOf(scheduleId))
        });

        try {
            Ndef ndef = Ndef.get(tag);
            if (ndef != null) {
                ndef.connect();
                if (!ndef.isWritable()) {
                    Toast.makeText(this, "쓰기 불가 태그", Toast.LENGTH_SHORT).show();
                    return;
                }
                ndef.writeNdefMessage(message);
                Toast.makeText(this, "NFC 기록 완료", Toast.LENGTH_SHORT).show();
                waitingForNfc = false;
                ndef.close();
            } else {
                Toast.makeText(this, "NDEF 지원 안됨", Toast.LENGTH_SHORT).show();
            }
        } catch (Exception e) {
            e.printStackTrace();
            Toast.makeText(this, "NFC 기록 실패", Toast.LENGTH_SHORT).show();
        }
    }
}
