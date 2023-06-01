# Tenbai_Lab

### 使い方
```
### 起動時
docker compose up -d
docker compose exec app /bin/bash
./mahou.sh
python manage.py migrate
python manage.py runserver 0.0.0.0:8888
http://localhost:8888/

### docker落とし方
docker compose down -v

```