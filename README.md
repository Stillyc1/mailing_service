# Проект по работе с банковскими операциями клиентов

## Описание: 
В проекте реализуем функции сортировки, преобразований банковских данных клиентов

## Установка:
1. клонируйте репозиторий через ssh
2. открывайте через pycharm
```
git@github.com:Stillyc1/course_project.git
```
2. устанавливайте зависимости из 
```
pyproject.toml
```

## Использование:
В пакете src реализованы модули для работы нашего приложения, а именно: 
1. external_api.py функции запроса курса валют, и получения курса акций, интересующих пользователя.
Данные по курсам и валютам хранятся в user_setting.json
2. utils.py набор функций для обработки информации по операциям клиента, а именно: подсчет суммы трат по всем картам,
подсчет кэшюэка по картам, вывод топ 5 транзакций за выбранный месяц, 
приветствие пользователя в зависимости от времени суток.
3. services.py функция для поисковой строки запроса от клиента, 
сортирует операции по ключевым данным(Описание или Категория)
4. reports.py реализованы функции для сортировки трат по категориям
5. views.py реализована функция обработки операций клиента с начала месяца по входную дату,
вывод информации в формате json, функция обрабатывает информацию, использует зависимые функции из других модулей

## Тестирование:
Функционал проекта тестируется в пакете tests

## Документация: 
Всё что сделано в этом проекте вы можете изучить на сайте [skypro](www.skypro.ru)

## Лицензии: 
Данный проект лицензирован, копирование и передача данных третьим лицам ничем не карается, но не поощеряется)
