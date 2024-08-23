FROM python:3.12

ENV PYTHONUNBUFFERED 1
RUN mkdir /test_task_books_dj/src

ENV PYTHONPATH=/test_task_books_dj/src


WORKDIR /test_task_books_dj/src

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
