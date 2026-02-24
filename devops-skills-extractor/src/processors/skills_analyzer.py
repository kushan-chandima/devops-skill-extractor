class SkillsAnalyzer:
    def __init__(self):
        self.skills_data = []

    def analyze_skills(self, cleaned_data):
        """Analyze skills from cleaned job data and return skill counts."""
        skill_counts = {}
        for job in cleaned_data:
            skills = job.get('skills', [])
            for skill in skills:
                skill_counts[skill] = skill_counts.get(skill, 0) + 1
        self.skills_data = sorted(skill_counts.items(), key=lambda x: x[1], reverse=True)
        return skill_counts

    def get_top_skills(self, top_n=10):
        return self.skills_data[:top_n]

    def generate_insights(self):
        insights = {
            'total_skills': len(self.skills_data),
            'top_skills': self.get_top_skills()
        }
        return insights