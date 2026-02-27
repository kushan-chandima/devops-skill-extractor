import sys
import json
import csv
from datetime import datetime
from collections import Counter
from pathlib import Path

from scrapers.linkedin_scraper import LinkedInScraper
from scrapers.glassdoor_scraper import GlassdoorScraper
from extractors.skills_extractor import SkillsExtractor
from processors.data_cleaner import DataCleaner
from processors.skills_analyzer import SkillsAnalyzer


def generate_reports(linkedin_data, glassdoor_data, combined_data, skill_counts, timestamp):
    """Generate timestamped reports with current data."""
    
    # Create output directory
    output_dir = Path(__file__).parent.parent / "data" / "processed"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Calculate statistics
    total_skills_mentions = sum(skill_counts.values())
    unique_skills = len(skill_counts)
    sorted_skills = sorted(skill_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Categorize skills
    skill_categories = {
        "Cloud Platforms": ["AWS", "Azure", "GCP", "OCI", "vSphere"],
        "Containerization": ["Docker", "Kubernetes", "OpenShift"],
        "IaC & Config Management": ["Terraform", "Ansible", "Chef", "Puppet", "Vault", "Consul"],
        "CI/CD Tools": ["Jenkins", "GitLab CI", "Bamboo", "Spinnaker", "Bitbucket", "CI/CD"],
        "Programming Languages": ["Python", "Go", "Java", "Ruby", "Rust", "PowerShell", "Bash"],
        "Monitoring & Observability": ["Prometheus", "Grafana", "DataDog", "ELK Stack", "Splunk", "New Relic"],
        "Version Control": ["Git", "GitHub", "Bitbucket"],
        "Operating Systems": ["Linux"],
        "Messaging & Data": ["Kafka", "MongoDB"],
        "Security": ["Security"],
        "Other": []
    }
    
    categorized_skills = {cat: {} for cat in skill_categories}
    for skill, count in sorted_skills:
        assigned = False
        for category, keywords in skill_categories.items():
            if skill in keywords:
                categorized_skills[category][skill] = count
                assigned = True
                break
        if not assigned:
            categorized_skills["Other"][skill] = count
    
    # Company and location analysis
    company_counts = Counter([job.get("company", "Unknown") for job in combined_data])
    location_counts = Counter([job.get("location", "Unknown") for job in combined_data])
    
    # Generate text report
    report_lines = []
    report_lines.append("=" * 70)
    report_lines.append("DEVOPS SKILLS ANALYSIS REPORT")
    report_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append("=" * 70)
    report_lines.append(f"\nTotal Job Postings Analyzed: {len(combined_data)}")
    report_lines.append(f"  - LinkedIn: {len(linkedin_data)} postings")
    report_lines.append(f"  - Glassdoor: {len(glassdoor_data)} postings")
    report_lines.append(f"Unique Skills Identified: {unique_skills}")
    report_lines.append(f"Total Skill Mentions: {total_skills_mentions}")
    report_lines.append(f"\nTOP 15 MOST IN-DEMAND SKILLS:")
    report_lines.append("-" * 70)
    for i, (skill, count) in enumerate(sorted_skills[:15], 1):
        percentage = (count / len(combined_data)) * 100
        report_lines.append(f"{i:<6}{skill:<20}{count:<10}{percentage:>6.1f}%")
    report_lines.append("\n" + "=" * 70)
    
    # Save text report
    text_report_path = output_dir / f"devops_skills_report_{timestamp}.txt"
    with open(text_report_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))
    
    # Save JSON report
    json_data = {
        "report_metadata": {
            "generated_at": datetime.now().isoformat(),
            "total_job_postings": len(combined_data),
            "linkedin_postings": len(linkedin_data),
            "glassdoor_postings": len(glassdoor_data),
            "unique_skills_count": unique_skills,
            "total_skill_mentions": total_skills_mentions
        },
        "skill_rankings": [
            {"rank": i, "skill": skill, "count": count, "percentage": round(count/len(combined_data)*100, 1)}
            for i, (skill, count) in enumerate(sorted_skills, 1)
        ],
        "skills_by_category": {
            cat: [{"skill": s, "count": c} for s, c in skills.items()]
            for cat, skills in categorized_skills.items() if skills
        },
        "job_postings": {"linkedin": linkedin_data, "glassdoor": glassdoor_data},
        "companies": list(company_counts.keys()),
        "locations": dict(location_counts)
    }
    json_report_path = output_dir / f"devops_skills_data_{timestamp}.json"
    with open(json_report_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2)
    
    # Save CSV report
    csv_report_path = output_dir / f"devops_skills_analysis_{timestamp}.csv"
    with open(csv_report_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Rank", "Skill", "Job Count", "Percentage", "Category"])
        for i, (skill, count) in enumerate(sorted_skills, 1):
            category = "Other"
            for cat, keywords in skill_categories.items():
                if skill in keywords:
                    category = cat
                    break
            percentage = round(count / len(combined_data) * 100, 1)
            writer.writerow([i, skill, count, f"{percentage}%", category])
    
    # Save jobs CSV
    jobs_csv_path = output_dir / f"job_postings_{timestamp}.csv"
    with open(jobs_csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Source", "Title", "Company", "Location", "Skills"])
        for job in linkedin_data:
            writer.writerow(["LinkedIn", job["title"], job["company"], job.get("location", "N/A"), "; ".join(job["skills"])])
        for job in glassdoor_data:
            writer.writerow(["Glassdoor", job["title"], job["company"], job.get("location", "N/A"), "; ".join(job["skills"])])
    
    return {
        "text_report": str(text_report_path),
        "json_data": str(json_report_path),
        "skills_csv": str(csv_report_path),
        "jobs_csv": str(jobs_csv_path)
    }


def main():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    print("=" * 70)
    print("DEVOPS SKILLS EXTRACTOR")
    print(f"Run Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    # Initialize scrapers
    linkedin_scraper = LinkedInScraper()
    glassdoor_scraper = GlassdoorScraper()

    # Fetch data from job postings
    print("\nFetching job postings...")
    linkedin_data = linkedin_scraper.fetch_data()
    glassdoor_data = glassdoor_scraper.fetch_data()

    # Combine data
    combined_data = linkedin_data + glassdoor_data
    print(f"Total job postings: {len(combined_data)}")

    # Initialize extractor and processor
    skills_extractor = SkillsExtractor()
    data_cleaner = DataCleaner()
    skills_analyzer = SkillsAnalyzer()

    # Extract skills
    extracted_skills = skills_extractor.extract_skills(combined_data)

    # Clean data
    cleaned_data = data_cleaner.clean_data(combined_data)

    # Analyze skills
    analysis_results = skills_analyzer.analyze_skills(cleaned_data)

    # Output results
    print("\nExtracted Skills:", extracted_skills)
    print("Analysis Results:", analysis_results)
    
    # Generate reports with timestamp
    print("\nGenerating reports...")
    reports = generate_reports(linkedin_data, glassdoor_data, combined_data, analysis_results, timestamp)
    
    print("\n" + "=" * 70)
    print("REPORTS GENERATED:")
    print("=" * 70)
    print(f"  1. Text Report:  {reports['text_report']}")
    print(f"  2. JSON Data:    {reports['json_data']}")
    print(f"  3. Skills CSV:   {reports['skills_csv']}")
    print(f"  4. Jobs CSV:     {reports['jobs_csv']}")
    print("=" * 70)


if __name__ == "__main__":
    main()