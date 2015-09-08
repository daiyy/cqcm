from django.test import TestCase
from pydash.services import *

class TestServices(TestCase):
    "test case for services"

    def test_get_uptime(self):
        self.assertIsNotNone(get_uptime())

    def test_get_platform(self):
        self.assertIsNotNone(get_platform())
