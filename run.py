from scraper.scraperFactory import createScraper

# This argument would be given by the user
market_name = "ebay"
product_name = "rolex"

if __name__ == '__main__':
    """
    Main script for scraping a marketplace for product information.

    This script creates a scraper instance for the specified marketplace and product,
    then initiates the scraping process with optional parameters for a limited number of pages and items per page.

    Usage:
        Modify the 'market_name' and 'product_name' variables to specify the marketplace and product to scrape.
        Optionally, adjust the 'num_pages_to_scrap' and 'num_items_per_page' parameters as needed. 
        They are optional and default to infinity, meaning all available pages and items will be scraped.

    Example:
        To scrape eBay for Rolex products on the first page with 5 items per page, 
        set 'num_pages_to_scrap=1' and 'num_items_per_page=5'. 
        Omitting these parameters will scrape all available pages and items.

    """
    scraper = createScraper(market_name, product_name)
    scraper.scrape_marketplace()
