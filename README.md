### Simple API for a blog site

A separate API application for my other youtube_project project. Since there are some flaws, it was decided to put it in a separate repository.
The current API has the ability to work CRUD with the posts application.


### Quickstart a project:

Clone the repository and go to it on the command line:

```
git clone https://github.com/yandex-praktikum/kittygram.git
```

```
cd kittygram
```

Create and activate a virtual environment:

```
python3 -m venv env
```

```
source env/bin/activate
```

Install dependencies from a file requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Perform migrations:

```
python3 manage.py migrate
```

Start a server:

```
python3 manage.py runserver
```


### Examples of API requests:

# Get posts:

GET request:
```
http://127.0.0.1:8000/api/v1/posts/
```
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

# Get comments:

GET request:
```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```
```
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```

# Get groups:

GET request:
```
http://127.0.0.1:8000/api/v1/groups/
```
```
[
  {
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
  }
]
```

# Get following:

GET request:
```
http://127.0.0.1:8000/api/v1/follow/
```
```
[
  {
    "user": "string",
    "following": "string"
  }
]
```

# Get JWT-token:

POST request:
```
http://127.0.0.1:8000/api/v1/jwt/create/
```
Payload:
```
{
  "username": "string",
  "password": "string"
}
```
```
{
"refresh": "string",
"access": "string"
}
```
