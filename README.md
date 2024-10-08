# Library API

This is an API for managing books in a library, developed as a test task.

## Main Features

- Create a book (POST /books/)
- Get a list of books with the ability to filter by author, year of publication, and language (GET /books/)
- Get detailed information about a book by its ID (GET /books/{id}/)
- Update information about a book (PUT /books/{id}/)
- Delete a book (DELETE /books/{id}/)

## Technologies

- Python
- Django
- Django REST Framework
- PostgreSQL
- Swagger documentation

## Installation and Running

1. Clone the repository to your local machine.
2. Configure the environment in `.env`. Yoc can start local or by docker-compose. For local start use `HOST=localhost`:
```ini
NAME=bookstore
USER=root
PASSWORD=root
# HOST=localhost # for local start or use docker-compose
HOST postgres
PORT=5432
```
3. Install the dependencies using:
```shell 
pip install -r requirements.txt
```

4. Perform migrations using:
```shell
python manage.py migrate
```
5. Start the server using:
```shell
python manage.py runserver
```
6. Start the server using:
```shell
python manage.py loaddata src/apps/library/fixtures/books.json
```

## Accessing the Application

You can access the application by navigating to `http://localhost:8000` in your web browser. This will take you to the main page of the application.

## Documentation with Swagger

Open the Swagger UI by going to `http://localhost:8000/docs/` in your web browser.


## Testing

To run unit tests, use the command `python manage.py test`.
