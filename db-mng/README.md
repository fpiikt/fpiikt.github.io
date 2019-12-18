## Администрирование систем управления базами данных

### Группа: P42552



### Практическое задание 1

1. Инсталлировать *Docker Engine - Community* на одну из предложенных платформ (Windows, Linux, MacOS): [https://docs.docker.com](https://docs.docker.com). Рекомендуется использовать платформу Ubuntu или в ОС Windows инсталлировать VirtualBox и установить Docker в виртуальную машину на основе Ubuntu.

2. Изучить материалы, опубликованные по адресу: [https://docs.docker.com/engine/docker-overview/](https://docs.docker.com/engine/docker-overview/) и выполнить все 8 частей по ссылке [https://docs.docker.com/compose/gettingstarted/](https://docs.docker.com/compose/gettingstarted/)

3. Реализовать два дополнительных маршрута (помимо корневого маршрута ```@app.route('/')```):

   1. Для одного из них реализовать функцию декремента (уменьшения) счетчика на 1.
   2. Для второго — реализовать функцию сброса (обнуления) счетчика.

   

### Практическое задание 2

1. Реализовать функционал, предложенный в практическом задании 1 с использованием СУБД SQLite. Изучите справочные материалы: 
   - https://docs.python.org/3/library/sqlite3.html —официальная стандартная библиотека Python для взаимодействия с SQLite.
   - https://python-scripts.com/sqlite — пример работы с СУБД SQLite.
   - https://ru.wikibooks.org/wiki/SQLAlchemy — альтернативный (модулю ```sqlite```) способ работы с СУБД; SQLAlchemy позволяет реализовать ORM (удобный механизм, позволяющий описывать структуры баз данных и способы взаимодействия с ними прямо в синтаксисе языка программирования, не используя запросы языка БД).
2. Используя репозиторий https://hub.docker.com, найти образы для наиболее популярных серверных SQL и noSQL систем управленя базами данных (например, MySQL или MariaDB, PostgresSQL, MongoDB).
3. Выбрать одну какую-либо СУБД и переписать фрагмент приложения из практического задания 1 с использованием этой СУБД. Изучите соответствующие справочные материалы: 
   - MongoDB: [начало работы с СУБД](https://docs.mongodb.com/manual/tutorial/getting-started/) (базовые команды), [работа с СУБД на Python](https://docs.mongodb.com/ecosystem/drivers/pymongo/).
   - MariaDB: [работа с СУБД на Python](https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/).
   - PostgresSQL: [работа с СУБД на Python](https://lectureswww.readthedocs.io/6.www.sync/2.codding/9.databases/1.postgres.html), возможно [использовать SQLAlchemy](https://docs.sqlalchemy.org/en/13/dialects/postgresql.html).