from django.test import TestCase
from django.test.client import Client
from django.test.utils import override_settings

@override_settings(DEBUG=True)
class Misc(TestCase):

    def setUp(self):
        self.client = Client()

    def test_hello_world(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)
