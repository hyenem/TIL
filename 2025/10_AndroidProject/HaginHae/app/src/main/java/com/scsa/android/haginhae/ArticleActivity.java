package com.scsa.android.haginhae;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.util.Xml;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;

import com.scsa.android.haginhae.databinding.ArticleRowBinding;

import org.xmlpull.v1.XmlPullParser;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.net.URL;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.stream.Collectors;

public class ArticleActivity extends AppCompatActivity {

    private static final String TAG = "ArticleActivity_SCSA";

    ListView listView;
    EditText searchInput;
    MyAdapter adapter;
    List<ArticleItem> list = new ArrayList<>();
    List<ArticleItem> filteredList = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_article);

        listView = findViewById(R.id.result);
        searchInput = findViewById(R.id.searchInput);
        adapter = new MyAdapter();
        listView.setAdapter(adapter);

        new MyAsyncTask().execute("https://www.sportschosun.com/rss/index_vb.htm");

        listView.setOnItemClickListener((parent, view, position, id) -> {
            ArticleItem item = filteredList.get(position);
            Intent intent = new Intent(Intent.ACTION_VIEW, android.net.Uri.parse(item.link));
            startActivity(intent);
        });

        // 검색어 입력할 때마다 필터링
        searchInput.addTextChangedListener(new android.text.TextWatcher() {
            @Override public void beforeTextChanged(CharSequence s, int start, int count, int after) { }
            @Override public void onTextChanged(CharSequence s, int start, int before, int count) { filterList(); }
            @Override public void afterTextChanged(android.text.Editable s) { }
        });
    }

    private void filterList() {
        String keyword = searchInput.getText().toString().toLowerCase();
        if (keyword.isEmpty()) {
            filteredList = new ArrayList<>(list);
        } else {
            filteredList = list.stream()
                    .filter(item -> item.title.toLowerCase().contains(keyword))
                    .collect(Collectors.toList());
        }
        adapter.notifyDataSetChanged();
    }

    class MyAsyncTask extends AsyncTask<String, String, List<ArticleItem>> {
        protected List<ArticleItem> doInBackground(String... arg) {
            try {
                Log.d(TAG, "RSS XML download start....");
                InputStream input = new URL(arg[0]).openConnection().getInputStream();
                BufferedReader reader = new BufferedReader(new InputStreamReader(input));
                parsing(reader);
                Log.d(TAG, "RSS parsed: " + list.size());
            } catch (Exception e) {
                e.printStackTrace();
            }
            return list;
        }

        protected void onPostExecute(List<ArticleItem> result) {
            filteredList = new ArrayList<>(list); // 처음엔 전체 보여줌
            adapter.notifyDataSetChanged();
        }

        XmlPullParser parser = Xml.newPullParser();
        private void parsing(Reader reader) throws Exception {
            parser.setInput(reader);
            int eventType = parser.getEventType();
            ArticleItem item = null;
            long id = 0;
            while (eventType != XmlPullParser.END_DOCUMENT) {
                String name = null;
                switch (eventType) {
                    case XmlPullParser.START_TAG:
                        name = parser.getName();
                        if (name.equalsIgnoreCase("item")) {
                            item = new ArticleItem();
                            item.id = ++id;
                        } else if (item != null) {
                            if (name.equalsIgnoreCase("title")) {
                                item.title = parser.nextText();
                            } else if (name.equalsIgnoreCase("link")) {
                                item.link = parser.nextText();
                            } else if (name.equalsIgnoreCase("description")) {
                                item.description = parser.nextText();
                            } else if (name.equalsIgnoreCase("pubDate")) {
                                item.pubDate = new Date(parser.nextText());
                            }
                        }
                        break;
                    case XmlPullParser.END_TAG:
                        name = parser.getName();
                        if (name.equalsIgnoreCase("item") && item != null) {
                            list.add(item);
                        }
                        break;
                }
                eventType = parser.next();
            }
        }
    }

    class MyAdapter extends BaseAdapter {
        @Override
        public View getView(int position, View convertView, ViewGroup viewGroup) {
            ViewHolder holder;
            if (convertView == null) {
                ArticleRowBinding binding = ArticleRowBinding.inflate(LayoutInflater.from(ArticleActivity.this), viewGroup, false);
                convertView = binding.getRoot();
                holder = new ViewHolder();
                holder.title = binding.title;
                convertView.setTag(holder);
            } else {
                holder = (ViewHolder) convertView.getTag();
            }
            ArticleItem item = filteredList.get(position);
            holder.title.setText(item.title);
            return convertView;
        }

        class ViewHolder { TextView title; }

        @Override public int getCount() { return filteredList.size(); }
        @Override public Object getItem(int i) { return filteredList.get(i); }
        @Override public long getItemId(int i) { return filteredList.get(i).id; }
    }
}
