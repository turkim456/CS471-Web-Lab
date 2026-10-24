from django.test import SimpleTestCase


class BookViewsTests(SimpleTestCase):
    def test_greeting_uses_template_and_query_parameter(self):
        for query, expected in [({}, "world!"), ({"name": ""}, "world!"),
                                ({"name": "Mousa"}, "Mousa"),
                                ({"name": "Dr. Faisal"}, "Dr. Faisal")]:
            with self.subTest(query=query):
                response = self.client.get("/books/", query)
                self.assertTemplateUsed(response, "bookmodule/index.html")
                self.assertContains(response, f"<h1>Hello from {expected}!</h1>")

    def test_greeting_escapes_html(self):
        response = self.client.get("/books/", {"name": "<script>alert(1)</script>"})
        self.assertContains(response, "&lt;script&gt;")
        self.assertNotContains(response, "<script>")

    def test_integer_path_parameter(self):
        for value in [0, 3, 10]:
            with self.subTest(value=value):
                response = self.client.get(f"/books/index2/{value}/")
                self.assertContains(response, f"value1 = {value}")

    def test_text_path_parameter_returns_error(self):
        response = self.client.get("/books/index2/text/")
        self.assertContains(response, "error, expected val1 to be integer", status_code=400)

    def test_book_details(self):
        for book_id, title, author in [
            (123, "Continuous Delivery", "J. Humble and D. Farley"),
            (456, "Secrets of Reverse Engineering", "E. Eilam"),
        ]:
            with self.subTest(book_id=book_id):
                response = self.client.get(f"/books/{book_id}")
                self.assertTemplateUsed(response, "bookmodule/show.html")
                self.assertContains(response, f"ID: {book_id}")
                self.assertContains(response, title)
                self.assertContains(response, author)

    def test_unknown_book_returns_404(self):
        self.assertEqual(self.client.get("/books/999").status_code, 404)
