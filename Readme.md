Test Project to check proper Android vs Django Interface

Database has tables
1. Login table with fields
   a) email_id : validation similar to "abc@example.com"
   b) password : character field
   c) mobile_number : character field
   d) hint  : character field
   e) id    : integer field (django default)

2. About table with fields
   a) about : character field
   b) id    : integer field (django default)

URL Schemes include
1. /register : to register new user
2. /login    : login with existing user (email_id & password)
3. /about    : input comment/about 
4. /display  : diplays all "About Table" fields in json

Security:
Adds a csrf_exempt decorator on every django view so as to easily
facilitate the android django post interface

Instruction to run:
* Requirements
  Virtualenv 1.11.6
  Django 1.9.1
  Python 3.4.3
[Linux]
1. virtualenv -p python3.4 env
2. source env/bin/activate
3. pip install Django==1.9.1
4. cd androidlogin/  (project root where the manage.py exists)
5. ./manage.py migrate
6. ./manage.py makemigrations login
7. ./manage.py migrate login
8. ./manage.py createsuperuser ( grants acces to django admin )
9. ./manage.py runserver