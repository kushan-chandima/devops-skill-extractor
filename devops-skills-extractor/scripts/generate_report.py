#!/usr/bin/env python
"""
DevOps Skills Extractor - Report Generator
Generates comprehensive analysis reports from job postings data.
"""
import sys
import json
import csv
from datetime import datetime
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from scrapers.linkedin_scraper import LinkedInScraper
from scrapers.glassdoor_scraper import GlassdoorScraper
from extractors.skills_extractor import SkillsExtractor
from processors.data_cleaner import DataCleaner
from processors.skills_analyzer import SkillsAnalyzer


def generate_reports():
    """Generate comprehensive DevOps skills analysis reports."""
    
    # Create output directory
    output_dir = Path(__file__).parent.parent / "data" / "processed"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    print("=" * 70)
    print("DEVOPS SKILLS EXTRACTOR - COMPREHENSIVE ANALYSIS")
    print(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    # Initialize scrapers
    linkedin_scraper = LinkedInScraper()
    glassdoor_scraper = GlassdoorScraper()
    
    # Fetch data
    print("\n[1/5] Fetching job postings from LinkedIn...")
    linkedin_data = linkedin_scraper.fetch_data()
    print(f"      Retrieved {len(linkedin_data)} job postings from LinkedIn")
    
    print("\n[2/5] Fetching job postings from Glassdoor...")
    glassdoor_data = glassdoor_scraper.fetch_data()
    print(f"      Retrieved {len(glassdoor_data)} job postings from Glassdoor")
    
    # Combine data
    combined_data = linkedin_data + glassdoor_data
    print(f"\n      Total job postings: {len(combined_data)}")
    
    # Extract and analyze skills
    print("\n[3/5] Extracting and analyzing skills...")
    skills_extractor = SkillsExtractor()
    data_cleaner = DataCleaner()
    skills_analyzer = SkillsAnalyzer()
    
    all_skills = skills_extractor.extract_skills(combined_data)
    cleaned_data = data_cleaner.clean_data(combined_data)
    skill_counts = skills_analyzer.analyze_skills(cleaned_data)
    
    # Calculate statistics
    total_skills_mentions = sum(skill_counts.values())
    unique_skills = len(skill_counts)
    
    # Sort skills by frequency
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
    
    # Assign skills to categories
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
    
    # Company analysis
    companies = [job.get("company", "Unknown") for job in combined_data]
    company_counts = Counter(companies)
    
    # Location analysis
    locations = [job.get("location", "Unknown") for job in combined_data]
    location_counts = Counter(locations)
    
    # ==================== GENERATE TEXT REPORT ====================
    print("\n[4/5] Generating reports...")
    
    report_lines = []
    report_lines.append("=" * 70)
    report_lines.append("DEVOPS SKILLS ANALYSIS REPORT")
    report_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append("=" * 70)
    
    report_lines.append("\n" + "-" * 70)
    report_lines.append("EXECUTIVE SUMMARY")
    report_lines.append("-" * 70)
    report_lines.append(f"Total Job Postings Analyzed: {len(combined_data)}")
    report_lines.append(f"  - LinkedIn: {len(linkedin_data)} postings")
    report_lines.append(f"  - Glassdoor: {len(glassdoor_data)} postings")
    report_lines.append(f"Unique Skills Identified: {unique_skills}")
    report_lines.append(f"Total Skill Mentions: {total_skills_mentions}")
    report_lines.append(f"Average Skills per Job: {total_skills_mentions / len(combined_data):.1f}")
    
    report_lines.append("\n" + "-" * 70)
    report_lines.append("TOP 15 MOST IN-DEMAND SKILLS")
    report_lines.append("-" * 70)
    report_lines.append(f"{'Rank':<6}{'Skill':<20}{'Count':<10}{'Percentage':<12}{'Visualization'}")
    report_lines.append("-" * 70)
    
    for i, (skill, count) in enumerate(sorted_skills[:15], 1):
        percentage = (count / len(combined_data)) * 100
        bar = "█" * int(percentage / 2)
        report_lines.append(f"{i:<6}{skill:<20}{count:<10}{percentage:>6.1f}%     {bar}")
    
    report_lines.append("\n" + "-" * 70)
    report_lines.append("SKILLS BY CATEGORY")
    report_lines.append("-" * 70)
    
    for category, skills in categorized_skills.items():
        if skills:
            report_lines.append(f"\n{category}:")
            for skill, count in sorted(skills.items(), key=lambda x: x[1], reverse=True):
                percentage = (count / len(combined_data)) * 100
                report_lines.append(f"  {skill:<25} {count:>3} jobs ({percentage:>5.1f}%)")
    
    report_lines.append("\n" + "-" * 70)
    report_lines.append("JOB POSTINGS BY SOURCE")
    report_lines.append("-" * 70)
    
    report_lines.append("\nLINKEDIN JOB POSTINGS:")
    report_lines.append("-" * 50)
    for i, job in enumerate(linkedin_data, 1):
        report_lines.append(f"{i:>2}. {job['title']}")
        report_lines.append(f"    Company: {job['company']}")
        report_lines.append(f"    Location: {job.get('location', 'N/A')}")
        report_lines.append(f"    Skills: {', '.join(job['skills'])}")
        report_lines.append("")
    
    report_lines.append("\nGLASSDOOR JOB POSTINGS:")
    report_lines.append("-" * 50)
    for i, job in enumerate(glassdoor_data, 1):
        report_lines.append(f"{i:>2}. {job['title']}")
        report_lines.append(f"    Company: {job['company']}")
        report_lines.append(f"    Location: {job.get('location', 'N/A')}")
        report_lines.append(f"    Skills: {', '.join(job['skills'])}")
        report_lines.append("")
    
    report_lines.append("\n" + "-" * 70)
    report_lines.append("COMPANIES HIRING")
    report_lines.append("-" * 70)
    for company, count in sorted(company_counts.items()):
        report_lines.append(f"  {company}")
    
    report_lines.append("\n" + "-" * 70)
    report_lines.append("JOB LOCATIONS")
    report_lines.append("-" * 70)
    for location, count in sorted(location_counts.items(), key=lambda x: x[1], reverse=True):
        report_lines.append(f"  {location}: {count} job(s)")
    
    report_lines.append("\n" + "-" * 70)
    report_lines.append("KEY INSIGHTS & RECOMMENDATIONS")
    report_lines.append("-" * 70)
    
    top_3 = [s[0] for s in sorted_skills[:3]]
    report_lines.append(f"\n1. MUST-HAVE SKILLS: {', '.join(top_3)}")
    report_lines.append(f"   These appear in {sorted_skills[0][1]}-{sorted_skills[2][1]} out of {len(combined_data)} job postings")
    
    cloud_skills = categorized_skills.get("Cloud Platforms", {})
    if cloud_skills:
        top_cloud = max(cloud_skills, key=cloud_skills.get)
        report_lines.append(f"\n2. DOMINANT CLOUD PLATFORM: {top_cloud}")
        report_lines.append(f"   {top_cloud} is required in {cloud_skills[top_cloud]} jobs ({cloud_skills[top_cloud]/len(combined_data)*100:.1f}%)")
    
    report_lines.append("\n3. CONTAINERIZATION IS ESSENTIAL:")
    container_skills = categorized_skills.get("Containerization", {})
    if container_skills:
        for skill, count in container_skills.items():
            report_lines.append(f"   - {skill}: {count} jobs ({count/len(combined_data)*100:.1f}%)")
    
    report_lines.append("\n4. INFRASTRUCTURE AS CODE:")
    report_lines.append("   Terraform and Ansible dominate the IaC space")
    
    report_lines.append("\n5. PROGRAMMING SKILLS:")
    prog_skills = categorized_skills.get("Programming Languages", {})
    if prog_skills:
        top_langs = sorted(prog_skills.items(), key=lambda x: x[1], reverse=True)[:3]
        report_lines.append(f"   Top languages: {', '.join([l[0] for l in top_langs])}")
    
    report_lines.append("\n" + "=" * 70)
    report_lines.append("END OF REPORT")
    report_lines.append("=" * 70)
    
    # Save text report
    text_report_path = output_dir / f"devops_skills_report_{timestamp}.txt"
    with open(text_report_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))
    print(f"      Text report saved: {text_report_path}")
    
    # ==================== GENERATE JSON REPORT ====================
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
        "job_postings": {
            "linkedin": linkedin_data,
            "glassdoor": glassdoor_data
        },
        "companies": list(company_counts.keys()),
        "locations": dict(location_counts)
    }
    
    json_report_path = output_dir / f"devops_skills_data_{timestamp}.json"
    with open(json_report_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2)
    print(f"      JSON data saved: {json_report_path}")
    
    # ==================== GENERATE CSV REPORT ====================
    csv_report_path = output_dir / f"devops_skills_analysis_{timestamp}.csv"
    with open(csv_report_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Rank", "Skill", "Job Count", "Percentage", "Category"])
        
        for i, (skill, count) in enumerate(sorted_skills, 1):
            # Find category
            category = "Other"
            for cat, keywords in skill_categories.items():
                if skill in keywords:
                    category = cat
                    break
            percentage = round(count / len(combined_data) * 100, 1)
            writer.writerow([i, skill, count, f"{percentage}%", category])
    
    print(f"      CSV data saved: {csv_report_path}")
    
    # ==================== GENERATE JOBS CSV ====================
    jobs_csv_path = output_dir / f"job_postings_{timestamp}.csv"
    with open(jobs_csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Source", "Title", "Company", "Location", "Skills"])
        for job in linkedin_data:
            writer.writerow(["LinkedIn", job["title"], job["company"], job.get("location", "N/A"), "; ".join(job["skills"])])
        for job in glassdoor_data:
            writer.writerow(["Glassdoor", job["title"], job["company"], job.get("location", "N/A"), "; ".join(job["skills"])])
    
    print(f"      Jobs CSV saved: {jobs_csv_path}")
    
    # ==================== PRINT SUMMARY TO CONSOLE ====================
    print("\n[5/5] Analysis Complete!")
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    print(f"\nTotal Jobs Analyzed: {len(combined_data)}")
    print(f"  - LinkedIn: {len(linkedin_data)}")
    print(f"  - Glassdoor: {len(glassdoor_data)}")
    
    print(f"\nUnique Skills Found: {unique_skills}")
    
    print("\nTOP 10 MOST IN-DEMAND DEVOPS SKILLS:")
    print("-" * 50)
    for i, (skill, count) in enumerate(sorted_skills[:10], 1):
        percentage = (count / len(combined_data)) * 100
        bar = "█" * int(percentage / 2)
        print(f"  {i:>2}. {skill:<18} {count:>2} jobs ({percentage:>5.1f}%) {bar}")
    
    print("\n" + "=" * 70)
    print("REPORTS GENERATED:")
    print("=" * 70)
    print(f"  1. Text Report:  {text_report_path}")
    print(f"  2. JSON Data:    {json_report_path}")
    print(f"  3. Skills CSV:   {csv_report_path}")
    print(f"  4. Jobs CSV:     {jobs_csv_path}")
    print("=" * 70)
    
    return {
        "text_report": str(text_report_path),
        "json_data": str(json_report_path),
        "skills_csv": str(csv_report_path),
        "jobs_csv": str(jobs_csv_path)
    }


if __name__ == "__main__":
    generate_reports()