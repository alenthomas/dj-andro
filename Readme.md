# Simple app to test android django json connection

### Database has tables
1. Login table with fields
   * email_id : with validation similar to "abc@example.com"
   * password : character field
   * mobile_number : character field
   * hint  : character field
   * id    : integer field (django default)

2. About table with fields
   * about : character field
   * id    : integer field (django default)

### URL Schemes include
    * /register : to register new user
    * /login    : login with existing user (email_id & password)
    * /about    : input comment/about 
    * /display  : diplays all "About Table" fields in json

### Security:

Adds a csrf_exempt decorator on every django view so as to easily
facilitate the android django post interface

###  Requirements

     *  Virtualenv 1.11.6
     *  Django 1.9.1
     *  Python 3.4.3

### Instruction to run:

**Linux**
```sh
$ virtualenv -p python3.4 env
$ source env/bin/activate
$ pip install Django==1.9.1
$ cd dj-android/                 (project root where the manage.py exists)
$ ./manage.py migrate
$ ./manage.py makemigrations login
$ ./manage.py migrate login
$ ./manage.py createsuperuser    ( grants acces to django admin )
$ ./manage.py runserver
```