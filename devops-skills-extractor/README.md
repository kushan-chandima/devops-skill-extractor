# DevOps Skills Extractor

A Python-based application that scrapes job postings from LinkedIn and Glassdoor to extract and analyze the most in-demand skills for DevOps engineers.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Tests](https://img.shields.io/badge/Tests-9%20passed-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Running Tests](#running-tests)
- [Generating Reports](#generating-reports)
- [Sample Output](#sample-output)
- [API Reference](#api-reference)
- [Skills Taxonomy](#skills-taxonomy)
- [Contributing](#contributing)
- [License](#license)

## Overview

The DevOps Skills Extractor analyzes job postings from major job platforms to identify trending skills in the DevOps field. It provides:

- **Data Collection**: Scrapes job postings from LinkedIn and Glassdoor
- **Skills Extraction**: Identifies and categorizes technical skills from job descriptions
- **Analysis & Insights**: Generates comprehensive reports with skill rankings and trends
- **Multiple Output Formats**: Exports data as TXT, JSON, and CSV files

## Features

- 🔍 **Multi-Platform Scraping**: Collect job data from LinkedIn and Glassdoor
- 📊 **Skills Analysis**: Automatic skill extraction and frequency analysis
- 📈 **Categorization**: Skills grouped by category (Cloud, Containerization, CI/CD, etc.)
- 📄 **Report Generation**: Comprehensive reports in multiple formats
- 🧪 **Test Coverage**: Full test suite with pytest
- 🐳 **Docker Support**: Containerized deployment ready

## Project Structure

```
devops-skills-extractor/
├── src/
│   ├── main.py                 # Application entry point
│   ├── api/
│   │   └── routes.py           # REST API endpoints
│   ├── config/
│   │   └── settings.py         # Configuration settings
│   ├── scrapers/
│   │   ├── base_scraper.py     # Base scraper class
│   │   ├── linkedin_scraper.py # LinkedIn job scraper
│   │   └── glassdoor_scraper.py# Glassdoor job scraper
│   ├── extractors/
│   │   └── skills_extractor.py # Skills extraction logic
│   ├── processors/
│   │   ├── data_cleaner.py     # Data cleaning utilities
│   │   └── skills_analyzer.py  # Skills analysis engine
│   ├── storage/
│   │   ├── database.py         # Database connections
│   │   └── models.py           # Data models
│   └── utils/
│       ├── logger.py           # Logging utilities
│       └── helpers.py          # Helper functions
├── data/
│   ├── raw/                    # Raw scraped data
│   ├── processed/              # Generated reports
│   └── skills_taxonomy.json    # Skills classification
├── notebooks/
│   └── analysis.ipynb          # Jupyter analysis notebook
├── tests/
│   ├── test_scrapers.py        # Scraper tests
│   ├── test_extractors.py      # Extractor tests
│   └── test_processors.py      # Processor tests
├── scripts/
│   ├── run_scraper.py          # Scraper execution script
│   └── generate_report.py      # Report generation script
├── requirements.txt            # Python dependencies
├── pyproject.toml              # Project configuration
├── Dockerfile                  # Docker configuration
├── docker-compose.yml          # Docker Compose setup
└── README.md                   # This file
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/devops-skills-extractor.git
cd devops-skills-extractor
```

### Step 2: Create Virtual Environment

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**Linux/macOS:**
```bash
python -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment (Optional)

```bash
cp .env.example .env
# Edit .env with your configuration
```

## Quick Start

### Run the Main Application

```bash
cd src
python main.py
```

### Run the Demo Script

```bash
python run_demo.py
```

**Expected Output:**
```
============================================================
FETCHING JOB POSTINGS
============================================================

LinkedIn Job Postings:
  - Senior DevOps Engineer at Amazon Web Services
    Skills: ['AWS', 'Docker', 'Kubernetes', 'Terraform', 'Python', 'CI/CD']
  ...

============================================================
EXTRACTING SKILLS
============================================================

Unique Skills Extracted: ['AWS', 'Ansible', 'Azure', 'CI/CD', 'Docker', ...]

============================================================
DEVOPS SKILLS SUMMARY
============================================================

Most In-Demand DevOps Skills:
  1. Kubernetes      ██████████████████████████████████████████████ (38)
  2. Docker          ██████████████████████████████████████████ (34)
  3. AWS             ██████████████████████████████████████ (31)
  ...
```

## Running Tests

### Run All Tests

```bash
python -m pytest tests/ -v
```

### Run Tests with Coverage Report

```bash
python -m pytest tests/ -v --tb=short
```

### Generate JUnit XML Report (for CI/CD)

```bash
python -m pytest tests/ -v --junitxml=test_report.xml
```

**Sample Test Output:**
```
============================= test session starts =============================
collected 9 items

tests/test_extractors.py::TestSkillsExtractor::test_empty_data PASSED    [ 11%]
tests/test_extractors.py::TestSkillsExtractor::test_extract_skills PASSED [ 22%]
tests/test_extractors.py::TestSkillsExtractor::test_invalid_data_format PASSED [ 33%]
tests/test_processors.py::TestSkillsAnalyzer::test_analyze_skills PASSED [ 44%]
tests/test_processors.py::TestSkillsAnalyzer::test_empty_data PASSED     [ 55%]
tests/test_scrapers.py::TestLinkedInScraper::test_fetch_data PASSED      [ 66%]
tests/test_scrapers.py::TestLinkedInScraper::test_parse_data PASSED      [ 77%]
tests/test_scrapers.py::TestGlassdoorScraper::test_fetch_data PASSED     [ 88%]
tests/test_scrapers.py::TestGlassdoorScraper::test_parse_data PASSED     [100%]

============================== 9 passed in 0.58s ==============================
```

## Generating Reports

### Global Report (190+ Job Postings)

```bash
python scripts/generate_report.py
```

This analyzes **190+ job postings** from LinkedIn and Glassdoor (international companies) and generates 4 report files in `data/processed/`:

| File | Format | Description |
|------|--------|-------------|
| `devops_skills_report_TIMESTAMP.txt` | Text | Full analysis report with insights |
| `devops_skills_data_TIMESTAMP.json` | JSON | Structured data for programmatic access |
| `devops_skills_analysis_TIMESTAMP.csv` | CSV | Skills ranking (Excel-compatible) |
| `job_postings_TIMESTAMP.csv` | CSV | All job postings data |

### Sri Lanka Local Jobs Report (50 Job Postings)

```bash
python scripts/generate_sri_lanka_report.py
```

This analyzes **50 job postings** from Sri Lankan companies and generates 4 specialized reports:

| File | Format | Description |
|------|--------|-------------|
| `sri_lanka_devops_report_TIMESTAMP.txt` | Text | Sri Lanka market analysis |
| `sri_lanka_devops_data_TIMESTAMP.json` | JSON | Sri Lanka jobs data |
| `sri_lanka_skills_analysis_TIMESTAMP.csv` | CSV | Sri Lanka skills ranking |
| `sri_lanka_job_postings_TIMESTAMP.csv` | CSV | Sri Lanka job listings |

**Sri Lankan Companies Included:**
- Major IT: WSO2, Virtusa, IFS, 99x, Sysco LABS, MillenniumIT, Zone24x7
- International offices: Accenture, Deloitte, HSBC, Citi, Standard Chartered
- Growing tech: Dialog Axiata, Arimac, hSenid, CodeGen, and more

### Report Contents

The generated reports include:

1. **Executive Summary**: Total jobs analyzed, unique skills count
2. **Top 15 Skills Ranking**: With visual bar charts
3. **Skills by Category**: Cloud, Containerization, CI/CD, etc.
4. **Job Postings List**: All scraped jobs with details
5. **Key Insights**: Recommendations based on analysis

## Sample Output

### Global Analysis (190 Job Postings)

| Rank | Skill | Jobs | Percentage | Category |
|------|-------|------|------------|----------|
| 1 | Kubernetes | 187 | 98.4% | Containerization |
| 2 | Docker | 184 | 96.8% | Containerization |
| 3 | AWS | 166 | 87.4% | Cloud Platforms |
| 4 | Terraform | 154 | 81.1% | IaC & Config Management |
| 5 | Python | 108 | 56.8% | Programming Languages |
| 6 | Jenkins | 60 | 31.6% | CI/CD Tools |
| 7 | Ansible | 43 | 22.6% | IaC & Config Management |
| 8 | Go | 36 | 18.9% | Programming Languages |
| 9 | Azure | 27 | 14.2% | Cloud Platforms |
| 10 | Prometheus | 27 | 14.2% | Monitoring |

### Sri Lanka Market Analysis (50 Job Postings)

| Rank | Skill | Jobs | Percentage | Category |
|------|-------|------|------------|----------|
| 1 | Kubernetes | 50 | 100% | Containerization |
| 2 | Docker | 50 | 100% | Containerization |
| 3 | AWS | 47 | 94% | Cloud Platforms |
| 4 | Python | 38 | 76% | Programming Languages |
| 5 | Terraform | 30 | 60% | IaC & Config Management |
| 6 | Jenkins | 24 | 48% | CI/CD Tools |
| 7 | Ansible | 15 | 30% | IaC & Config Management |
| 8 | Azure | 10 | 20% | Cloud Platforms |
| 9 | Go | 7 | 14% | Programming Languages |
| 10 | Linux | 7 | 14% | Operating Systems |
| 9 | Azure | 6 | 15.0% | Cloud Platforms |
| 10 | GCP | 6 | 15.0% | Cloud Platforms |

### Key Insights

- **Must-Have Skills**: Kubernetes, Docker, AWS (appear in 75%+ of jobs)
- **Dominant Cloud Platform**: AWS (77.5% of postings)
- **IaC Standard**: Terraform is the most requested IaC tool (65%)
- **Top Programming Languages**: Python, Go, Java

## API Reference

### SkillsExtractor

```python
from extractors.skills_extractor import SkillsExtractor

extractor = SkillsExtractor()
skills = extractor.extract_skills(job_postings)
# Returns: set of unique skills
```

### SkillsAnalyzer

```python
from processors.skills_analyzer import SkillsAnalyzer

analyzer = SkillsAnalyzer()
skill_counts = analyzer.analyze_skills(cleaned_data)
# Returns: dict with skill frequencies

top_skills = analyzer.get_top_skills(10)
# Returns: list of (skill, count) tuples
```

### LinkedInScraper / GlassdoorScraper

```python
from scrapers.linkedin_scraper import LinkedInScraper

scraper = LinkedInScraper()
jobs = scraper.fetch_data(job_title="DevOps Engineer")
# Returns: list of job dictionaries with title, company, skills
```

## Skills Taxonomy

The application categorizes skills into the following groups:

| Category | Skills |
|----------|--------|
| **Cloud Platforms** | AWS, Azure, GCP, OCI |
| **Containerization** | Docker, Kubernetes, OpenShift |
| **IaC & Config Management** | Terraform, Ansible, Chef, Puppet |
| **CI/CD Tools** | Jenkins, GitLab CI, CircleCI, Spinnaker |
| **Programming Languages** | Python, Go, Java, Ruby, Bash |
| **Monitoring & Observability** | Prometheus, Grafana, DataDog, ELK Stack |
| **Version Control** | Git, GitHub, Bitbucket |

## Docker Deployment

### Build and Run with Docker

```bash
docker build -t devops-skills-extractor .
docker run devops-skills-extractor
```

### Using Docker Compose

```bash
docker-compose up
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Install dev dependencies
pip install -r requirements.txt
pip install pytest pytest-cov black isort

# Run tests before committing
python -m pytest tests/ -v

# Format code
black src/ tests/
isort src/ tests/
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- LinkedIn and Glassdoor for job posting data
- The open-source community for invaluable tools and libraries
- All contributors who help improve this project

---

**Made with ❤️ for the DevOps community**