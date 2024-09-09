import requests
import os
from dotenv import load_dotenv
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

backend_url = os.getenv("backend_url", default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    "sentiment_analyzer_url", default="http://localhost:5050/"
)


def get_request(endpoint, **kwargs):
    """Send a GET request to the backend with optional parameters."""
    params = ""
    if kwargs:
        params = "&".join([f"{key}={value}" for key, value in kwargs.items()])

    request_url = f"{backend_url}{endpoint}?{params}"
    logger.info(f"GET from {request_url}")

    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        logger.error(f"Network exception occurred: {err}")
        return None


def analyze_review_sentiments(text):
    """Analyze the sentiment of a given text."""
    request_url = f"{sentiment_analyzer_url}analyze/{text}"
    logger.info(f"Sentiment analysis request to {request_url}")

    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        logger.error(f"Network exception occurred: {err}")
        return None


def post_review(data_dict):
    """Send a POST request to insert a review."""
    request_url = f"{backend_url}/insert_review"
    logger.info(f"POST to {request_url} with data {data_dict}")

    try:
        response = requests.post(request_url, json=data_dict)
        return response.json()
    except Exception as err:
        logger.error(f"Network exception occurred: {err}")
        return None
