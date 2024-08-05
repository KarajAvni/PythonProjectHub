import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send an HTTP request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Example: Extract all text from paragraphs
        paragraphs = soup.find_all('p')
        for paragraph in paragraphs:
            print(paragraph.get_text())

        # Example: Extract all links
        links = soup.find_all('a')
        for link in links:
            print(link.get('href'))

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Replace 'https://example.com' with the URL of the website you want to scrape
scrape_website('https://example.com')

