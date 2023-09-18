from scraper.ebayScraper import EbayScraper


def createScraper(marketplace_name, product_name):
    """
    Factory function to create a scraper instance for a specific marketplace.

    Args:
        marketplace_name (str): The name of the marketplace for which to create the scraper.
        product_name (str): The name or keyword of the product to search for on the marketplace.

    Returns:
        MarketplaceScraper: An instance of a subclass of MarketplaceScraper specific to the chosen marketplace.

    Raises:
        Exception: If an unknown or unsupported marketplace name is provided.
    """
    if marketplace_name == "ebay":
        return EbayScraper(product_name)
    else:
        raise Exception("Unkown marketplace")
