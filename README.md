<h1 align="center">
  Spam Filter Web Page ☎️
</h1>

![](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=whit)
![](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)

## Running locally with docker 🐳

When booting the containers (both the project one and the data base one) for the first time, it may fail due to bad order of execution. If that happens, booting a second time should fix it.

```
$ docker-compose up
```

When the docker has finished booting and everything is okey, there will be an instance of django running on localhost at port 8000. 


## Adding a DB superuser inside the docker container 👤💾

Before accessing the data base (as admin), an admin user must be created. In order to create it inside the django instance use: 

```
$ docker exec -it django python manage.py createsuperuser
```

## Dependencies ⚙️

Notice we have a dependencies file for each Docker Compose and Heroku, that is due to `django-heroku` package currently (2022-03-21) down on the pip package manager. This causes errors when configuring docker containers.

Issue will be fixed as soon as the package is available on pip packet manager.


