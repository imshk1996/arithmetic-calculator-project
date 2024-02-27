from django.test import TestCase, Client
from django.urls import reverse

class CalculatorViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_calculate_valid_expression(self):
        url = reverse('calculate')
        data = {'expression': '5+3-2'}
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], 6)

    def test_calculate_invalid_expression(self):
        url = reverse('calculate')
        data = {'expression': '5+3*2'}
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid expression', response.json()['error'])

    def test_calculate_missing_expression(self):
        url = reverse('calculate')
        response = self.client.post(url, {}, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Expression not provided', response.json()['error'])
