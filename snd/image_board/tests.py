from django.test import TestCase

class TestCalls(TestCase):
    def test_call_view_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
