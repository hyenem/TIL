package com.scsa.android.haginhae;

import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class ContributeActivity extends AppCompatActivity {

    private ListView contributeListView;
    private ScheduleService scheduleService;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_contribute);

        contributeListView = findViewById(R.id.contributeListView);

        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("http://10.10.0.14:8080/api/")
                .addConverterFactory(GsonConverterFactory.create())
                .build();

        scheduleService = retrofit.create(ScheduleService.class);

        // 서버에서 Contribute 데이터 호출
        scheduleService.getContributions().enqueue(new Callback<List<Contribute>>() {
            @Override
            public void onResponse(Call<List<Contribute>> call, Response<List<Contribute>> response) {
                if (response.isSuccessful() && response.body() != null) {
                    List<Contribute> contributeList = response.body();

                    // 리스트 뷰에 간단히 표시
                    ArrayAdapter<String> adapter = new ArrayAdapter<>(ContributeActivity.this,
                            android.R.layout.simple_list_item_1);
                    for (int i = 0; i < contributeList.size(); i++) {
                        Contribute c = contributeList.get(i);
                        adapter.add((i+1) + "위: " + c.getMemberName() + " (" + c.getAttendedCount() + "회)");
                    }
                    contributeListView.setAdapter(adapter);
                } else {
                    Toast.makeText(ContributeActivity.this, "불러오기 실패", Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void onFailure(Call<List<Contribute>> call, Throwable t) {
                Toast.makeText(ContributeActivity.this, "서버 오류", Toast.LENGTH_SHORT).show();
            }
        });
    }
}
