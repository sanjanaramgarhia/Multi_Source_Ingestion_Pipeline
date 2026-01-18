# Development process

## Problem Statement
Build ingestion connectors that fetch data from multiple sources and store the output in a unified JSON format..

## Breakdown 
1: NewsAPI ingestion
2: CSV ingestion
3: Web scraping
4: Normalization
5: Saving output

## Task 1:
**AI Prompt Used:**
Build a Python data fetcher that retrieves news articles from NewsAPI using REST API.
Handle API key authentication, timeouts, and missing fields.
Return the data in a structured format suitable for further processing.

**AI Response:**
The AI provided a Python function using the requests library to call the NewsAPI endpoint and parse the JSON response. The function extracted fields such as title, description, content, URL, and published date.

**My Review:**
The API call logic was correct.
Error handling for missing environment variables was not present.
Returned fields were not aligned with a common schema.

**Final Code**
API key loaded using environment variables.
Clear error raised if the key is missing.
API field publishedAt mapped to internal fetched_at.
Output passed through a normalization layer.
Returned data as a list of normalized articles.

--------------------------------------## Task 2: ---------------------------------------------

**AI Prompt Used:**
Write a Python function to read a local CSV file containing articles.
Extract the title and text fields and return the data in dictionary format.

**AI Response:**
The AI generated a function csv.DictReader to iterate through rows and convert each row into a dictionary.

**My Review:**
CSV reading logic was correct.
Some fields required by the final schema were missing.
No handling for missing values.

**Final Code**
CSV rows converted into article records.
Missing fields handled using default values.
Each record passed through the same normalization function used by NewsAPI.

--------------------------------------## Task 3: ---------------------------------------------

**AI Prompt Used:**
Create a Python web scraper that fetches article title and content from a website.

**AI Response:**
The AI suggested using HTTP requests and HTML parsing to extract content from a web page and return it as a dictionary.

**My Review:**
Scraper logic worked for basic cases.
Web content was unstructured and inconsistent.
Scraper needed to return data in the same format as other sources.

**Final Code**
Web content scraped and cleaned.
Title and content extracted.
Source tagged as "web".
Output normalized using the shared normalization layer.

--------------------------------------## Task 4: ---------------------------------------------

**AI Prompt Used:**
Design a common normalization function that converts data from different sources into a single consistent JSON schema.

**AI Response:**
The AI proposed a normalization function that accepted multiple fields and returned a dictionary with default values for missing data.

**My Review:**
The response was all correct.

**Final Code**
{
  "title": "string",
  "content": "string",
  "source": "string",
  "url": "string",
  "fetched_at": "ISO-8601 timestamp"
}

--------------------------------------## Task 5: ---------------------------------------------

**AI Prompt Used:**
Write a Python entry point that combines results from multiple data sources and saves the output as JSON.

**AI Response:**
The AI suggested combining lists from each fetcher and writing them to a JSON file.

**My Review:**
Combining logic was correct.
Environment variables needed to be loaded before execution.
Testing required isolation from external dependencies.

**Final Code**
main.py orchestrates all fetchers.
One article selected per source.
Final output saved to output/articles.json.
Environment variables loaded at entry point.
Integration tested using pytest with mocked fetchers.

# LEARNINGS

Learned how Python treats folders as packages and understood the role of __init__.py in enabling imports across different directories within a project.

Gained hands-on experience with proper project structure and how to access functions from other modules in a scalable way.

Learned the difference between manual testing and automated unit testing.

Used pytest for the first time to write unit and integration tests instead of relying on print-based debugging.

Learned how to test code in isolation without depending on external APIs or real data sources.