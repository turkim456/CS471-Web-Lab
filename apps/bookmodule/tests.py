from django.contrib.staticfiles import finders
from django.test import SimpleTestCase
from django.urls import reverse


class BookPagesTests(SimpleTestCase):
    def test_pages_share_layout(self):
        pages = [
            ("books.index", [], "bookmodule/index.html", "My First Index HTML Page"),
            ("books.list_books", [], "bookmodule/list_books.html", "List of Books"),
            ("books.aboutus", [], "bookmodule/aboutus.html", "About Us"),
            ("books.view_one_book", [1], "bookmodule/one_book.html", "Show one Book"),
        ]
        for name, args, template, title in pages:
            with self.subTest(page=name):
                response = self.client.get(reverse(name, args=args))
                self.assertEqual(response.status_code, 200)
                for shared in [template, "layouts/base.html", "includes/header.html", "includes/footer.html"]:
                    self.assertTemplateUsed(response, shared)
                self.assertContains(response, f"<title>{title}</title>")
                self.assertContains(response, "/static/styles.css")
                self.assertContains(response, "/static/qu-icon.png")
                self.assertContains(response, 'href="/books/"')
                self.assertContains(response, 'href="/books/list_books/"')
                self.assertContains(response, 'href="/books/aboutus/"')

    def test_active_navigation(self):
        for url, label in [("/books/", "Home"), ("/books/list_books/", "List Books"),
                           ("/books/aboutus/", "About"), ("/books/1/", "List Books")]:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertContains(response, 'class="active"', count=1)
                self.assertRegex(response.content.decode(), 'class="active" href="[^"]+">' + label)

    def test_book_links_and_images(self):
        response = self.client.get("/books/list_books/")
        self.assertContains(response, 'href="/books/1/"', count=2)
        for image in ["book1.jpg", "book2.jpg", "book3.jpg"]:
            self.assertContains(response, f'/static/{image}')
        response = self.client.get("/books/1/")
        self.assertContains(response, "Internet &amp; World Wide Web How to Program")
        self.assertContains(response, 'href="/books/list_books/">Go Back')

    def test_static_assets_exist(self):
        for name in ["styles.css", "qu-icon.png", "book1.jpg", "book2.jpg", "book3.jpg"]:
            with self.subTest(asset=name):
                self.assertIsNotNone(finders.find(name))

    def test_lab3_number_routes(self):
        for number in [0, 3, 10]:
            self.assertContains(self.client.get(f"/books/index2/{number}/"), f"value1 = {number}")
        self.assertContains(self.client.get("/books/index2/text/"), "error, expected val1 to be integer", status_code=400)
