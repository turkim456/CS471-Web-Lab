# CS471 Web Lab 3

Django views, URL parameters, and HTML templates.

## Run

```powershell
python -m venv .venv
python -m pip --python .venv/Scripts/python.exe install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py runserver
```

## Pages

- `/books/`
- `/books/?name=Turki`
- `/books/index2/3/`
- `/books/index2/text/`
- `/books/123`
- `/books/456`

## Tests

```powershell
.\.venv\Scripts\python.exe manage.py test apps.bookmodule
```
