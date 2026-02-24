import sys
from scrapers.linkedin_scraper import LinkedInScraper
from scrapers.glassdoor_scraper import GlassdoorScraper
from extractors.skills_extractor import SkillsExtractor
from processors.data_cleaner import DataCleaner
from processors.skills_analyzer import SkillsAnalyzer

def main():
    # Initialize scrapers
    linkedin_scraper = LinkedInScraper()
    glassdoor_scraper = GlassdoorScraper()

    # Fetch data from job postings
    linkedin_data = linkedin_scraper.fetch_data()
    glassdoor_data = glassdoor_scraper.fetch_data()

    # Combine data
    combined_data = linkedin_data + glassdoor_data

    # Initialize extractor and processor
    skills_extractor = SkillsExtractor()
    data_cleaner = DataCleaner()
    skills_analyzer = SkillsAnalyzer()

    # Extract skills
    extracted_skills = skills_extractor.extract(combined_data)

    # Clean data
    cleaned_data = data_cleaner.clean(combined_data)

    # Analyze skills
    analysis_results = skills_analyzer.analyze(cleaned_data)

    # Output results
    print("Extracted Skills:", extracted_skills)
    print("Analysis Results:", analysis_results)

if __name__ == "__main__":
    main()