import requests
import json

# Your API key from NewsAPI
API_KEY = 'faad4557f1e348649b42d2e179491af0'

# Base URL for the Top Headlines endpoint
url = 'https://www.dawn.com/v2/everything'

# Parameters for the request
params = {
    'apiKey': API_KEY,           # Your NewsAPI API key
    'country': 'pak',             # You can change this to any country code (e.g., 'us', 'gb', 'in')
    'category': 'sports',       # You can change this to 'business', 'technology', 'sports', etc.
    'pageSize': 5,               # Number of results per page (you can adjust this)
    'language': 'en'             # News language (English in this case)
}

# Send GET request to News API
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Convert the response to JSON format
    news_data = response.json()

    # Print the top headlines
    print("Top Headlines:")
    for article in news_data['articles']:
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"Source: {article['source']['name']}")
        print(f"URL: {article['url']}")
        print('---' * 10)
else:
    print(f"Error {response.status_code}: {response.text}")
