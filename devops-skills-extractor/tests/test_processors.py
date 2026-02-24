import unittest
from src.processors.skills_analyzer import SkillsAnalyzer
from src.processors.data_cleaner import DataCleaner

class TestSkillsAnalyzer(unittest.TestCase):

    def setUp(self):
        self.data_cleaner = DataCleaner()
        self.skills_analyzer = SkillsAnalyzer()

    def test_analyze_skills(self):
        raw_data = [
            {"skills": ["Python", "Docker", "Kubernetes"]},
            {"skills": ["Python", "AWS", "Terraform"]},
            {"skills": ["Docker", "Kubernetes", "CI/CD"]}
        ]
        cleaned_data = self.data_cleaner.clean_data(raw_data)
        analysis_result = self.skills_analyzer.analyze_skills(cleaned_data)

        expected_result = {
            "Python": 2,
            "Docker": 2,
            "Kubernetes": 2,
            "AWS": 1,
            "Terraform": 1,
            "CI/CD": 1
        }

        self.assertEqual(analysis_result, expected_result)

    def test_empty_data(self):
        cleaned_data = self.data_cleaner.clean_data([])
        analysis_result = self.skills_analyzer.analyze_skills(cleaned_data)

        expected_result = {}
        self.assertEqual(analysis_result, expected_result)

if __name__ == '__main__':
    unittest.main()