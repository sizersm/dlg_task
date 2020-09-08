from main import app
import unittest

app.testing = True


class AppTests(unittest.TestCase):

    def test_total_view_result_code(self):
        with app.test_client() as client:
            # sends HTTP GET request to the application
            result = client.get('/total')

            # assert the status code of the response
            self.assertEqual(result.status_code, 200)

    def test_total_view_result_value(self):
        expected = {'total': 50000005000000}

        with app.test_client() as client:
            result = client.get('/total')

            # assert the json result of the response
            self.assertEqual(result.json, expected)
