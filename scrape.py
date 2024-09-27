from selenium import webdriver # type: ignore
from bs4 import BeautifulSoup # type: ignore
import time
import requests  # type: ignore
import json

BASE_URL = "https://www.notion.so/help"

def get_help_articles():
    # Set up the browser (you can download the right driver for Chrome or Firefox)
    driver = webdriver.Chrome()  # or webdriver.Firefox()
    driver.get(BASE_URL)
    
    # Wait for the page to fully load (increase time if needed)
    time.sleep(5)
    
    # Get the page source after JavaScript execution
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Now find article links (adjust the class or tag based on the actual HTML)
    articles = soup.find_all('a', href=True)
    
    links = []
    for article in articles:
        article_url = article.get('href')
        if article_url and 'notion-academy' not in article_url:
            if not article_url.startswith('http'):
                article_url = BASE_URL + article_url
            links.append(article_url)
    
    driver.quit()  # Close the browser
    print(f"Found {len(links)} articles")
    return links

    
def get_article_content(article_url):
    response = requests.get(article_url)
    if response.status_code == 404:
        print(f"404 Error: {article_url}")
        return None, None
    elif response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1')
        if title:
            title = title.text.strip()
        else:
            title = "No title"
        content = [elem.text.strip() for elem in soup.find_all(['h2', 'p', 'li'])]
        return title, "\n".join(content)
    else:
        print(f"Error fetching article content: {response.status_code}")
        return None, None

    
def chunk_content(title, content, max_chunk_size=750):
    words = content.split()  # Split the content into words
    current_chunk = []
    current_length = 0
    chunks = []

    for word in words:
        current_length += len(word) + 1  # Count the word length + space
        current_chunk.append(word)

        # When the chunk reaches the max size, store it and reset
        if current_length >= max_chunk_size:
            chunks.append(' '.join(current_chunk))
            current_chunk = []
            current_length = 0

    # Add any remaining content as a chunk
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return [(title, chunk) for chunk in chunks]

def save_to_json(chunks, filename='notion_help_chunks.json'):
    with open(filename, 'w') as f:
        json.dump(chunks, f, indent=4)

def main():
    articles = get_help_articles()
    all_chunks = []

    for article_url in articles:
        title, content = get_article_content(article_url)
        if title and content:
            chunks = chunk_content(title, content)
            all_chunks.extend(chunks)
    
    save_to_json(all_chunks)
    print("Content chunked and saved to JSON file.")

if __name__ == "__main__":
    main()