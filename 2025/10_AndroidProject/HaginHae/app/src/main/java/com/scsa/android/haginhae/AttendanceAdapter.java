package com.scsa.android.haginhae;

import android.content.Context;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

import java.util.List;

public class AttendanceAdapter extends BaseAdapter {

    private static final String TAG = "AttendanceAdapter_SCSA";
    
    private final List<Attendance> attendances;
    private final LayoutInflater inflater;

    public AttendanceAdapter(Context context, List<Attendance> attendances) {
        this.attendances = attendances;
        this.inflater = LayoutInflater.from(context);
    }

    @Override
    public int getCount() {
        return attendances.size();
    }

    @Override
    public Object getItem(int position) {
        return attendances.get(position);
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        if (convertView == null) {
            convertView = inflater.inflate(android.R.layout.simple_list_item_2, parent, false);
        }

        TextView text1 = convertView.findViewById(android.R.id.text1);
        TextView text2 = convertView.findViewById(android.R.id.text2);

        Attendance att = attendances.get(position);
        text1.setText(att.getMember().getName());

        String statusText;
        if(att.getActualStatus()!=null && att.getActualStatus()== Attendance.Status.참석){
            statusText = "참석완료⭐";
        } else if(att.getPlannedStatus()!=null){
            switch (att.getPlannedStatus()) {
                case 참여:
                    statusText = "참석예정 (●)";
                    break;
                case 불확실:
                    statusText = "불확실 (△)";
                    break;
                case 불참:
                    statusText = "불참 (X)";
                    break;
                default:
                    statusText = "미정";
                    break;
            }
        } else {
            statusText = "미정";
        }
        text2.setText(statusText);

        return convertView;
    }
}