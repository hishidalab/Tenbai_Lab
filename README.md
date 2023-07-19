# Tenbai_Lab

### 使い方
```
### 起動時
docker compose up -d
docker compose exec app /bin/bash
./mahou.sh
python -m pip install Pillow
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata fixture1.json
python manage.py runserver 0.0.0.0:8888
http://localhost:8888/pengin/login/

### docker落とし方
docker compose down -v

```
