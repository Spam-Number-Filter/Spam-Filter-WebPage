<h1 align="center">
  Spam Filter Web Page ☎️
</h1>

[![Flake8 Linter](https://github.com/Spam-Number-Filter/Spam-Filter-WebPage/workflows/Flake8%20lint%20check/badge.svg)](https://github.com/Spam-Number-Filter/Spam-Filter-WebPage/actions/workflows/flake8-lint.yml)
[![Unit Tests](https://github.com/Spam-Number-Filter/Spam-Filter-WebPage/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/Spam-Number-Filter/Spam-Filter-WebPage/actions/workflows/unit-tests.yml)
[![Behavior Tests](https://github.com/Spam-Number-Filter/Spam-Filter-WebPage/workflows/Behavior%20Tests/badge.svg)](https://github.com/Spam-Number-Filter/Spam-Filter-WebPage/actions/workflows/behavior-tests.yml)
[![Deploy to Heroku](https://github.com/Spam-Number-Filter/Spam-Filter-WebPage/actions/workflows/deploy-heroku.yml/badge.svg)](https://github.com/Spam-Number-Filter/Spam-Filter-WebPage/actions/workflows/deploy-heroku.yml)

## Summary

- [Getting Started](#getting-started-)
- [Running locally with docker](#running-with-docker-and-using-postgres-as-database-)
- [Deployment to Heroku](#deploy-to-heroku-)
- [License](#license-)
- [Contributing](#contributing-)

## Getting Started 🔍

These instructions will give you a copy of the project up and running on your local machine for development and testing
purposes. See deployment for notes on deploying the project on a live system and the docker notes for running the
project on a container.

First of all, be aware that it is recommended to create a python virtual environment for installing the project
dependencies!
After you have created the environment, run the following command for installing the running dependencies:

```bash
pip install -r requirements.txt
```

If you want to install the development dependencies (which installs the linter, test runner, test coverage tools, etc)
run the following command:

```bash
pip install -r .github/dev-requirements.txt
```

Once installed, you have to run the following commands for creating and migrating the database:

```bash
python manage.py collectstatic --noinput
python manage.py migrate --run-syncdb 
python manage.py migrate
```

Finally, you can run the server with the following command:

```bash
python manage.py runserver
```

In order to access the sqlite database as admin, the already created superuser can be used. The credentials are the
following:

**User:** admin

**Password:** admin

## Running with docker and using postgres as database 🐳

First, build the docker image with the following command:

```bash
docker-compose build
```

Then, start the docker container with the following command:

```bash
docker-compose up
```

When booting the containers (both the project one and the data base one) for the first time, it may fail due to bad
order of execution. If that happens, booting a second time should fix it.
When the docker has finished booting and everything is okey, there will be an instance of django running on localhost at
port 8000.

### Adding a DB superuser inside the docker container 👤💾

Before accessing the data base (as admin), an admin user must be created. In order to create it inside the django
instance use:

```bash
docker exec -it django python manage.py createsuperuser
```

## Deploy to Heroku 🌎

For deploying to heroku, we've configured two github workflows which are run in the following contexts:

- Main workflow: When a commit get's pushed to the master branch, it will deploy the current branch to the heroku
  production environment.
- Develop workflow: When a commit get's pushed to the develop branch, it will deploy the current branch to the heroku
  development environment.

## License 📖

The project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for more information.

## Contributing 🧑‍🤝‍🧑

Please read [the CONTRIBUTING.md](.github/CONTRIBUTING.md) for details on our code of conduct, and the process for
submitting pull requests to us.
