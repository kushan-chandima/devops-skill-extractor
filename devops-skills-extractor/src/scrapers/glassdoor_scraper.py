import requests
from bs4 import BeautifulSoup
from .base_scraper import BaseScraper


class GlassdoorScraper(BaseScraper):
    def __init__(self, base_url=None, headers=None):
        self.base_url = base_url or "https://www.glassdoor.com"
        self.headers = headers or self._get_default_headers()

    def _get_default_headers(self):
        return {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def fetch_data(self, job_title=None, location=None):
        """Fetch job data from Glassdoor. Returns mock data for testing."""
        search_title = job_title or "DevOps Engineer"
        # Return mock data for testing purposes - 100 realistic job postings
        return [
            # Consulting & IT Services
            {"title": "DevOps Engineer", "company": "Accenture", "location": "Chicago, IL", "skills": ["AWS", "Docker", "Kubernetes", "Jenkins", "Terraform", "Linux"]},
            {"title": "Senior DevOps Engineer", "company": "Deloitte", "location": "New York, NY", "skills": ["Azure", "Docker", "Kubernetes", "Ansible", "Python", "Git"]},
            {"title": "Cloud DevOps Engineer", "company": "Capgemini", "location": "Dallas, TX", "skills": ["AWS", "GCP", "Terraform", "Docker", "Kubernetes", "Jenkins"]},
            {"title": "DevOps Architect", "company": "Infosys", "location": "Atlanta, GA", "skills": ["AWS", "Azure", "Docker", "Kubernetes", "Ansible", "Chef"]},
            {"title": "DevOps Engineer", "company": "Cognizant", "location": "Boston, MA", "skills": ["AWS", "Docker", "Jenkins", "Puppet", "Linux", "Bash"]},
            {"title": "Platform Engineer", "company": "TCS", "location": "Edison, NJ", "skills": ["AWS", "Azure", "Kubernetes", "Docker", "Terraform", "Python"]},
            {"title": "DevOps Consultant", "company": "Wipro", "location": "Houston, TX", "skills": ["AWS", "Kubernetes", "Docker", "Ansible", "Jenkins", "Linux"]},
            {"title": "Cloud Engineer", "company": "HCL Technologies", "location": "Cary, NC", "skills": ["AWS", "Azure", "Kubernetes", "Docker", "Terraform", "Python"]},
            {"title": "DevOps Specialist", "company": "Tech Mahindra", "location": "Santa Clara, CA", "skills": ["AWS", "Kubernetes", "Docker", "Jenkins", "Ansible", "Python"]},
            {"title": "SRE", "company": "LTIMindtree", "location": "Warren, NJ", "skills": ["AWS", "Kubernetes", "Docker", "Terraform", "Prometheus", "Go"]},
            # SaaS & Software Companies
            {"title": "Site Reliability Engineer", "company": "Splunk", "location": "San Francisco, CA", "skills": ["AWS", "Kubernetes", "Docker", "Go", "Terraform", "Prometheus"]},
            {"title": "DevOps Engineer", "company": "Atlassian", "location": "Austin, TX", "skills": ["AWS", "Docker", "Kubernetes", "Bamboo", "Bitbucket", "Python"]},
            {"title": "Platform Engineer", "company": "Snowflake", "location": "San Mateo, CA", "skills": ["AWS", "Kubernetes", "Terraform", "Python", "Docker", "CI/CD"]},
            {"title": "DevOps Specialist", "company": "Workday", "location": "Pleasanton, CA", "skills": ["AWS", "Docker", "Kubernetes", "Ansible", "Java", "Jenkins"]},
            {"title": "Cloud Infrastructure Engineer", "company": "ServiceNow", "location": "Santa Clara, CA", "skills": ["AWS", "Azure", "Kubernetes", "Terraform", "Python", "Linux"]},
            {"title": "DevOps Engineer", "company": "Palo Alto Networks", "location": "Santa Clara, CA", "skills": ["AWS", "Docker", "Kubernetes", "Jenkins", "Python", "Security"]},
            {"title": "Senior DevOps Engineer", "company": "Twilio", "location": "San Francisco, CA", "skills": ["AWS", "Kubernetes", "Docker", "Terraform", "Go", "Prometheus"]},
            {"title": "DevOps Engineer II", "company": "Box", "location": "Redwood City, CA", "skills": ["AWS", "Docker", "Kubernetes", "Jenkins", "Ruby", "Terraform"]},
            {"title": "Infrastructure Engineer", "company": "Datadog", "location": "New York, NY", "skills": ["AWS", "GCP", "Kubernetes", "Docker", "Go", "Terraform"]},
            {"title": "DevOps Lead", "company": "HashiCorp", "location": "San Francisco, CA", "skills": ["Terraform", "Vault", "Consul", "Kubernetes", "AWS", "Go"]},
            {"title": "Cloud DevOps Engineer", "company": "MongoDB", "location": "New York, NY", "skills": ["AWS", "Kubernetes", "Docker", "Terraform", "Python", "MongoDB"]},
            {"title": "DevOps Engineer", "company": "Elastic", "location": "Mountain View, CA", "skills": ["AWS", "Kubernetes", "Docker", "ELK Stack", "Terraform", "Python"]},
            {"title": "Platform DevOps", "company": "GitLab", "location": "Remote", "skills": ["GCP", "Kubernetes", "Docker", "GitLab CI", "Terraform", "Ruby"]},
            {"title": "DevOps Engineer", "company": "Confluent", "location": "Mountain View, CA", "skills": ["AWS", "Kubernetes", "Docker", "Kafka", "Terraform", "Java"]},
            {"title": "Senior SRE/DevOps", "company": "New Relic", "location": "Portland, OR", "skills": ["AWS", "Kubernetes", "Docker", "Go", "Prometheus", "Grafana"]},
            # E-commerce & Marketplace
            {"title": "DevOps Engineer", "company": "Wayfair", "location": "Boston, MA", "skills": ["GCP", "Kubernetes", "Docker", "Terraform", "Python", "Jenkins"]},
            {"title": "Platform Engineer", "company": "Instacart", "location": "San Francisco, CA", "skills": ["AWS", "Kubernetes", "Docker", "Terraform", "Ruby", "Datadog"]},
            {"title": "SRE", "company": "DoorDash", "location": "San Francisco, CA", "skills": ["AWS", "Kubernetes", "Docker", "Go", "Terraform", "Prometheus"]},
            {"title": "DevOps Engineer", "company": "Lyft", "location": "San Francisco, CA", "skills": ["AWS", "Kubernetes", "Docker", "Go", "Terraform", "Envoy"]},
            {"title": "Cloud Engineer", "company": "Chewy", "location": "Plantation, FL", "skills": ["AWS", "Kubernetes", "Docker", "Terraform", "Python", "Jenkins"]},
            # Fintech
            {"title": "DevOps Engineer", "company": "Square", "location": "San Francisco, CA", "skills": ["AWS", "Kubernetes", "Docker", "Ruby", "Terraform", "Prometheus"]},
            {"title": "Platform Engineer", "company": "Robinhood", "location": "Menlo Park, CA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Kafka"]},
            {"title": "SRE", "company": "Coinbase", "location": "San Francisco, CA", "skills": ["AWS", "Kubernetes", "Docker", "Go", "Terraform", "Datadog"]},
            {"title": "DevOps Lead", "company": "Chime", "location": "San Francisco, CA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Jenkins"]},
            {"title": "Cloud DevOps", "company": "SoFi", "location": "San Francisco, CA", "skills": ["AWS", "Kubernetes", "Docker", "Terraform", "Java", "Jenkins"]},
            {"title": "DevOps Engineer", "company": "Affirm", "location": "San Francisco, CA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Ansible"]},
            {"title": "Infrastructure Engineer", "company": "Marqeta", "location": "Oakland, CA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Datadog"]},
            {"title": "SRE", "company": "Adyen", "location": "San Francisco, CA", "skills": ["AWS", "Kubernetes", "Docker", "Java", "Terraform", "Prometheus"]},
            {"title": "Platform Engineer", "company": "Toast", "location": "Boston, MA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Jenkins"]},
            {"title": "DevOps Engineer", "company": "Bill.com", "location": "San Jose, CA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Ansible"]},
            # Healthcare Tech
            {"title": "DevOps Engineer", "company": "Epic Systems", "location": "Madison, WI", "skills": ["Azure", "Kubernetes", "Docker", "Python", "Terraform", "Jenkins"]},
            {"title": "Platform Engineer", "company": "Veeva Systems", "location": "Pleasanton, CA", "skills": ["AWS", "Kubernetes", "Docker", "Java", "Terraform", "Jenkins"]},
            {"title": "SRE", "company": "Cerner", "location": "Kansas City, MO", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Ansible", "Jenkins"]},
            {"title": "Cloud DevOps", "company": "Teladoc Health", "location": "Purchase, NY", "skills": ["AWS", "Kubernetes", "Docker", "Terraform", "Python", "Datadog"]},
            {"title": "DevOps Engineer", "company": "Oscar Health", "location": "New York, NY", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Jenkins"]},
            # Automotive & Transportation
            {"title": "DevOps Engineer", "company": "Tesla", "location": "Palo Alto, CA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Jenkins"]},
            {"title": "Platform Engineer", "company": "Rivian", "location": "Irvine, CA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Ansible"]},
            {"title": "SRE", "company": "Lucid Motors", "location": "Newark, CA", "skills": ["AWS", "Kubernetes", "Docker", "Go", "Terraform", "Prometheus"]},
            {"title": "Cloud DevOps", "company": "Ford", "location": "Dearborn, MI", "skills": ["AWS", "Azure", "Kubernetes", "Docker", "Terraform", "Jenkins"]},
            {"title": "DevOps Engineer", "company": "General Motors", "location": "Detroit, MI", "skills": ["GCP", "Kubernetes", "Docker", "Python", "Terraform", "Ansible"]},
            # Media & Entertainment
            {"title": "DevOps Engineer", "company": "Hulu", "location": "Santa Monica, CA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Spinnaker"]},
            {"title": "Platform Engineer", "company": "Warner Bros Discovery", "location": "New York, NY", "skills": ["AWS", "Kubernetes", "Docker", "Go", "Terraform", "Jenkins"]},
            {"title": "SRE", "company": "NBCUniversal", "location": "New York, NY", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Datadog"]},
            {"title": "Cloud DevOps", "company": "ViacomCBS", "location": "New York, NY", "skills": ["AWS", "Kubernetes", "Docker", "Terraform", "Python", "Jenkins"]},
            {"title": "DevOps Engineer", "company": "Sony", "location": "San Mateo, CA", "skills": ["AWS", "Kubernetes", "Docker", "Java", "Terraform", "Ansible"]},
            # Hardware & Semiconductor
            {"title": "DevOps Engineer", "company": "NVIDIA", "location": "Santa Clara, CA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "GPU"]},
            {"title": "Platform Engineer", "company": "AMD", "location": "Santa Clara, CA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Ansible", "Jenkins"]},
            {"title": "SRE", "company": "Intel", "location": "Santa Clara, CA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Prometheus"]},
            {"title": "Cloud DevOps", "company": "Qualcomm", "location": "San Diego, CA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Jenkins"]},
            {"title": "DevOps Engineer", "company": "Broadcom", "location": "San Jose, CA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Ansible", "Linux"]},
            # Aerospace & Defense
            {"title": "DevOps Engineer", "company": "SpaceX", "location": "Hawthorne, CA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Linux"]},
            {"title": "Platform Engineer", "company": "Lockheed Martin", "location": "Bethesda, MD", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Ansible", "Jenkins"]},
            {"title": "SRE", "company": "Northrop Grumman", "location": "Falls Church, VA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Security"]},
            {"title": "Cloud DevOps", "company": "Raytheon", "location": "Waltham, MA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Ansible", "Jenkins"]},
            {"title": "DevOps Engineer", "company": "Boeing", "location": "Seattle, WA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Linux"]},
            # Hospitality & Travel
            {"title": "DevOps Engineer", "company": "Booking.com", "location": "New York, NY", "skills": ["AWS", "Kubernetes", "Docker", "Java", "Terraform", "Prometheus"]},
            {"title": "Platform Engineer", "company": "Expedia", "location": "Seattle, WA", "skills": ["AWS", "Kubernetes", "Docker", "Java", "Terraform", "Jenkins"]},
            {"title": "SRE", "company": "Marriott", "location": "Bethesda, MD", "skills": ["AWS", "Azure", "Kubernetes", "Docker", "Terraform", "Ansible"]},
            {"title": "Cloud DevOps", "company": "Hilton", "location": "McLean, VA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Jenkins"]},
            {"title": "DevOps Engineer", "company": "Tripadvisor", "location": "Needham, MA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Datadog"]},
            # Real Estate Tech
            {"title": "DevOps Engineer", "company": "Zillow", "location": "Seattle, WA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Jenkins"]},
            {"title": "Platform Engineer", "company": "Redfin", "location": "Seattle, WA", "skills": ["AWS", "Kubernetes", "Docker", "Java", "Terraform", "Ansible"]},
            {"title": "SRE", "company": "Opendoor", "location": "San Francisco, CA", "skills": ["AWS", "Kubernetes", "Docker", "Go", "Terraform", "Datadog"]},
            {"title": "Cloud DevOps", "company": "Compass", "location": "New York, NY", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Jenkins"]},
            {"title": "DevOps Engineer", "company": "CoStar Group", "location": "Washington, DC", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Ansible"]},
            # Education Tech
            {"title": "DevOps Engineer", "company": "Coursera", "location": "Mountain View, CA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Jenkins"]},
            {"title": "Platform Engineer", "company": "Duolingo", "location": "Pittsburgh, PA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Prometheus"]},
            {"title": "SRE", "company": "Chegg", "location": "Santa Clara, CA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Datadog"]},
            {"title": "Cloud DevOps", "company": "Udemy", "location": "San Francisco, CA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Jenkins"]},
            {"title": "DevOps Engineer", "company": "Instructure", "location": "Salt Lake City, UT", "skills": ["AWS", "Kubernetes", "Docker", "Ruby", "Terraform", "Ansible"]},
            # Food & Delivery
            {"title": "DevOps Engineer", "company": "Uber Eats", "location": "San Francisco, CA", "skills": ["AWS", "Kubernetes", "Docker", "Go", "Terraform", "Prometheus"]},
            {"title": "Platform Engineer", "company": "Grubhub", "location": "Chicago, IL", "skills": ["AWS", "Kubernetes", "Docker", "Java", "Terraform", "Jenkins"]},
            {"title": "SRE", "company": "Postmates", "location": "San Francisco, CA", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Datadog"]},
            {"title": "Cloud DevOps", "company": "Blue Apron", "location": "New York, NY", "skills": ["AWS", "Kubernetes", "Docker", "Ruby", "Terraform", "Ansible"]},
            {"title": "DevOps Engineer", "company": "HelloFresh", "location": "New York, NY", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Jenkins"]},
            # International (Europe, Asia, etc.)
            {"title": "DevOps Engineer", "company": "Delivery Hero", "location": "Berlin, Germany", "skills": ["AWS", "Kubernetes", "Docker", "Go", "Terraform", "Prometheus"]},
            {"title": "Platform Engineer", "company": "N26", "location": "Berlin, Germany", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Kafka"]},
            {"title": "SRE", "company": "Zalando", "location": "Berlin, Germany", "skills": ["AWS", "Kubernetes", "Docker", "Java", "Terraform", "Prometheus"]},
            {"title": "Cloud DevOps", "company": "Spotify", "location": "London, UK", "skills": ["GCP", "Kubernetes", "Docker", "Python", "Terraform", "Backstage"]},
            {"title": "DevOps Engineer", "company": "Monzo", "location": "London, UK", "skills": ["AWS", "Kubernetes", "Docker", "Go", "Terraform", "Prometheus"]},
            {"title": "Platform Engineer", "company": "Starling Bank", "location": "London, UK", "skills": ["AWS", "Kubernetes", "Docker", "Java", "Terraform", "Jenkins"]},
            {"title": "SRE", "company": "Checkout.com", "location": "London, UK", "skills": ["AWS", "Kubernetes", "Docker", "Go", "Terraform", "Datadog"]},
            {"title": "DevOps Engineer", "company": "Gojek", "location": "Jakarta, Indonesia", "skills": ["GCP", "Kubernetes", "Docker", "Go", "Terraform", "Kafka"]},
            {"title": "Cloud DevOps", "company": "Sea Group", "location": "Singapore", "skills": ["AWS", "Kubernetes", "Docker", "Python", "Terraform", "Jenkins"]},
            {"title": "Platform Engineer", "company": "Carousell", "location": "Singapore", "skills": ["AWS", "Kubernetes", "Docker", "Go", "Terraform", "Prometheus"]}
        ]

    def fetch_data_live(self, job_title, location):
        """Fetch live data from Glassdoor."""
        url = f"{self.base_url}/jobs?q={job_title}&l={location}"
        response = requests.get(url, headers=self.headers)
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

    def _parse_html(self, html_content):
        """Parse HTML content from Glassdoor."""
        soup = BeautifulSoup(html_content, 'html.parser')
        job_postings = []
        for job in soup.find_all('div', class_='job_seen_beacon'):
            title_elem = job.find('h2', class_='jobTitle')
            company_elem = job.find('span', class_='companyName')
            
            title = title_elem.text.strip() if title_elem else ""
            company = company_elem.text.strip() if company_elem else ""
            skills = self.extract_skills(job)
            
            job_postings.append({
                'title': title,
                'company': company,
                'skills': skills
            })
        return job_postings

    def extract_skills(self, job):
        skills_section = job.find('div', class_='job-snippet')
        if skills_section:
            return [skill.strip() for skill in skills_section.text.split(',')]
        return []