# Scraper

A Python web scraping project for extracting product information from various online marketplaces.

## Introduction

This project provides a framework for scraping product data from different online marketplaces. It includes a set of classes and functions for scraping product details, saving them as JSON files, and more. The project currently supports eBay as a sample marketplace, but it can be extended to include other platforms.

## Requirements

- Python 3.x
- Libraries: requests, BeautifulSoup, lxml

## Usage

### 1. Scraper Factory

To create a scraper instance for a specific marketplace, you can use the `createScraper` function provided in `scraperFactory.py`. Pass the name of the marketplace and the product name as arguments.

```python
from scraperFactory import createScraper

# Define the marketplace and product name
marketplace_name = "ebay"
product_name = "rolex"

# Create a scraper instance
scraper = createScraper(marketplace_name, product_name)

# Scraping configuration
num_pages_to_scrap = optional
num_items_per_page : optional

# Start scraping
scraper.scrape_marketplace(num_pages_to_scrap, num_items_per_page)
```
