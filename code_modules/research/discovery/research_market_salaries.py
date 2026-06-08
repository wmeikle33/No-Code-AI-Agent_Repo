from statistics import mean
from collections import Counter
import re


def research_market_salaries(job_title, location, experience_level):
    return {
        "job_title": job_title,
        "location": location,
        "experience_level": experience_level,
        "status": "requires_external_salary_api",
        "recommended_sources": ["BLS", "Levels.fyi", "Payscale", "Salary.com", "Indeed"],
        "output_fields": ["p25_salary", "median_salary", "p75_salary", "currency"]
    }

