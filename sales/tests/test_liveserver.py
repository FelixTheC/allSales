from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class SalesBackendTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(SalesBackendTest, cls).setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(SalesBackendTest, cls).tearDownClass()

    def test_connect(self):
        url = 'http://localhost:8000/sales/listsorders'
        self.selenium.get(url)
        self.selenium.find_element_by_id('id_customer_staff')