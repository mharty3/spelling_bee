import app
import unittest


class TestApp(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_home(self):
        response = self.app.get('/')
        # Make your assertions
        self.assertEqual(response.status_code, 200)


    def test_api_no_args(self):
        response = self.app.get('/api/spelling_bee')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Error:", response.data)


    def test_api_with_letters(self):
        response = self.app.get('/api/spelling_bee?letters=avngurd')

        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        self.assertIn('all_words', data.keys())
        self.assertIn('pangrams', data.keys())
        self.assertIn('vanguard', data['pangrams'])
        self.assertEqual(len(data['all_words']), 92)
   

if __name__ == "__main__":
    unittest.main()