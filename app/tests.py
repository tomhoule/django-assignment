from django.test import TestCase
from django.test.client import Client
from django.test.utils import override_settings
import re
from app import models


# We force debug mode in order to let template errors throw and crash the tests
@override_settings(DEBUG=True)
class Pages(TestCase):
    """
    End-to-end tests for the routes.
    """

    def setUp(self):
        self.client = Client()
        self.site = models.Site.objects.create(name="Some")
        models.Site.objects.create(name="Some other")
        models.DataEntry.objects.create(
            site=self.site,
            a_value=12.0,
            b_value=180.0,
            date="1969-08-24"
        )

    def tearDown(self):
        models.Site.objects.all().delete()

    def test_homepage_renders(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)

    def test_sites_page_renders(self):
        res = self.client.get("/sites")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"<h1>Sites</h1>", res.content)

    def test_homepage_and_sites_page_are_the_same(self):
        home = self.client.get("/").content
        sites = self.client.get("/sites").content
        self.assertEqual(home, sites)

    def test_homepage_table_has_the_right_number_of_rows(self):
        res = self.client.get("/sites")
        sites_count = models.Site.objects.count()
        # This is a bit of a hack. We could parse the returned html instead.
        matches = re.findall(r'class="site-row"', res.content.decode())
        self.assertEqual(sites_count, len(matches))

    def test_summary_page_renders(self):
        res = self.client.get("/summary")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"<h1>Summary</h1>", res.content)

    def test_site_page_renders(self):
        res = self.client.get("/sites/{}".format(self.site.id))
        self.assertEqual(res.status_code, 200)
        self.assertIn(self.site.name.encode(), res.content)

    def test_site_page_tables_has_the_right_number_of_rows(self):
        res = self.client.get("/sites/{}".format(self.site.id))
        matches = re.findall(r'class="dataentry-row"', str(res.content))
        self.assertEqual(len(matches), 1)  # TODO: make this more robust


class Models(TestCase):
    """
    Test that the models themselves behave correctly.
    """

    def setUp(self):
        self.random_site = models.Site.objects.create(name="Random")
        self.entry = models.DataEntry.objects.create(
            site=self.random_site,
            a_value=12.0,
            b_value=180.0,
            date="1969-08-24"
        )

    def tearDown(self):
        self.random_site.delete()

    def test_sites_are_named_properly(self):
        self.assertIn("Random Site", str(self.random_site))

    def test_data_entry_str_method_works(self):
        self.assertIn("Random", str(self.entry))
