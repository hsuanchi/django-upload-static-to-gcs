# django-upload-static-to-gcs

## Launch on local runtime
Create your virtual environment
```
$ python3 -m venv venv
```

And enable virtual environment
```
$ . venv/bin/activate
```

Install requirements
```
$ pip install -r requirements.txt 
```

Run Django
```
$ python3 manager.py runserver
```

## 1. 將圖片存至本地

### 1.1 Run
http://127.0.0.1:8000/local/
<img src="https://github.com/hsuanchi/django-upload-static-to-gcs/blob/main/doc/local folder.jpg">

## 2. 將圖片存至 Google Cloud Storage

### 2.1 Requirement install

```
google-cloud-storage
django-storages
```

### 2.2 Get Google Storage key
申請憑證：https://console.cloud.google.com/apis/credentials

### 2.3 Run
http://127.0.0.1:8000/local/
<img src="https://github.com/hsuanchi/django-upload-static-to-gcs/blob/main/doc/google_storage.jpg">
