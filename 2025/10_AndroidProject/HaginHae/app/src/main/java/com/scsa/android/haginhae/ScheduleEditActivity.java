package com.scsa.android.haginhae;

import android.annotation.SuppressLint;
import android.app.AlarmManager;
import android.app.DatePickerDialog;
import android.app.PendingIntent;
import android.app.TimePickerDialog;
import android.content.Context;
import android.content.Intent;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.provider.Settings;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.Locale;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class ScheduleEditActivity extends AppCompatActivity {
    private Button btnPickDate, btnPickTime, btnSave;
    private EditText editTaskTitle;
    private String pickedDate = null;
    private String pickedTime = null;
    private AlarmManager alarmManager;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_schedule_edit);

        alarmManager = (AlarmManager) getSystemService(ALARM_SERVICE);

        btnPickDate = findViewById(R.id.btnPickDate);
        btnPickTime = findViewById(R.id.btnPickTime);
        btnSave = findViewById(R.id.btnSave);
        editTaskTitle = findViewById(R.id.editTaskTitle);

        // Intent에서 taskTitle, selectedDate 받기
        String taskTitle = getIntent().getStringExtra("taskTitle");
        if (taskTitle != null) {
            editTaskTitle.setText(taskTitle);
        }

        String selectedDate = getIntent().getStringExtra("selectedDate");
        if (selectedDate != null) {
            pickedDate = selectedDate;
            btnPickDate.setText(pickedDate);
        }

        btnPickDate.setOnClickListener(v -> {
            Calendar now = Calendar.getInstance();
            new DatePickerDialog(this, (view, y, m, d) -> {
                pickedDate = String.format("%04d-%02d-%02d", y, m + 1, d);
                btnPickDate.setText(pickedDate);
            }, now.get(Calendar.YEAR), now.get(Calendar.MONTH), now.get(Calendar.DAY_OF_MONTH)).show();
        });

        btnPickTime.setOnClickListener(v -> {
            Calendar now = Calendar.getInstance();
            new TimePickerDialog(this, (view, h, min) -> {
                pickedTime = String.format("%02d:%02d", h, min);
                btnPickTime.setText(pickedTime);
            }, now.get(Calendar.HOUR_OF_DAY), now.get(Calendar.MINUTE), true).show();
        });

        btnSave.setOnClickListener(v -> {
            String inputTitle = editTaskTitle.getText().toString();
            if (inputTitle.isEmpty() || pickedDate == null || pickedTime == null) {
                Toast.makeText(this, "할 일, 날짜, 시간을 모두 입력하세요.", Toast.LENGTH_SHORT).show();
                return;
            }

            Schedule schedule = new Schedule(pickedDate, pickedTime, inputTitle);
            Retrofit retrofit = new Retrofit.Builder()
                    .baseUrl("http://10.10.0.14:8080/api/")
                    .addConverterFactory(GsonConverterFactory.create())
                    .build();

            ScheduleService scheduleService = retrofit.create(ScheduleService.class);
            scheduleService.createSchedule(schedule).enqueue(new Callback<Void>() {
                @Override
                public void onResponse(Call<Void> call, Response<Void> response) {
                    Toast.makeText(ScheduleEditActivity.this, "일정 등록 완료", Toast.LENGTH_SHORT).show();
                    setAlarm(pickedDate, pickedTime, inputTitle);
                    finish();
                }

                @Override
                public void onFailure(Call<Void> call, Throwable t) {
                    Toast.makeText(ScheduleEditActivity.this, "서버 오류", Toast.LENGTH_SHORT).show();
                }
            });
        });
    }

    private void setAlarm(String pickedDate, String pickedTime, String taskTitle) {
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm", Locale.getDefault());

        try {
            Date targetDate = sdf.parse(pickedDate + " " + pickedTime);
            long triggerTimeMillis = targetDate.getTime() - (60 * 60 * 1000); // 1시간 전

            if (triggerTimeMillis <= System.currentTimeMillis()) {
                Toast.makeText(this, "이미 지난 시간입니다.", Toast.LENGTH_SHORT).show();
                return;
            }

            Intent intent = new Intent(this, AlarmReceiver.class);
            intent.putExtra("taskTitle", taskTitle);

            // requestCode를 taskTitle 해시값으로 고정
            int requestCode = (taskTitle != null ? taskTitle.hashCode() : (int) System.currentTimeMillis());

            PendingIntent pendingIntent = PendingIntent.getBroadcast(
                    this, requestCode, intent, PendingIntent.FLAG_UPDATE_CURRENT | PendingIntent.FLAG_IMMUTABLE);

            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
                if (!alarmManager.canScheduleExactAlarms()) {
                    Intent permissionIntent = new Intent(Settings.ACTION_REQUEST_SCHEDULE_EXACT_ALARM);
                    startActivity(permissionIntent);
                    Toast.makeText(this, "정확한 알람 권한을 허용해주세요", Toast.LENGTH_LONG).show();
                    return;
                }
            }

            alarmManager.setExactAndAllowWhileIdle(AlarmManager.RTC_WAKEUP, triggerTimeMillis, pendingIntent);

        } catch (ParseException e) {
            e.printStackTrace();
            Toast.makeText(this, "시간 파싱 실패", Toast.LENGTH_SHORT).show();
        }
    }



    @Override
    protected void onResume() {
        super.onResume();
        checkStartPermissionRequest();
    }

    public void checkStartPermissionRequest() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
            if (!alarmManager.canScheduleExactAlarms()) {
                Intent intent = new Intent(Settings.ACTION_REQUEST_SCHEDULE_EXACT_ALARM,
                        Uri.parse("package:" + getPackageName()));
                startActivity(intent);
            }
        }
        if (!Settings.canDrawOverlays(this)) {
            Intent intent = new Intent(Settings.ACTION_MANAGE_OVERLAY_PERMISSION,
                    Uri.parse("package:" + getPackageName()));
            startActivityForResult(intent, 1000);
            Toast.makeText(this, "권한을 허용해 주세요.", Toast.LENGTH_SHORT).show();
        }
    }
}
