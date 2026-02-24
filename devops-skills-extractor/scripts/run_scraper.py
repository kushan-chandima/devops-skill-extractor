import sys
from src.scrapers.linkedin_scraper import LinkedInScraper
from src.scrapers.glassdoor_scraper import GlassdoorScraper
from src.extractors.skills_extractor import SkillsExtractor
from src.processors.data_cleaner import DataCleaner
from src.processors.skills_analyzer import SkillsAnalyzer
from src.storage.database import Database

def main():
    # Initialize scrapers
    linkedin_scraper = LinkedInScraper()
    glassdoor_scraper = GlassdoorScraper()

    # Scrape job postings
    linkedin_data = linkedin_scraper.fetch_data()
    glassdoor_data = glassdoor_scraper.fetch_data()

    # Combine data
    combined_data = linkedin_data + glassdoor_data

    # Initialize extractor and processor
    skills_extractor = SkillsExtractor()
    data_cleaner = DataCleaner()
    skills_analyzer = SkillsAnalyzer()

    # Extract skills
    raw_skills = skills_extractor.extract_skills(combined_data)

    # Clean data
    cleaned_data = data_cleaner.clean_data(raw_skills)

    # Analyze skills
    analysis_results = skills_analyzer.analyze(cleaned_data)

    # Store results in the database
    db = Database()
    db.store_skills(analysis_results)

if __name__ == "__main__":
    main()