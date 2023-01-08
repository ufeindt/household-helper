from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class DjangoFreshInstallTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get("http://localhost:8000")
        self.assertIn(
            "The install worked successfully! Congratulations!",
            self.browser.title,
        )
