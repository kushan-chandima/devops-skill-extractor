import unittest
from src.scrapers.linkedin_scraper import LinkedInScraper
from src.scrapers.glassdoor_scraper import GlassdoorScraper

class TestLinkedInScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = LinkedInScraper()

    def test_fetch_data(self):
        data = self.scraper.fetch_data("DevOps Engineer")
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    def test_parse_data(self):
        raw_data = [{"title": "DevOps Engineer", "skills": ["AWS", "Docker"]}]
        parsed_data = self.scraper.parse_data(raw_data)
        self.assertIn("AWS", parsed_data[0]['skills'])
        self.assertIn("Docker", parsed_data[0]['skills'])

class TestGlassdoorScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = GlassdoorScraper()

    def test_fetch_data(self):
        data = self.scraper.fetch_data("DevOps Engineer")
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    def test_parse_data(self):
        raw_data = [{"title": "DevOps Engineer", "skills": ["Kubernetes", "CI/CD"]}]
        parsed_data = self.scraper.parse_data(raw_data)
        self.assertIn("Kubernetes", parsed_data[0]['skills'])
        self.assertIn("CI/CD", parsed_data[0]['skills'])

if __name__ == '__main__':
    unittest.main()