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

public class Contribute {
    private Long memberId;
    private String memberName;
    private int attendedCount;

    public Long getMemberId() { return memberId; }
    public String getMemberName() { return memberName; }
    public int getAttendedCount() { return attendedCount; }

}
