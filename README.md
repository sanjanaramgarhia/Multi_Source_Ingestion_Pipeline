# Multi-Source Ingestion Pipeline

A real-world data ingestion pipeline that fetches data from multiple sources
(API, CSV, Web Scraping), normalizes it into a common JSON schema, and stores
the output for downstream processing.

## Sources
- NewsAPI (REST API)
- Local CSV file
- Web Scraper

## Workflow
NewsAPI → Fetch + Parse  
CSV → Read + Parse  
Web → Scrape + Parse  
→ Normalize  
→ Save to JSON  

## Output Schema
```json
{
  "title": "string",
  "content": "string",
  "source": "string",
  "url": "string",
  "fetched_at": "ISO-8601 timestamp"
}

## Run
python main.py

## Test
pytest -v
