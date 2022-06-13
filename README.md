# Pets App

Pets Application is a Backend application ( REST API ) with Django Framework that contains :

- CRUD User.
- CRUD Pets.
- Authentication & Authorization.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Django.

```bash
source venv/bin/activate
pip3 install -r requirements.txt

```

## Install Environment

```bash
./manage.py makemigrations
./manage.py migrate
```

## Run Project

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Conclusion

After you run the application you will be able to connect to it by listening to the
http://localhost:8000/docs

## API Documentation

- (GET) http://localhost:8000/api/pets : List of pets
- (GET) http://localhost:8000/api/pets/id=1 : Get pet by id
- (POST) http://localhost:8000/api/pets/create : Add a pet
- (GET) http://localhost:8000/api/users : List of users
- (POST) http://localhost:8000/api/users : Subscribe
- (POST) http://localhost:8000/api/Auth : Authentication

## License

[MIT](https://choosealicense.com/licenses/mit/)
