import unittest
from src.extractors.skills_extractor import SkillsExtractor

class TestSkillsExtractor(unittest.TestCase):

    def setUp(self):
        self.extractor = SkillsExtractor()

    def test_extract_skills(self):
        # Mock data for testing
        mock_data = [
            {"job_title": "DevOps Engineer", "skills": ["AWS", "Docker", "Kubernetes"]},
            {"job_title": "Site Reliability Engineer", "skills": ["GCP", "Terraform", "Ansible"]}
        ]
        expected_skills = {"AWS", "Docker", "Kubernetes", "GCP", "Terraform", "Ansible"}
        
        extracted_skills = self.extractor.extract_skills(mock_data)
        
        self.assertEqual(extracted_skills, expected_skills)

    def test_empty_data(self):
        mock_data = []
        expected_skills = set()
        
        extracted_skills = self.extractor.extract_skills(mock_data)
        
        self.assertEqual(extracted_skills, expected_skills)

    def test_invalid_data_format(self):
        mock_data = [
            {"job_title": "DevOps Engineer", "skills": "AWS, Docker, Kubernetes"}
        ]
        
        with self.assertRaises(ValueError):
            self.extractor.extract_skills(mock_data)

if __name__ == '__main__':
    unittest.main()