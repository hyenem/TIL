package com.scsa.android.haginhae;

import android.app.AlertDialog;
import android.app.DatePickerDialog;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.util.ArrayList;
import java.util.Calendar;
import java.util.Comparator;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class TodoActivity extends AppCompatActivity {

    private static final String TAG = "TodoActivity_SCSA";

    private ListView todoListView;
    private List<Todo> todoList = new ArrayList<>();
    private TodoAdapter adapter;
    private TodoService todoService;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_todo);

        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("http://10.10.0.14:8080/api/")
                .addConverterFactory(GsonConverterFactory.create())
                .build();

        todoService = retrofit.create(TodoService.class);

        todoListView = findViewById(R.id.todoListView);
        adapter = new TodoAdapter();
        todoListView.setAdapter(adapter);

        findViewById(R.id.btnAddTodo).setOnClickListener(v -> showAddTodoDialog());

        fetchTodos();
    }

    private void fetchTodos() {
        todoService.getTodos().enqueue(new Callback<List<Todo>>() {
            @Override
            public void onResponse(Call<List<Todo>> call, Response<List<Todo>> response) {
                if (response.isSuccessful() && response.body() != null) {
                    todoList.clear();
                    todoList.addAll(response.body());
                    // ✅ 정렬: 미완료 → 완료 순서로 정렬
                    todoList.sort(Comparator.comparing(Todo::isCompleted));
                    adapter.notifyDataSetChanged();
                }
            }

            @Override
            public void onFailure(Call<List<Todo>> call, Throwable t) {
                Toast.makeText(TodoActivity.this, "불러오기 실패", Toast.LENGTH_SHORT).show();
            }
        });
    }

    private void showAddTodoDialog() {
        EditText input = new EditText(this);
        new AlertDialog.Builder(this)
                .setTitle("할 일 추가")
                .setView(input)
                .setPositiveButton("추가", (dialog, which) -> {
                    Todo newTodo = new Todo();
                    newTodo.title = input.getText().toString();
                    newTodo.completed = false;
                    todoService.createTodo(newTodo).enqueue(new Callback<Todo>() {
                        @Override
                        public void onResponse(Call<Todo> call, Response<Todo> response) {
                            fetchTodos();
                        }

                        @Override
                        public void onFailure(Call<Todo> call, Throwable t) {
                            Toast.makeText(TodoActivity.this, "등록 실패", Toast.LENGTH_SHORT).show();
                        }
                    });
                })
                .setNegativeButton("취소", null)
                .show();
    }

    private void showDatePicker(Todo todo) {
        Calendar c = Calendar.getInstance();
        new DatePickerDialog(this, (view, year, month, dayOfMonth) -> {
            String date = String.format("%04d-%02d-%02d", year, month + 1, dayOfMonth);
            Schedule schedule = new Schedule(date, "00:00", todo.title);

            todoService.createSchedule(schedule).enqueue(new Callback<Void>() {
                @Override
                public void onResponse(Call<Void> call, Response<Void> response) {
                    Toast.makeText(TodoActivity.this, "스케줄 등록됨", Toast.LENGTH_SHORT).show();
                }

                @Override
                public void onFailure(Call<Void> call, Throwable t) {
                    Toast.makeText(TodoActivity.this, "스케줄 실패", Toast.LENGTH_SHORT).show();
                }
            });
        }, c.get(Calendar.YEAR), c.get(Calendar.MONTH), c.get(Calendar.DAY_OF_MONTH)).show();
    }

    class TodoAdapter extends BaseAdapter {
        @Override
        public int getCount() { return todoList.size(); }
        @Override
        public Object getItem(int i) { return todoList.get(i); }
        @Override
        public long getItemId(int i) { return i; }

        @Override
        public View getView(int i, View convertView, ViewGroup parent) {
            if (convertView == null) {
                convertView = LayoutInflater.from(TodoActivity.this)
                        .inflate(R.layout.item_todo, parent, false);
            }
            CheckBox checkBox = convertView.findViewById(R.id.checkBox);
            Button btnDelete = convertView.findViewById(R.id.btnDelete);

            Todo todo = todoList.get(i);

            checkBox.setOnCheckedChangeListener(null);  // ✅ 리스너 잠시 해제
            checkBox.setText(todo.title);
            checkBox.setChecked(todo.isCompleted());

            // ✅ 새로 리스너 등록
            checkBox.setOnCheckedChangeListener((buttonView, isChecked) -> {
                todo.setCompleted(isChecked);
                todoService.updateTodo(todo.getId(), todo).enqueue(new Callback<Todo>() {
                    @Override
                    public void onResponse(Call<Todo> call, Response<Todo> response) {
                        if(todo.isCompleted()){
                            Intent intent = new Intent(TodoActivity.this, ScheduleEditActivity.class);
                            intent.putExtra("taskTitle", todo.title);
                            startActivity(intent);
                        }
                        fetchTodos();
                    }

                    @Override
                    public void onFailure(Call<Todo> call, Throwable t) {
                        Toast.makeText(TodoActivity.this, "상태 업데이트 실패", Toast.LENGTH_SHORT).show();
                    }
                });
            });

            btnDelete.setOnClickListener(v -> {
                new AlertDialog.Builder(TodoActivity.this)
                        .setTitle("삭제")
                        .setMessage("정말 삭제하시겠습니까?")
                        .setPositiveButton("삭제", (dialog, which) -> {
                            todoService.deleteTodo(todo.getId()).enqueue(new Callback<Void>() {
                                @Override
                                public void onResponse(Call<Void> call, Response<Void> response) {
                                    fetchTodos();
                                }

                                @Override
                                public void onFailure(Call<Void> call, Throwable t) {
                                    Toast.makeText(TodoActivity.this, "삭제 실패", Toast.LENGTH_SHORT).show();
                                }
                            });
                        })
                        .setNegativeButton("취소", null)
                        .show();
            });

            return convertView;
        }

    }
}
