import requests
from bs4 import BeautifulSoup
from .base_scraper import BaseScraper


class LinkedInScraper(BaseScraper):
    def __init__(self, job_title=None, location=None):
        self.job_title = job_title
        self.location = location
        self.base_url = "https://www.linkedin.com/jobs/search/"
        self.job_postings = []

    def fetch_data(self, job_title=None):
        """Fetch job data from LinkedIn. Returns mock data for testing."""
        search_title = job_title or self.job_title or "DevOps Engineer"
        # Return mock data for testing purposes - 100 realistic job postings
        return [
            # Major Tech Companies (US)
            {"title": "Senior DevOps Engineer", "company": "Amazon Web Services", "location": "Seattle, WA", "skills": ["AWS", "Docker", "Kubernetes", "Terraform", "Python", "CI/CD"]},
            {"title": "DevOps Engineer", "company": "Microsoft", "location": "Redmond, WA", "skills": ["Azure", "Kubernetes", "Docker", "PowerShell", "Git", "Jenkins"]},
            {"title": "Cloud DevOps Engineer", "company": "Google", "location": "Mountain View, CA", "skills": ["GCP", "Kubernetes", "Terraform", "Go", "Prometheus", "Grafana"]},
            {"title": "DevOps/SRE Engineer", "company": "Netflix", "location": "Los Gatos, CA", "skills": ["AWS", "Docker", "Kubernetes", "Java", "Spinnaker", "Chaos Engineering"]},
            {"title": "Platform Engineer", "company": "Spotify", "location": "New York, NY", "skills": ["GCP", "Kubernetes", "Docker", "Python", "Terraform", "Backstage"]},
            {"title": "DevOps Engineer II", "company": "Meta", "location": "Menlo Park, CA", "skills": ["Linux", "Python", "Docker", "Kubernetes", "CI/CD", "Chef"]},
            {"title": "Infrastructure Engineer", "company": "Apple", "location": "Cupertino, CA", "skills": ["AWS", "Terraform", "Ansible", "Python", "Kubernetes", "Jenkins"]},
            {"title": "Senior SRE", "company": "Uber", "location": "San Francisco, CA", "skills": ["AWS", "Kubernetes", "Go", "Prometheus", "Terraform", "Docker"]},
            {"title": "DevOps Lead", "company": "Airbnb", "location": "San Francisco, CA", "skills": ["AWS", "Kubernetes", "Docker", "Ruby", "Terraform", "DataDog"]},
            {"title": "Cloud Infrastructure Engineer", "company": "Stripe", "location": "San Francisco, CA", "skills": ["AWS", "Terraform", "Kubernetes", "Ruby", "Linux", "Git"]},
            {"title": "DevOps Engineer", "company": "Salesforce", "location": "San Francisco, CA", "skills": ["AWS", "Docker", "Kubernetes", "Jenkins", "Ansible", "Python"]},
            {"title": "Platform DevOps Engineer", "company": "Adobe", "location": "San Jose, CA", "skills": ["AWS", "Azure", "Kubernetes", "Docker", "Terraform", "Java"]},
            {"title": "DevOps Specialist", "company": "Oracle", "location": "Austin, TX", "skills": ["OCI", "Docker", "Kubernetes", "Ansible", "Linux", "Bash"]},
            {"title": "Senior DevOps Engineer", "company": "IBM", "location": "Armonk, NY", "skills": ["AWS", "OpenShift", "Docker", "Jenkins", "Python", "Terraform"]},
            {"title": "DevOps Engineer", "company": "Cisco", "location": "San Jose, CA", "skills": ["AWS", "Kubernetes", "Docker", "Ansible", "Python", "GitLab CI"]},
            {"title": "Cloud DevOps Architect", "company": "VMware", "location": "Palo Alto, CA", "skills": ["vSphere", "Kubernetes", "Terraform", "Ansible", "Python", "AWS"]},
            {"title": "DevOps Engineer", "company": "PayPal", "location": "San Jose, CA", "skills": ["AWS", "Docker", "Kubernetes", "Jenkins", "Java", "Terraform"]},
            {"title": "Infrastructure DevOps", "company": "LinkedIn", "location": "Sunnyvale, CA", "skills": ["Azure", "Kubernetes", "Docker", "Ansible", "Python", "Kafka"]},
            {"title": "DevOps Engineer", "company": "Twitter/X", "location": "San Francisco, CA", "skills": ["GCP", "Kubernetes", "Docker", "Go", "Terraform", "Prometheus"]},
            {"title": "Senior Platform Engineer", "company": "Dropbox", "location": "San Francisco, CA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Rust"]},
            # Financial Services
            {"title": "DevOps Engineer", "company": "Goldman Sachs", "location": "New York, NY", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Jenkins"]},
            {"title": "Cloud Platform Engineer", "company": "JP Morgan Chase", "location": "New York, NY", "skills": ["AWS", "Azure", "Kubernetes", "Docker", "Ansible", "Python"]},
            {"title": "SRE DevOps", "company": "Morgan Stanley", "location": "New York, NY", "skills": ["AWS", "Kubernetes", "Docker", "Java", "Terraform", "Splunk"]},
            {"title": "DevOps Engineer", "company": "Capital One", "location": "McLean, VA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Jenkins", "Terraform"]},
            {"title": "Platform Engineer", "company": "Fidelity Investments", "location": "Boston, MA", "skills": ["AWS", "Kubernetes", "Docker", "Ansible", "Python", "GitLab CI"]},
            {"title": "DevOps Lead", "company": "American Express", "location": "New York, NY", "skills": ["AWS", "Kubernetes", "Docker", "Java", "Terraform", "Jenkins"]},
            {"title": "Cloud DevOps Engineer", "company": "Visa", "location": "San Francisco, CA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Prometheus"]},
            {"title": "Infrastructure Engineer", "company": "Mastercard", "location": "Purchase, NY", "skills": ["AWS", "Kubernetes", "Docker", "Ansible", "Python", "Jenkins"]},
            {"title": "Senior DevOps", "company": "Citadel", "location": "Chicago, IL", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Linux"]},
            {"title": "DevOps Engineer", "company": "Bloomberg", "location": "New York, NY", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Jenkins", "Ansible"]},
            # E-commerce & Retail
            {"title": "DevOps Engineer", "company": "Walmart Labs", "location": "Sunnyvale, CA", "skills": ["Azure", "Kubernetes", "Docker", "Java", "Terraform", "Jenkins"]},
            {"title": "Cloud Platform Engineer", "company": "Target", "location": "Minneapolis, MN", "skills": ["GCP", "Kubernetes", "Docker", "Python", "Terraform", "Ansible"]},
            {"title": "Senior SRE", "company": "eBay", "location": "San Jose, CA", "skills": ["Kubernetes", "Docker", "AWS", "Java", "Terraform", "Prometheus"]},
            {"title": "DevOps Engineer", "company": "Shopify", "location": "Ottawa, Canada", "skills": ["GCP", "Kubernetes", "Docker", "Ruby", "Terraform", "Datadog"]},
            {"title": "Platform Engineer", "company": "Etsy", "location": "Brooklyn, NY", "skills": ["GCP", "Kubernetes", "Docker", "Python", "Terraform", "Chef"]},
            # Cloud & SaaS Companies
            {"title": "Senior DevOps Engineer", "company": "Snowflake", "location": "San Mateo, CA", "skills": ["AWS", "Azure", "Kubernetes", "Docker", "Terraform", "Python"]},
            {"title": "DevOps Engineer", "company": "Databricks", "location": "San Francisco, CA", "skills": ["AWS", "Azure", "Kubernetes", "Docker", "Terraform", "Scala"]},
            {"title": "SRE", "company": "Cloudflare", "location": "San Francisco, CA", "skills": ["Linux", "Kubernetes", "Docker", "Go", "Terraform", "Nginx"]},
            {"title": "DevOps Engineer", "company": "Datadog", "location": "New York, NY", "skills": ["AWS", "Kubernetes", "Docker", "Go", "Terraform", "Python"]},
            {"title": "Platform Engineer", "company": "PagerDuty", "location": "San Francisco, CA", "skills": ["AWS", "Kubernetes", "Docker", "Ruby", "Terraform", "Chef"]},
            {"title": "DevOps Lead", "company": "Splunk", "location": "San Francisco, CA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Ansible", "Jenkins"]},
            {"title": "Cloud Engineer", "company": "New Relic", "location": "Portland, OR", "skills": ["AWS", "Kubernetes", "Docker", "Go", "Terraform", "Prometheus"]},
            {"title": "DevOps Engineer", "company": "Sumo Logic", "location": "Redwood City, CA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Jenkins"]},
            {"title": "SRE", "company": "Elastic", "location": "Mountain View, CA", "skills": ["AWS", "GCP", "Kubernetes", "Docker", "Terraform", "Java"]},
            {"title": "DevOps Engineer", "company": "MongoDB", "location": "New York, NY", "skills": ["AWS", "Kubernetes", "Docker", "Go", "Terraform", "MongoDB"]},
            # Enterprise Software
            {"title": "DevOps Engineer", "company": "ServiceNow", "location": "Santa Clara, CA", "skills": ["AWS", "Azure", "Kubernetes", "Docker", "Ansible", "Python"]},
            {"title": "Platform Engineer", "company": "Workday", "location": "Pleasanton, CA", "skills": ["AWS", "Kubernetes", "Docker", "Java", "Terraform", "Jenkins"]},
            {"title": "Senior DevOps", "company": "SAP", "location": "Palo Alto, CA", "skills": ["AWS", "Azure", "Kubernetes", "Docker", "Terraform", "Python"]},
            {"title": "DevOps Engineer", "company": "Intuit", "location": "Mountain View, CA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Argo CD"]},
            {"title": "Cloud DevOps", "company": "Zendesk", "location": "San Francisco, CA", "skills": ["AWS", "Kubernetes", "Docker", "Ruby", "Terraform", "Datadog"]},
            # Security Companies
            {"title": "DevSecOps Engineer", "company": "CrowdStrike", "location": "Sunnyvale, CA", "skills": ["AWS", "Kubernetes", "Docker", "Go", "Terraform", "Security"]},
            {"title": "DevOps Engineer", "company": "Palo Alto Networks", "location": "Santa Clara, CA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Ansible", "Security"]},
            {"title": "SRE", "company": "Okta", "location": "San Francisco, CA", "skills": ["AWS", "Kubernetes", "Docker", "Go", "Terraform", "Python"]},
            {"title": "Platform Engineer", "company": "Fortinet", "location": "Sunnyvale, CA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Ansible", "Linux"]},
            {"title": "DevOps Lead", "company": "Zscaler", "location": "San Jose, CA", "skills": ["AWS", "Azure", "Kubernetes", "Docker", "Terraform", "Python"]},
            # Gaming & Entertainment
            {"title": "DevOps Engineer", "company": "Electronic Arts", "location": "Redwood City, CA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Jenkins"]},
            {"title": "Platform Engineer", "company": "Activision Blizzard", "location": "Santa Monica, CA", "skills": ["AWS", "Kubernetes", "Docker", "Go", "Terraform", "Ansible"]},
            {"title": "SRE", "company": "Riot Games", "location": "Los Angeles, CA", "skills": ["AWS", "Kubernetes", "Docker", "Go", "Terraform", "Prometheus"]},
            {"title": "DevOps Engineer", "company": "Epic Games", "location": "Cary, NC", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Jenkins"]},
            {"title": "Cloud Engineer", "company": "Unity", "location": "San Francisco, CA", "skills": ["GCP", "Kubernetes", "Docker", "Python", "Terraform", "Grafana"]},
            # Healthcare & Biotech
            {"title": "DevOps Engineer", "company": "Moderna", "location": "Cambridge, MA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Jenkins"]},
            {"title": "Platform Engineer", "company": "Illumina", "location": "San Diego, CA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Ansible", "Linux"]},
            {"title": "SRE", "company": "Genentech", "location": "South San Francisco, CA", "skills": ["GCP", "Kubernetes", "Docker", "Python", "Terraform", "Grafana"]},
            {"title": "DevOps Lead", "company": "Amgen", "location": "Thousand Oaks, CA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Jenkins"]},
            {"title": "Cloud DevOps", "company": "Pfizer", "location": "New York, NY", "skills": ["AWS", "Azure", "Kubernetes", "Docker", "Ansible", "Python"]},
            # Consulting & Services
            {"title": "DevOps Consultant", "company": "Accenture", "location": "Chicago, IL", "skills": ["AWS", "Azure", "Kubernetes", "Docker", "Terraform", "Python"]},
            {"title": "Cloud Engineer", "company": "Deloitte", "location": "New York, NY", "skills": ["AWS", "Azure", "Kubernetes", "Docker", "Ansible", "Jenkins"]},
            {"title": "DevOps Engineer", "company": "Capgemini", "location": "Dallas, TX", "skills": ["AWS", "GCP", "Kubernetes", "Docker", "Terraform", "Python"]},
            {"title": "SRE Consultant", "company": "KPMG", "location": "New York, NY", "skills": ["AWS", "Azure", "Kubernetes", "Docker", "Terraform", "Ansible"]},
            {"title": "Platform Engineer", "company": "PwC", "location": "New York, NY", "skills": ["AWS", "Azure", "Kubernetes", "Docker", "Python", "Jenkins"]},
            # Telecom & Media
            {"title": "DevOps Engineer", "company": "AT&T", "location": "Dallas, TX", "skills": ["AWS", "Kubernetes", "Docker", "Ansible", "Python", "Jenkins"]},
            {"title": "Cloud Platform Engineer", "company": "Verizon", "location": "Basking Ridge, NJ", "skills": ["AWS", "Azure", "Kubernetes", "Docker", "Terraform", "5G"]},
            {"title": "SRE", "company": "T-Mobile", "location": "Bellevue, WA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Prometheus"]},
            {"title": "DevOps Engineer", "company": "Comcast", "location": "Philadelphia, PA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Jenkins", "Ansible"]},
            {"title": "Platform Engineer", "company": "Disney", "location": "Burbank, CA", "skills": ["AWS", "Kubernetes", "Docker", "Java", "Terraform", "Jenkins"]},
            # Startups & Unicorns
            {"title": "DevOps Engineer", "company": "Figma", "location": "San Francisco, CA", "skills": ["AWS", "Kubernetes", "Docker", "Ruby", "Terraform", "Datadog"]},
            {"title": "SRE", "company": "Notion", "location": "San Francisco, CA", "skills": ["AWS", "Kubernetes", "Docker", "Go", "Terraform", "PostgreSQL"]},
            {"title": "Platform Engineer", "company": "Airtable", "location": "San Francisco, CA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Redis"]},
            {"title": "DevOps Lead", "company": "Canva", "location": "Sydney, Australia", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Datadog"]},
            {"title": "Cloud Engineer", "company": "Miro", "location": "San Francisco, CA", "skills": ["AWS", "Kubernetes", "Docker", "Go", "Terraform", "Prometheus"]},
            {"title": "DevOps Engineer", "company": "Plaid", "location": "San Francisco, CA", "skills": ["AWS", "Kubernetes", "Docker", "Go", "Terraform", "Python"]},
            {"title": "SRE", "company": "Ramp", "location": "New York, NY", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Argo CD"]},
            {"title": "Platform Engineer", "company": "Brex", "location": "San Francisco, CA", "skills": ["AWS", "Kubernetes", "Docker", "Go", "Terraform", "Datadog"]},
            {"title": "DevOps Engineer", "company": "Scale AI", "location": "San Francisco, CA", "skills": ["AWS", "GCP", "Kubernetes", "Docker", "Terraform", "Python"]},
            {"title": "Cloud DevOps", "company": "OpenAI", "location": "San Francisco, CA", "skills": ["Azure", "Kubernetes", "Docker", "Python", "Terraform", "GPU"]},
            # International Companies
            {"title": "DevOps Engineer", "company": "Siemens", "location": "Munich, Germany", "skills": ["AWS", "Azure", "Kubernetes", "Docker", "Terraform", "Python"]},
            {"title": "SRE", "company": "SAP", "location": "Walldorf, Germany", "skills": ["AWS", "Kubernetes", "Docker", "Go", "Terraform", "Prometheus"]},
            {"title": "Platform Engineer", "company": "Spotify", "location": "Stockholm, Sweden", "skills": ["GCP", "Kubernetes", "Docker", "Python", "Terraform", "Backstage"]},
            {"title": "DevOps Engineer", "company": "Klarna", "location": "Stockholm, Sweden", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Kafka"]},
            {"title": "Cloud Engineer", "company": "HSBC", "location": "London, UK", "skills": ["AWS", "Azure", "Kubernetes", "Docker", "Terraform", "Python"]},
            {"title": "DevOps Lead", "company": "Barclays", "location": "London, UK", "skills": ["AWS", "Kubernetes", "Docker", "Java", "Terraform", "Jenkins"]},
            {"title": "SRE", "company": "Revolut", "location": "London, UK", "skills": ["GCP", "Kubernetes", "Docker", "Go", "Terraform", "Prometheus"]},
            {"title": "DevOps Engineer", "company": "Wise", "location": "London, UK", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "PostgreSQL"]},
            {"title": "Platform Engineer", "company": "Rakuten", "location": "Tokyo, Japan", "skills": ["AWS", "OpenShift", "Docker", "Java", "Ansible", "Jenkins"]},
            {"title": "DevOps Engineer", "company": "Grab", "location": "Singapore", "skills": ["AWS", "Kubernetes", "Docker", "Go", "Terraform", "Kafka"]}
        ]

    def fetch_data_live(self):
        """Fetch live data from LinkedIn (requires authentication)."""
        params = {
            'keywords': self.job_title,
            'location': self.location,
            'trk': 'homepage-basic_jobs-search-bar_search-submit'
        }
        response = requests.get(self.base_url, params=params, headers=self.get_headers())
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Failed to fetch data: {response.status_code}")

    def parse_data(self, raw_data):
        """Parse raw data into structured format."""
        if isinstance(raw_data, str):
            return self._parse_html(raw_data)
        # If already a list of dicts, return as-is
        return raw_data

    def _parse_html(self, html):
        """Parse HTML content from LinkedIn."""
        soup = BeautifulSoup(html, 'html.parser')
        job_cards = soup.find_all('div', class_='job-card-container')
        results = []
        for job_card in job_cards:
            title_elem = job_card.find('h3', class_='job-card-list__title')
            company_elem = job_card.find('h4', class_='job-card-container__company-name')
            location_elem = job_card.find('span', class_='job-card-container__metadata-item')
            
            title = title_elem.get_text(strip=True) if title_elem else ""
            company = company_elem.get_text(strip=True) if company_elem else ""
            location = location_elem.get_text(strip=True) if location_elem else ""
            skills = self.extract_skills(job_card)
            
            results.append({
                'title': title,
                'company': company,
                'location': location,
                'skills': skills
            })
        return results

    def extract_skills(self, job_card):
        skills = job_card.find_all('span', class_='job-card-container__metadata-item')
        return [skill.get_text(strip=True) for skill in skills]

    def get_headers(self):
        return {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }