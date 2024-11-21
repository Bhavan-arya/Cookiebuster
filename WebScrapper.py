import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send a GET request to the specified URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find and extract specific data
        # Example: Extracting all article titles from a blog page
        titles = soup.find_all('h2')  # Assuming titles are in <h2> tags
        
        print("Article Titles:")
        for title in titles:
            print(title.get_text(strip=True))  # Print the text of each title
    else:
        print(f"Failed to retrieve data: {response.status_code}")

if __name__ == "__main__":
    url = "https://example.com"  # Replace with the target URL
    scrape_website(url)
