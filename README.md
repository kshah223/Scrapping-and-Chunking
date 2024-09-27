# Scraping and Chunking Notion Help Articles

This Python project scrapes articles from the Notion Help Center, extracts their content, and chunks it into smaller sections before saving the data into a JSON file. The project uses Selenium to handle JavaScript-rendered pages, BeautifulSoup for parsing the HTML, and Requests for HTTP requests.

## Features

- **Scraping Notion Help Articles**: Scrapes article links from the Notion Help Center.
- **Article Content Extraction**: Fetches and extracts the content of each article.
- **Content Chunking**: Breaks down large article content into smaller, manageable chunks of text.
- **JSON Storage**: Saves the chunked content into a JSON file for easy processing.

## Requirements

To run the project, you will need the following:

- **Python 3.x**
- **Selenium**: To handle the dynamic JavaScript content on the Notion Help Center.
- **BeautifulSoup**: To parse the HTML content.
- **Requests**: To make HTTP requests to fetch article content.
- **Chrome WebDriver** (or another browser driver): Required by Selenium to interact with the webpage.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/kshah223/Scrapping-and-Chunking.git
    cd Scraping-and-Chunking
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

    If you haven't created a `requirements.txt` file, here are the main dependencies:

    ```text
    requests
    beautifulsoup4
    selenium
    ```

3. Download and set up the [ChromeDriver](https://chromedriver.chromium.org/downloads) or another WebDriver that matches your browser. Place the WebDriver in your system's PATH or specify the location in the script.

## Usage

To run the script, execute the following command:

```bash
python scrape.py
