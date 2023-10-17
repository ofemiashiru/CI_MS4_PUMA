from django.test import TestCase
from products.models import Product

import random

class TestViews(TestCase):

    def test_index(self):   

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        template = 'home/index.html'

        self.assertTemplateUsed(response, template)



