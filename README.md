# Chat_App

# Getting Started
	Clone the repository onto your local machine:
	git clone git@github.com:xralphlauren/Chat_drf.git

# Создайте виртуальную среду и установите необходимые зависимости:
	python3 -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt

# Вы можете использовать уже созданную базу данных или удалить старую и создать свою.
Если вы решили создать свою базу данных:
	./manage.py makemigrations
	./manage.py migrate

# Запустите сервер разработки:
	./manage.py runserver

# Все запросы к серверу требуют созданных пользователей. В моей базе данных уже есть 5 пользователей, если вы создали свою базу данных, создайте несколько пользователей.
# Сначала создайте учетную запись администратора:
	./manage.py createsuperuser

# Далее заходим в админ панель, используем только что созданный аккаунт
	http://127.0.0.1:8000/admin
# Примеры запросов для Chat_App
	перед выполнением запросов к серверу. Вам нужно получить токен jwt. Для этого выполните следующие действия:
	http://127.0.0.1:8000/account/register/
	

# Далее в ваших запросах нужно принимать в шапке следующее значение: {'Authorization': 'Bearer your_token'}
	Создание или удаление тем (Post/Delete)
	
	http://127.0.0.1:8000/chat/api/create_delete_thread/1/2
	http://127.0.0.1:8000/chat/api/create_delete_thread/1/3
	http://127.0.0.1:8000/chat/api/create_delete_thread/1/4
	http://127.0.0.1:8000/chat/api/create_delete_thread/1/5
	http://127.0.0.1:8000/chat/api/create_delete_thread/2/3
	http://127.0.0.1:8000/chat/api/create_delete_thread/2/5
	http://127.0.0.1:8000/chat/api/create_delete_thread/5/3
	http://127.0.0.1:8000/chat/api/create_delete_thread/5/4

	Получение списка тем для пользователя (с последним сообщением)
	http://127.0.0.1:8000/chat/api/get_threads/1
	http://127.0.0.1:8000/chat/api/get_threads/2
	http://127.0.0.1:8000/chat/api/get_threads/3
	http://127.0.0.1:8000/chat/api/get_threads/4
	http://127.0.0.1:8000/chat/api/get_threads/5


# Получить список сообщений для треда или создать новый (Post/Get)
	Если вы хотите создавать сообщения, вы также должны указать идентификатор отправителя и текст сообщения в теле запроса. 53 Пример: {"sender": 2, "message_text": "какой-то случайный текст 555"}
	http://127.0.0.1:8000/chat/api/get_create_message/1
	http://127.0.0.1:8000/chat/api/get_create_message/2
	http://127.0.0.1:8000/chat/api/get_create_message/3

# Изменить статус сообщения или сообщений на is_read — True 58 Укажите список с идентификатором сообщения в теле запроса. Пример тела запроса для сообщений с идентификатором 5,6,7 {"message_id": [5,6,7]}
	http://127.0.0.1:8000/api/set_message_status


# Получение количества непрочитанных сообщений на пользователя
	http://127.0.0.1:8000/chat/api/count_unread_message/1
	http://127.0.0.1:8000/chat/api/count_unread_message/2
	http://127.0.0.1:8000/chat/api/count_unread_message/3
	http://127.0.0.1:8000/chat/api/count_unread_message/4
	http://127.0.0.1:8000/chat/api/count_unread_message/5
