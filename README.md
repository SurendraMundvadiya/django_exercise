# django_exercise

django_exercise is a Python project for create messages

## Installation

please install virtualenv

```bash
>>> pip install virtualenv
>>> python -m virtualenv env
>>> .\env\Scripts\activate

>>> git clone https://github.com/Surendra-Mundvadiya/django_exercise.git
>>> cd django_exercise
>>> pip install requirment.txt
>>> python manage.py runserver

```

## Usage

this project has four end point for you convenience

# SIGN UP

```api
API : http://127.0.0.1:8000/api/signup/
METHOD: POST
BODY: {
           "username":"rachel",
           "password":"test@123",
           "email":"rache@zane.com",
           "first_name":"rachel",
           "last_name":"zane"
      }
RETURN: status
```

# SIGN IN

```api
API : http://127.0.0.1:8000/api/signin/
METHOD: POST
BODY: {
          "username":"rachel",
          "password":"test@123"
      }
return: token
```

# SEND MESSAGE

```api
API : http://127.0.0.1:8000/api/send_message/
METHOD: POST
BODY: {
       "messages":"hello, world!"
      }
HEADER: {
         Authorization : Token b37d07dacc59370d8d92d9b8e14bbfb86d874d2c
        }

return: status
```

# GET MESSAGES

```api
API http://127.0.0.1:8000/api/get_messages/
MOETHOD: GET
HEADER: {
         Authorization : Token b37d07dacc59370d8d92d9b8e14bbfb86d874d2c
        }

return: messages
```
