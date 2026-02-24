#!/usr/bin/env python
"""Demo script to show application output."""
import sys
sys.path.insert(0, 'src')

from scrapers.linkedin_scraper import LinkedInScraper
from scrapers.glassdoor_scraper import GlassdoorScraper
from extractors.skills_extractor import SkillsExtractor
from processors.data_cleaner import DataCleaner
from processors.skills_analyzer import SkillsAnalyzer

def main():
    # Initialize scrapers
    linkedin_scraper = LinkedInScraper()
    glassdoor_scraper = GlassdoorScraper()

    # Fetch job data
    print('=' * 60)
    print('FETCHING JOB POSTINGS')
    print('=' * 60)

    linkedin_data = linkedin_scraper.fetch_data()
    glassdoor_data = glassdoor_scraper.fetch_data()

    print('\nLinkedIn Job Postings:')
    for job in linkedin_data:
        print(f'  - {job["title"]} at {job["company"]}')
        print(f'    Skills: {job["skills"]}')

    print('\nGlassdoor Job Postings:')
    for job in glassdoor_data:
        print(f'  - {job["title"]} at {job["company"]}')
        print(f'    Skills: {job["skills"]}')

    # Combine data
    combined_data = linkedin_data + glassdoor_data
    print(f'\nTotal Job Postings: {len(combined_data)}')

    # Extract unique skills
    print('\n' + '=' * 60)
    print('EXTRACTING SKILLS')
    print('=' * 60)

    skills_extractor = SkillsExtractor()
    all_skills = skills_extractor.extract_skills(combined_data)
    print(f'\nUnique Skills Extracted: {sorted(all_skills)}')

    # Clean data
    data_cleaner = DataCleaner()
    cleaned_data = data_cleaner.clean_data(combined_data)

    # Analyze skills
    print('\n' + '=' * 60)
    print('SKILLS ANALYSIS')
    print('=' * 60)

    skills_analyzer = SkillsAnalyzer()
    skill_counts = skills_analyzer.analyze_skills(cleaned_data)

    print('\nSkill Frequency:')
    for skill, count in sorted(skill_counts.items(), key=lambda x: x[1], reverse=True):
        print(f'  {skill}: {count} job(s)')

    insights = skills_analyzer.generate_insights()
    print(f'\nTotal Unique Skills: {insights["total_skills"]}')
    print(f'Top Skills: {[s[0] for s in insights["top_skills"]]}')

    # Summary
    print('\n' + '=' * 60)
    print('DEVOPS SKILLS SUMMARY')
    print('=' * 60)
    print('\nMost In-Demand DevOps Skills:')
    for i, (skill, count) in enumerate(insights["top_skills"], 1):
        bar = '█' * (count * 5)
        print(f'  {i}. {skill:15} {bar} ({count})')

if __name__ == "__main__":
    main()
