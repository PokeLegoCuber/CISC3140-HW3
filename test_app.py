import unittest
from hw3 import app


class HomeViewTest(unittest.TestCase):

	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/', content_type='html/text')
		self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
