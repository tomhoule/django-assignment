from django.test import TestCase
from django.test.client import Client
from django.test.utils import override_settings


# We force debug mode in order to let template errors throw and crash the tests
@override_settings(DEBUG=True)
class Pages(TestCase):

    def setUp(self):
        self.client = Client()

    def test_homepage_renders(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"<h1>Hello", res.content)

    def test_sites_page_renders(self):
        res = self.client.get("/sites")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"<h1>Hello", res.content)

    def test_homepage_and_sites_page_are_the_same(self):
        home = self.client.get("/").content
        sites = self.client.get("/sites").content
        self.assertEqual(home, sites)

    def test_summary_page_renders(self):
        res = self.client.get("/summary")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"<h1>Hello", res.content)
