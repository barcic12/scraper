
from product.ebayProduct import EbayProduct
from scraper.marketpPaceScraper import MarketPlaceScraper


class EbayScraper(MarketPlaceScraper):
    """
    This class represents an eBay scraper for retrieving product data from eBay.

    Args:
        search_word (str): The search keyword to use on eBay.

    Attributes:
        xpath_item_a_tag_elemnt (str): The XPath expression to extract item URLs from a feed page.
        page_query (str): The query parameter used for paginating through search results.
        search_word_url (str): The URL used for searching eBay with the specified search word.
        number_of_pages (int): The total number of pages in the search results.

    Methods:
        create_product(product_url): Create an instance of the `EbayProduct` class for a given product URL.
    """
    xpath_item_a_tag_elemnt = "//div[@class='s-item__wrapper clearfix']/div[@class='s-item__image-section']/div[@class='s-item__image']/a"

    def __init__(self, search_word):
        """
        Initialize the eBay scraper with the search word and set up necessary attributes.

        Args:
            search_word (str): The search keyword to use on eBay.
        """
        super().__init__(search_word)
        self.page_query = "_pgn"
        self.search_word_url = f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={self.sesrch_word}&_sacat=0"
        total_results_xpath = "//h1[@class='srp-controls__count-heading']/span[@class='BOLD']"
        total_items_per_page_xpath = "//span[@id='srp-ipp-menu']//span[@class='btn__cell']/span"
        self.number_of_pages = self.count_pages(
            total_results_xpath, total_items_per_page_xpath)

    def create_product(self, product_url):
        """
        Create an instance of the `EbayProduct` class for a given product URL.

        Args:
            product_url (str): The URL of the eBay product.

        Returns:
            EbayProduct: An instance of the `EbayProduct` class.
        """
        product = EbayProduct(product_url)
        return product
