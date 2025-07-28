import unittest
from crawl import normalize_url

class TestCrawl(unittest.TestCase):
    def test_normalize_url_capitals(self):
        input_url = "https://APP.example.com/PATH"
        expected = "app.example.com/path"
        actual = normalize_url(input_url)
        self.assertEqual(actual, expected)

    def test_normalize_url_slash(self):
        input_url = "https://app.example.com/path/"
        expected = "app.example.com/path"
        actual = normalize_url(input_url)
        self.assertEqual(actual, expected)

    def test_normalize_url_protocols(self):
        input_urls = ["https://app.example.com/path", "http://app.example.com/path"]
        expected = "app.example.com/path"
        for url in input_urls:
            actual = normalize_url(url)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
