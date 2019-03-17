import os

from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")
SOURCES = 'https://newsapi.org/v2/sources'
TOP_HEAD = 'https://newsapi.org/v2/top-headlines'
