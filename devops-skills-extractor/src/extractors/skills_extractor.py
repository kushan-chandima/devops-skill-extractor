class SkillsExtractor:
    def __init__(self):
        self.skills = []

    def extract_skills(self, job_postings):
        """Extract skills from job postings and return as a set."""
        all_skills = set()
        for posting in job_postings:
            skills = posting.get('skills', [])
            if not isinstance(skills, list):
                raise ValueError("Skills must be a list")
            all_skills.update(skills)
        return all_skills

    def _parse_skills(self, posting):
        """Parse skills from a single job posting."""
        skills = posting.get('skills', [])
        if isinstance(skills, list):
            return skills
        return []

    def get_unique_skills(self):
        return list(set(self.skills))