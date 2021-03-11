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



## Method 1. Save image to local folder

### Run Django
```
$ python3 manager.py runserver
```

http://127.0.0.1:8000/cloud/
<img src="https://github.com/hsuanchi/django-upload-static-to-gcs/blob/main/doc/local folder.jpg">

## Method 2. Save image to Google Cloud Storage

### Requirement install

```
[google-cloud-storage](https://pypi.org/project/google-cloud-storage/)
[django-storages](https://pypi.org/project/django-storages/)
```

### Get Google Storage credentials
Get json key：https://console.cloud.google.com/apis/credentials

### Run Django
```
$ python3 manager.py runserver
```

http://127.0.0.1:8000/local/
<img src="https://github.com/hsuanchi/django-upload-static-to-gcs/blob/main/doc/google_storage.jpg">
