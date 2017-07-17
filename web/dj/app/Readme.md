## Django Setup

- `mkdir dj`: for all django projects
- `cd dj`
- `django-admin startproject hello .`: create project hello
- `python manage.py runserver 0.0.0.0:8000`: run


## More...

- `python manage.py migrate   # 创建表结构`
- $ python manage.py makemigrations TestModel  # 让 Django 知道我们在我们的模型有一些变更
- $ python manage.py migrate TestModel   # 创建表结构

## createsuperuser

python manage.py createsuperuser