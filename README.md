## Usage

1. Scraper Factory (Abstract Factory)
   The project utilizes the Abstract Factory design pattern to create scraper instances for specific marketplaces. The ScraperFactory class provides an abstract interface for creating different types of scrapers, and concrete factory classes, such as EbayScraperFactory, implement this interface to create scraper instances for specific marketplaces.

To create a scraper instance for a particular marketplace, follow these steps:
from scraperFactory import ScraperFactory, EbayScraperFactory

# Define the marketplace and product name

marketplace_name = "ebay"
product_name = "rolex"

# Create a scraper factory instance for eBay

factory = EbayScraperFactory(product_name)

# Use the factory to create a scraper instance

scraper = factory.create_scraper()

# Scraping configuration

num_pages_to_scrap = optional
num_items_per_page = optional

# Start scraping

scraper.scrape_marketplace(num_pages_to_scrap, num_items_per_page)

This design pattern allows for easy extensibility by adding new concrete factory classes for additional marketplaces. It separates the creation of scraper objects from their use, promoting a cleaner and more maintainable codebase.

## Design Pattern - Abstract Factory

The Abstract Factory design pattern is employed to create families of related objects without specifying their concrete classes. In this project, the ScraperFactory acts as the abstract factory, and concrete factory classes like EbayScraperFactory are responsible for creating scraper instances tailored to specific marketplaces.

By using the Abstract Factory pattern, the project achieves the following benefits:

Extensibility: New marketplaces can be easily added by implementing additional concrete factory classes, ensuring the project can adapt to changing requirements.

Maintainability: The separation of object creation from client code enhances code maintainability and readability.

Consistency: The pattern ensures that all scraper instances adhere to a common interface, providing consistency in usage.

Flexibility: It allows clients to switch between different families of objects (scrapers) without modifying their code.

This design pattern empowers the project to grow and accommodate various marketplaces seamlessly, making it a robust solution for web scraping tasks.
