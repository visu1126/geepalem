from django.test import TestCase
from .models import goods

class Unittests (TestCase):
    def setup(self):
        goods.objects.create(name='Knockout',
                             description='Knockouts feel of distress and gives back lost energy',
                             item_cost='199.00',
                             stock_qty='60.00',
                             volume='11940.00')
    def test_get_method(self):
        url = "http://127.0.0.1:8000/students/"
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        qs = goods.objects.filter(name='Knockout')
        self.assertEqual(qs.count(), 0)