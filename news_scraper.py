import requests
from bs4 import BeautifulSoup

# URL of a news website (You can replace this with another news source)
URL = 'https://www.bbc.com/news'

# Send HTTP request
response = requests.get(URL)

# Check for successful response
if response.status_code == 200:
    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all headline tags (commonly h2 or h3 in BBC)
    headlines = soup.find_all(['h2', 'h3'])

    # Extract and clean text
    extracted_headlines = [headline.get_text(strip=True) for headline in headlines if headline.get_text(strip=True)]


    with open('headlines.txt', 'w', encoding='utf-8') as file:
        for index, title in enumerate(extracted_headlines, start=1):
            file.write(f"{index}. {title}\n")

    print(f"Scraped {len(extracted_headlines)} headlines and saved to 'headlines.txt'")
else:
    print(f"Failed to fetch page, status code: {response.status_code}")
