import unittest
from unittest.mock import patch

from dashboard import backend


class TestDashboard(unittest.TestCase):
    def setUp(self):
        self.app = backend.app.test_client()

    @patch('openai.ChatCompletion.create')
    def test_send_request(self, mock_create):
        mock_create.return_value = {'id': 'test', 'object': 'chat.completion'}
        response = self.app.post('/api/request', data={'content': 'test content'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'id': 'test', 'object': 'chat.completion'})

    @patch('openai.ChatCompletion.list')
    def test_get_response(self, mock_list):
        mock_list.return_value = {'data': [{'id': 'test', 'object': 'chat.completion'}]}
        response = self.app.get('/api/response')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'data': [{'id': 'test', 'object': 'chat.completion'}]})

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
