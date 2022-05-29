# Приложение для обработки запросов
## Запуск контейнера
Для запуска контейнера вам необходимо выполнить:
```sh
docker-compose up --build
```
--------------------------------
Адрес для подключение к запущенному приложению:

```sh
http://localhost:8008/docs#/default/
```
--------------------------------
## Функционал
При переходе по указанному выше адресу можно найти 4 поля
- '/search'
- '/query'
- '/selected'
- '/drop_by_id'
--------------------------------
В разделе /search следует указать слово или выражение для поиска в таблице. Ответом будет массив строк (до 20) упорядоченный по дате создания
- id
- rubrics
- text
- created_date
-------------------------------
В разделе '/query' при получения строки query выводится ответ на запрос без ограничений.
-------------------------------
В разделе '/selected' выводятся первые 20 строчек таблицы по дате создания
-------------------------------
В разделе '/drop_by_id' передается id - числовое выражение id строки, которая будет удалена.
_______________________________
Таблица сохраняет данные.
