package com.ssafy.fit.model;

public class Video {
	private int no;
	private String title;
	private String part;
	private String url;
	
	public Video(){}
	
	public Video(int no, String title, String part, String url) {
		this.no = no;
		this.title = title;
		this.part = part;
		this.url = url;
	}
	
	//getter setter 설정
	 public int getNo() {
		 return this.no;
	 }
	 
	 public void setNo(int no) {
		 this.no = no;
	 }
	 
	 public String getTitle() {
		 return this.title;
	 }
	 
	 public void setTitle(String title) {
		 this.title = title;
	 }
	 
	 public String getPart() {
		 return this.part;
	 }
	 
	 public void setPart(String part) {
		 this.part = part;
	 }
	 
	 public String getUrl() {
		 return this.url;
	 }
	 
	 public void setUrl(String url) {
		 this.url = url;
	 }
	 
	 public String toString() {
		 return "Video [no: " + no + ", title: " + title + ", part: " + part + ", url: " + url + "]";
	 }
	
	 
}
