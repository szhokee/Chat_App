Chat_App
Getting Started
Clone the repository onto your local machine:
git clone git@github.com:xralphlauren/Chat_drf.git

Create a virtual environment and install the required dependencies:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

You can use the already created database or delete the old one and create your own.
If you choose to create your database:
python3 manage.py makemigrations
python3 manage.py migrate

Run the development server:
python3 manage.py runserver

All requests to the server require created users. There are already 5 users in my database, if you have created your database, please create some users
First create an admin account:
python3 manage.py createsuperuser
Next, go to the admin panel, use your newly created account
http://127.0.0.1:8000/admin
Sample requests for Chat_drf
before making requests to the server. You need to get a jwt token. To do this, go do the following:
go to url: http://127.0.0.1:8000/api/token/
Enter your login/password
Copy access token
Further in your requests, you need to take the following value in the header: {'Authorization': 'Bearer your_token'}
Creating or deleting threads (Post/Delete)
http://127.0.0.1:8000/api/create_delete_thread/1/2
http://127.0.0.1:8000/api/create_delete_thread/1/3
http://127.0.0.1:8000/api/create_delete_thread/1/4
http://127.0.0.1:8000/api/create_delete_thread/1/5
http://127.0.0.1:8000/api/create_delete_thread/2/3
http://127.0.0.1:8000/api/create_delete_thread/2/5
http://127.0.0.1:8000/api/create_delete_thread/5/3
http://127.0.0.1:8000/api/create_delete_thread/5/4

Getting a list of threads for a user (with the latest message)
http://127.0.0.1:8000/api/get_threads/1
http://127.0.0.1:8000/api/get_threads/2
http://127.0.0.1:8000/api/get_threads/3
http://127.0.0.1:8000/api/get_threads/4
http://127.0.0.1:8000/api/get_threads/5

Get a list of messages for thread or create a new one (Post/Get)
If you want to create messages, you must also specify the sender ID and message text in the request body.
Example: {"sender": 2, "message_text": "some random Text 555"}
http://127.0.0.1:8000/api/get_create_message/1
http://127.0.0.1:8000/api/get_create_message/2
http://127.0.0.1:8000/api/get_create_message/3

Change the status of a message or messages to is_read - True
Specify a list with message ID in the request body. Request body example, for messages with id 5,6,7 {"message_id": [5,6,7]}
http://127.0.0.1:8000/api/set_message_status

Getting the number of unread messages per user
http://127.0.0.1:8000/api/count_unread_message/1
http://127.0.0.1:8000/api/count_unread_message/2
http://127.0.0.1:8000/api/count_unread_message/3
http://127.0.0.1:8000/api/count_unread_message/4
http://127.0.0.1:8000/api/count_unread_message/5