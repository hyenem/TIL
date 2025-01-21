<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>singleFileUploadForm</title>
</head>
<body>
	<form action="/singleFileUpload" method="POST" enctype="multipart/form-data">
		<input type="file" name="file">
		<button>파일 업로드</button>
	</form>
</body>
</html>