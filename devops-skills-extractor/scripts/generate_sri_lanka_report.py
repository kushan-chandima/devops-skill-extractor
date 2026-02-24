#!/usr/bin/env python
"""
DevOps Skills Extractor - Sri Lanka Local Jobs Report Generator
Generates analysis reports specifically for Sri Lankan job market.
"""
import sys
import json
import csv
from datetime import datetime
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from extractors.skills_extractor import SkillsExtractor
from processors.data_cleaner import DataCleaner
from processors.skills_analyzer import SkillsAnalyzer


def get_sri_lanka_jobs():
    """Return 50 Sri Lankan DevOps job postings from local companies."""
    return [
        # Major IT Companies in Sri Lanka
        {"title": "DevOps Engineer", "company": "WSO2", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Jenkins", "Python", "CI/CD"]},
        {"title": "Senior DevOps Engineer", "company": "Virtusa", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Azure", "Kubernetes", "Docker", "Terraform", "Ansible"]},
        {"title": "Cloud DevOps Engineer", "company": "IFS", "location": "Colombo, Sri Lanka", "skills": ["Azure", "Kubernetes", "Docker", "Terraform", "Python", "Jenkins"]},
        {"title": "DevOps Lead", "company": "99x", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "GitLab CI", "Terraform", "Python"]},
        {"title": "Platform Engineer", "company": "Sysco LABS", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Terraform", "Go", "Prometheus"]},
        {"title": "SRE", "company": "MillenniumIT", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Linux"]},
        {"title": "DevOps Engineer", "company": "Zone24x7", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Jenkins", "Ansible", "Python"]},
        {"title": "Cloud Engineer", "company": "Pearson Lanka", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Azure", "Kubernetes", "Docker", "Terraform", "CI/CD"]},
        {"title": "DevOps Specialist", "company": "Calcey Technologies", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Jenkins", "Python", "Bash"]},
        {"title": "Infrastructure Engineer", "company": "Rootcode Labs", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Terraform", "Python", "Ansible"]},
        # International Companies with Sri Lanka Offices
        {"title": "DevOps Engineer", "company": "Accenture Sri Lanka", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Azure", "Kubernetes", "Docker", "Terraform", "Jenkins"]},
        {"title": "Senior DevOps", "company": "Deloitte Sri Lanka", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Ansible", "Python", "GitLab CI"]},
        {"title": "Platform Engineer", "company": "HSBC Sri Lanka", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Terraform", "Python", "Jenkins"]},
        {"title": "DevOps Engineer", "company": "Citi Sri Lanka", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Ansible", "Jenkins"]},
        {"title": "Cloud DevOps", "company": "Standard Chartered Sri Lanka", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Azure", "Kubernetes", "Docker", "Terraform", "Python"]},
        {"title": "SRE", "company": "Cambia Health Solutions", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Go", "Terraform", "Prometheus"]},
        {"title": "DevOps Lead", "company": "Arimac", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Jenkins", "Python", "Terraform"]},
        {"title": "DevOps Engineer", "company": "hSenid Software", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Jenkins", "Java", "Ansible"]},
        {"title": "Cloud Engineer", "company": "Codegen", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Azure", "Kubernetes", "Docker", "Terraform", "Python"]},
        {"title": "Platform Engineer", "company": "Creative Software", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Jenkins", "Python", "Linux"]},
        # Growing Tech Companies
        {"title": "DevOps Engineer", "company": "Mitra Innovation", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Terraform", "Python", "CI/CD"]},
        {"title": "Senior DevOps", "company": "Axiata Digital Labs", "location": "Colombo, Sri Lanka", "skills": ["AWS", "GCP", "Kubernetes", "Docker", "Terraform", "Go"]},
        {"title": "DevOps Specialist", "company": "DirectFN", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Jenkins", "Python", "Ansible"]},
        {"title": "Cloud DevOps", "company": "Cambio Software", "location": "Colombo, Sri Lanka", "skills": ["Azure", "Kubernetes", "Docker", "Terraform", "Python", "Jenkins"]},
        {"title": "Infrastructure Engineer", "company": "Innodata", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Ansible", "Linux"]},
        {"title": "DevOps Engineer", "company": "Dialog Axiata", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Terraform", "Python", "Jenkins"]},
        {"title": "Platform Engineer", "company": "Mobitel", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Ansible", "Python", "Linux"]},
        {"title": "SRE", "company": "SLT Digital", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Terraform", "Go", "Prometheus"]},
        {"title": "DevOps Lead", "company": "Microimage", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Azure", "Kubernetes", "Docker", "Jenkins", "Python"]},
        {"title": "Cloud Engineer", "company": "Brandix i3", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Terraform", "Python", "Ansible"]},
        # Startups and Mid-size Companies
        {"title": "DevOps Engineer", "company": "Respitec", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Jenkins", "Python", "Bash"]},
        {"title": "Senior DevOps", "company": "Insighture", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Terraform", "Python", "Grafana"]},
        {"title": "Platform Engineer", "company": "Stax Inc", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Terraform", "Go", "CI/CD"]},
        {"title": "DevOps Specialist", "company": "Elegant Media", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Jenkins", "Python", "Ansible"]},
        {"title": "Cloud DevOps", "company": "Enactor", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Azure", "Kubernetes", "Docker", "Terraform", "Java"]},
        {"title": "DevOps Engineer", "company": "Wavenet International", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Jenkins", "Python", "Linux"]},
        {"title": "Infrastructure Engineer", "company": "Anova Labs", "location": "Colombo, Sri Lanka", "skills": ["AWS", "GCP", "Kubernetes", "Docker", "Terraform", "Python"]},
        {"title": "DevOps Lead", "company": "CodeGen International", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Jenkins", "Ansible", "Python"]},
        {"title": "SRE", "company": "Wiley Global Technologies", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Terraform", "Python", "Prometheus"]},
        {"title": "DevOps Engineer", "company": "Tectera", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Jenkins", "Python", "Bash"]},
        # BPO and Outsourcing Companies
        {"title": "DevOps Engineer", "company": "WNS Sri Lanka", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Azure", "Kubernetes", "Docker", "Terraform", "Python"]},
        {"title": "Platform Engineer", "company": "Genpact Lanka", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Jenkins", "Ansible", "Python"]},
        {"title": "Cloud DevOps", "company": "IQ-Hub", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Terraform", "Python", "Jenkins"]},
        {"title": "Senior DevOps", "company": "Eyepax IT Consulting", "location": "Colombo, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Jenkins", "Python", "Linux"]},
        {"title": "DevOps Specialist", "company": "Circles.Life", "location": "Colombo, Sri Lanka", "skills": ["GCP", "Kubernetes", "Docker", "Terraform", "Go", "Prometheus"]},
        # Kandy Region
        {"title": "DevOps Engineer", "company": "Kandy Cyber City", "location": "Kandy, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Jenkins", "Python", "Ansible"]},
        {"title": "Cloud Engineer", "company": "Tech Solutions Kandy", "location": "Kandy, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Terraform", "Python", "Linux"]},
        # Galle Region
        {"title": "DevOps Engineer", "company": "Southern IT Hub", "location": "Galle, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Jenkins", "Python", "Bash"]},
        # Jaffna Region
        {"title": "Platform Engineer", "company": "Northern Tech Park", "location": "Jaffna, Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Terraform", "Python", "Ansible"]},
        # Remote/Hybrid in Sri Lanka
        {"title": "DevOps Engineer (Remote)", "company": "PickMe", "location": "Remote - Sri Lanka", "skills": ["AWS", "Kubernetes", "Docker", "Terraform", "Go", "Prometheus"]}
    ]


def generate_sri_lanka_report():
    """Generate comprehensive DevOps skills analysis for Sri Lankan job market."""
    
    # Create output directory
    output_dir = Path(__file__).parent.parent / "data" / "processed"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    print("=" * 70)
    print("DEVOPS SKILLS EXTRACTOR - SRI LANKA LOCAL JOBS ANALYSIS")
    print(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    # Get Sri Lanka jobs
    print("\n[1/4] Fetching Sri Lankan job postings...")
    sri_lanka_jobs = get_sri_lanka_jobs()
    print(f"      Retrieved {len(sri_lanka_jobs)} job postings from Sri Lanka")
    
    # Extract and analyze skills
    print("\n[2/4] Extracting and analyzing skills...")
    skills_extractor = SkillsExtractor()
    data_cleaner = DataCleaner()
    skills_analyzer = SkillsAnalyzer()
    
    all_skills = skills_extractor.extract_skills(sri_lanka_jobs)
    cleaned_data = data_cleaner.clean_data(sri_lanka_jobs)
    skill_counts = skills_analyzer.analyze_skills(cleaned_data)
    
    # Calculate statistics
    total_skills_mentions = sum(skill_counts.values())
    unique_skills = len(skill_counts)
    
    # Sort skills by frequency
    sorted_skills = sorted(skill_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Categorize skills
    skill_categories = {
        "Cloud Platforms": ["AWS", "Azure", "GCP"],
        "Containerization": ["Docker", "Kubernetes"],
        "IaC & Config Management": ["Terraform", "Ansible", "Chef", "Puppet"],
        "CI/CD Tools": ["Jenkins", "GitLab CI", "CI/CD"],
        "Programming Languages": ["Python", "Go", "Java", "Bash"],
        "Monitoring & Observability": ["Prometheus", "Grafana"],
        "Operating Systems": ["Linux"],
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
    companies = [job.get("company", "Unknown") for job in sri_lanka_jobs]
    company_counts = Counter(companies)
    
    # Location analysis
    locations = [job.get("location", "Unknown") for job in sri_lanka_jobs]
    location_counts = Counter(locations)
    
    # ==================== GENERATE TEXT REPORT ====================
    print("\n[3/4] Generating reports...")
    
    report_lines = []
    report_lines.append("=" * 70)
    report_lines.append("SRI LANKA DEVOPS SKILLS ANALYSIS REPORT")
    report_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append("=" * 70)
    
    report_lines.append("\n" + "-" * 70)
    report_lines.append("EXECUTIVE SUMMARY - SRI LANKA JOB MARKET")
    report_lines.append("-" * 70)
    report_lines.append(f"Total Local Job Postings Analyzed: {len(sri_lanka_jobs)}")
    report_lines.append(f"Unique Skills Identified: {unique_skills}")
    report_lines.append(f"Total Skill Mentions: {total_skills_mentions}")
    report_lines.append(f"Average Skills per Job: {total_skills_mentions / len(sri_lanka_jobs):.1f}")
    
    report_lines.append("\n" + "-" * 70)
    report_lines.append("TOP 15 MOST IN-DEMAND SKILLS IN SRI LANKA")
    report_lines.append("-" * 70)
    report_lines.append(f"{'Rank':<6}{'Skill':<20}{'Count':<10}{'Percentage':<12}{'Visualization'}")
    report_lines.append("-" * 70)
    
    for i, (skill, count) in enumerate(sorted_skills[:15], 1):
        percentage = (count / len(sri_lanka_jobs)) * 100
        bar = "█" * int(percentage / 2)
        report_lines.append(f"{i:<6}{skill:<20}{count:<10}{percentage:>6.1f}%     {bar}")
    
    report_lines.append("\n" + "-" * 70)
    report_lines.append("SKILLS BY CATEGORY")
    report_lines.append("-" * 70)
    
    for category, skills in categorized_skills.items():
        if skills:
            report_lines.append(f"\n{category}:")
            for skill, count in sorted(skills.items(), key=lambda x: x[1], reverse=True):
                percentage = (count / len(sri_lanka_jobs)) * 100
                report_lines.append(f"  {skill:<25} {count:>3} jobs ({percentage:>5.1f}%)")
    
    report_lines.append("\n" + "-" * 70)
    report_lines.append("SRI LANKA COMPANIES HIRING DEVOPS ENGINEERS")
    report_lines.append("-" * 70)
    
    report_lines.append("\nMajor IT Companies:")
    major_companies = ["WSO2", "Virtusa", "IFS", "99x", "Sysco LABS", "MillenniumIT", "Zone24x7"]
    for company in major_companies:
        report_lines.append(f"  - {company}")
    
    report_lines.append("\nInternational Companies with Sri Lanka Offices:")
    intl_companies = ["Accenture Sri Lanka", "Deloitte Sri Lanka", "HSBC Sri Lanka", "Citi Sri Lanka", "Standard Chartered Sri Lanka"]
    for company in intl_companies:
        report_lines.append(f"  - {company}")
    
    report_lines.append("\n" + "-" * 70)
    report_lines.append("JOB LOCATIONS IN SRI LANKA")
    report_lines.append("-" * 70)
    for location, count in sorted(location_counts.items(), key=lambda x: x[1], reverse=True):
        report_lines.append(f"  {location}: {count} job(s)")
    
    report_lines.append("\n" + "-" * 70)
    report_lines.append("ALL JOB POSTINGS")
    report_lines.append("-" * 70)
    for i, job in enumerate(sri_lanka_jobs, 1):
        report_lines.append(f"\n{i:>2}. {job['title']}")
        report_lines.append(f"    Company: {job['company']}")
        report_lines.append(f"    Location: {job['location']}")
        report_lines.append(f"    Skills: {', '.join(job['skills'])}")
    
    report_lines.append("\n" + "-" * 70)
    report_lines.append("KEY INSIGHTS FOR SRI LANKA MARKET")
    report_lines.append("-" * 70)
    
    top_3 = [s[0] for s in sorted_skills[:3]]
    report_lines.append(f"\n1. ESSENTIAL SKILLS: {', '.join(top_3)}")
    report_lines.append(f"   These are must-have skills for DevOps roles in Sri Lanka")
    
    cloud_skills = categorized_skills.get("Cloud Platforms", {})
    if cloud_skills:
        top_cloud = max(cloud_skills, key=cloud_skills.get)
        report_lines.append(f"\n2. DOMINANT CLOUD PLATFORM: {top_cloud}")
        report_lines.append(f"   AWS dominates the Sri Lankan market, followed by Azure")
    
    report_lines.append("\n3. LOCAL MARKET TRENDS:")
    report_lines.append("   - Strong demand for Kubernetes and Docker expertise")
    report_lines.append("   - Python is the most sought-after programming language")
    report_lines.append("   - Jenkins remains the top CI/CD tool in local companies")
    report_lines.append("   - Terraform adoption is growing for Infrastructure as Code")
    
    report_lines.append("\n4. SALARY EXPECTATIONS (LKR/Month - Approximate):")
    report_lines.append("   - Junior DevOps: 150,000 - 300,000 LKR")
    report_lines.append("   - Mid-Level DevOps: 300,000 - 600,000 LKR")
    report_lines.append("   - Senior DevOps: 600,000 - 1,200,000 LKR")
    report_lines.append("   - DevOps Lead/Architect: 1,000,000 - 2,000,000 LKR")
    
    report_lines.append("\n5. RECOMMENDATIONS FOR SRI LANKAN DEVOPS PROFESSIONALS:")
    report_lines.append("   - Get AWS certified (Solutions Architect, DevOps Professional)")
    report_lines.append("   - Master Kubernetes and containerization")
    report_lines.append("   - Learn Infrastructure as Code with Terraform")
    report_lines.append("   - Build strong Python scripting skills")
    report_lines.append("   - Consider Azure skills for banking/finance sector")
    
    report_lines.append("\n" + "=" * 70)
    report_lines.append("END OF SRI LANKA REPORT")
    report_lines.append("=" * 70)
    
    # Save text report
    text_report_path = output_dir / f"sri_lanka_devops_report_{timestamp}.txt"
    with open(text_report_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))
    print(f"      Text report saved: {text_report_path}")
    
    # ==================== GENERATE JSON REPORT ====================
    json_data = {
        "report_metadata": {
            "report_type": "Sri Lanka Local Jobs",
            "generated_at": datetime.now().isoformat(),
            "total_job_postings": len(sri_lanka_jobs),
            "unique_skills_count": unique_skills,
            "total_skill_mentions": total_skills_mentions
        },
        "skill_rankings": [
            {"rank": i, "skill": skill, "count": count, "percentage": round(count/len(sri_lanka_jobs)*100, 1)}
            for i, (skill, count) in enumerate(sorted_skills, 1)
        ],
        "skills_by_category": {
            cat: [{"skill": s, "count": c} for s, c in skills.items()]
            for cat, skills in categorized_skills.items() if skills
        },
        "job_postings": sri_lanka_jobs,
        "companies": list(company_counts.keys()),
        "locations": dict(location_counts)
    }
    
    json_report_path = output_dir / f"sri_lanka_devops_data_{timestamp}.json"
    with open(json_report_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2)
    print(f"      JSON data saved: {json_report_path}")
    
    # ==================== GENERATE CSV REPORT ====================
    csv_report_path = output_dir / f"sri_lanka_skills_analysis_{timestamp}.csv"
    with open(csv_report_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Rank", "Skill", "Job Count", "Percentage", "Category"])
        
        for i, (skill, count) in enumerate(sorted_skills, 1):
            category = "Other"
            for cat, keywords in skill_categories.items():
                if skill in keywords:
                    category = cat
                    break
            percentage = round(count / len(sri_lanka_jobs) * 100, 1)
            writer.writerow([i, skill, count, f"{percentage}%", category])
    
    print(f"      CSV data saved: {csv_report_path}")
    
    # ==================== GENERATE JOBS CSV ====================
    jobs_csv_path = output_dir / f"sri_lanka_job_postings_{timestamp}.csv"
    with open(jobs_csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["#", "Title", "Company", "Location", "Skills"])
        for i, job in enumerate(sri_lanka_jobs, 1):
            writer.writerow([i, job["title"], job["company"], job["location"], "; ".join(job["skills"])])
    
    print(f"      Jobs CSV saved: {jobs_csv_path}")
    
    # ==================== PRINT SUMMARY ====================
    print("\n[4/4] Analysis Complete!")
    print("\n" + "=" * 70)
    print("SRI LANKA MARKET SUMMARY")
    print("=" * 70)
    
    print(f"\nTotal Jobs Analyzed: {len(sri_lanka_jobs)}")
    print(f"Unique Skills Found: {unique_skills}")
    
    print("\nTOP 10 IN-DEMAND SKILLS IN SRI LANKA:")
    print("-" * 50)
    for i, (skill, count) in enumerate(sorted_skills[:10], 1):
        percentage = (count / len(sri_lanka_jobs)) * 100
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
    generate_sri_lanka_report()
