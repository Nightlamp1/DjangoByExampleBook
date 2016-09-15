from django.test import TestCase
from selenium import webdriver

class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_blog_page_displays_correctly(self):
        self.browser.get('http://localhost:8000/blog/')

        self.assertIn('My Blog', self.browser.title)
