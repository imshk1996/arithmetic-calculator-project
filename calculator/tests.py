from django.test import TestCase
from rest_framework.test import APIClient

class CalculatorTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_valid_expression(self):
        data = {'expression': '10+5-3'}
        response = self.client.post('/api/calculate/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['result'], 12)

    def test_invalid_expression(self):
        data = {'expression': '10*5'}
        response = self.client.post('/api/calculate/', data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid expression', response.data['error'])

    def test_missing_operand(self):
        data = {'expression': '10+'}
        response = self.client.post('/api/calculate/', data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid expression: Missing operand after '+'", response.data['error'])

    def test_double_negative(self):
        data = {'expression': '--10+5'}
        response = self.client.post('/api/calculate/', data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid expression: Double negative at the beginning', response.data['error'])    

    def test_invalid_method(self):
        response = self.client.get('/api/calculate/')
        self.assertEqual(response.status_code, 405)
