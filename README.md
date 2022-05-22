# soa-graphql

# Запуск (без докера)
1. Поднимаем базу
```docker run -d --name postgres -e POSTGRES_HOST_AUTH_METHOD=trust -p 5432:5432 -v /var/folders/mount:/var/lib/postgresql/data postgres:12-alpine```
2. Создаем юзера `db_user`
```create user db_user```
3. создаем базу `mafia_game`
```create database mafia_game owner db_user```
4. Устанавливаем зависимости
```pip3 install -r requirements.txt```
5. Запускаем приложение
```PYTHONPATH=. python3 app/main.py```

# Выполненные пункты
Все кроме последнего
