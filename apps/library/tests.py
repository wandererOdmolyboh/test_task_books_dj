from django.test import TestCase

from apps.library.models import Book


class BookModelTest(TestCase):
    tmp_data = None

    @classmethod
    def setUpTestData(cls):
        tmp_data = {
            'title': 'title_Book',
            'author': 'tom',
            'published_date': '2024-01-01',
            'isbn': '911112',
            'pages': 200,
            'cover': None,
            'language': 'uk'
        }
        Book.objects.create(**tmp_data)
        tmp_data['isbn'] = '911113'
        Book.objects.create(**tmp_data)

        tmp_data['isbn'] = '111111'
        tmp_data['author'] = 'author_author'
        cls.book = Book.objects.create(**tmp_data)

        for i in range(1, 12):
            tmp_data["isbn"] = str(int(tmp_data["isbn"]) + i)
            tmp_data["title"] = tmp_data["title"] + str(i)
            Book.objects.create(**tmp_data)
        cls.book_count_start = Book.objects.count()

    def test_create_book(self):
        data = {
            'title': 'New Book',
            'author': 'New Author',
            'published_date': '2025-01-01',
            'isbn': '9113314',
            'pages': 300,
            'cover': '',
            'language': 'ca'
        }
        response = self.client.post('/books/', data)
        self.assertEqual(response.status_code, 201)  # 201 is the status code for 'created'

        book = Book.objects.get(isbn=data['isbn'])
        self.assertEqual(book.title, data['title'])
        self.assertEqual(book.author, data['author'])
        self.assertEqual(str(book.published_date), data['published_date'])
        self.assertEqual(book.pages, data['pages'])
        self.assertEqual(book.cover, data['cover'])
        self.assertEqual(book.language, data['language'])
        book_count = Book.objects.count()
        self.assertEqual(self.book_count_start + 1, book_count)

    def test_title_content(self):
        response = self.client.get(f'/books/{self.book.id}/')

        self.assertEqual(response.status_code, 200)

        book = response.json()

        self.assertEqual(book['title'], self.book.title)
        self.assertEqual(book['author'], self.book.author)
        self.assertEqual(book['published_date'], str(self.book.published_date))
        self.assertEqual(book['isbn'], self.book.isbn)
        self.assertEqual(book['pages'], self.book.pages)
        self.assertEqual(book['cover'], self.book.cover)
        self.assertEqual(book['language'], self.book.language)

    def test_update_book(self):
        new_title = 'Updated Title'
        data = {
            'title': new_title,
            'author': self.book.author,
            'published_date': str(self.book.published_date),
            'isbn': self.book.isbn,
            'pages': self.book.pages,
            'cover': self.book.cover,
            'language': self.book.language
        }
        response = self.client.put(f'/books/{self.book.id}/', data, content_type='application/json')
        self.assertEqual(response.status_code, 200)  # 200 is the status code for 'ok'

        book = Book.objects.get(id=self.book.id)
        self.assertEqual(book.title, new_title)

    def test_delete_book(self):
        response = self.client.delete(f'/books/{self.book.id}/')
        self.assertEqual(response.status_code, 204)  # 204 is the status code for 'no content'

        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(id=self.book.id)

    def test_pagination(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)

        books = response.json()
        self.assertEqual(len(books['results']), 10)

        response = self.client.get('/books/', {'page': 5, 'page_size': 3})
        self.assertEqual(response.status_code, 200)

        books = response.json()
        self.assertEqual(len(books['results']), 2)

    def test_filter_by_author(self):
        response = self.client.get('/books/', {'search': 'tom'})
        self.assertEqual(response.status_code, 200)

        books = response.json()

        for book in books['results']:
            self.assertEqual(book['author'], 'tom')
            self.assertNotEqual(book['author'], 'author_author')
