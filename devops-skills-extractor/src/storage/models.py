from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class JobPosting(Base):
    __tablename__ = 'job_postings'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    company = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    date_posted = Column(String(50), nullable=False)
    source = Column(String(50), nullable=False)  # e.g., LinkedIn, Glassdoor

class Skill(Base):
    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    job_posting_id = Column(Integer, nullable=False)  # Foreign key to JobPosting
    proficiency_level = Column(String(50))  # e.g., Beginner, Intermediate, Expert