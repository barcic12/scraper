from abc import ABC, abstractmethod
import math
import requests
from bs4 import BeautifulSoup
from lxml import etree


class MarketPlaceScraper(ABC):
    """
    Abstract base class for marketplace scrapers.

    Attributes:
        sesrch_word (str): The search keyword for the marketplace.
        number_of_pages (int): The number of pages to scrape.
        page_query (str): The query parameter for pagination in the URL.
        search_word_url (str): The URL for searching products in the marketplace.

    Methods:
        scrape_marketplace(num_pages_to_scrap=float('inf'), num_items_per_page=float('inf')):
            Scrapes the marketplace for products.

        create_product(product_url):
            Abstract method to create a product instance based on the product URL.

        scrape_feed_page(feed_page_url):
            Scrapes a feed page from the marketplace.

        retrieve_items_URLs(feed_page, number_of_items_to_scrap):
            Retrieves a list of item URLs from the feed page.

        get_datials_data(items_URLs):
            Retrieves details data for each item URL.

        count_pages(total_results_xpath, total_items_per_page_xpath):
            Counts the number of pages to scrape based on the total results and items per page.

    """

    def __init__(self, sesrch_word):
        """
        Initializes a new instance of the MarketplaceScraper class.

        Args:
            sesrch_word (str): The search keyword for the marketplace.
        """
        self.sesrch_word = sesrch_word
        self.number_of_pages = None
        self.page_query = None
        self.search_word_url = None

    def scrape_marketplace(self, num_pages_to_scrap=float('inf'), num_items_per_page=float('inf')):

        for i in range(1, min(num_pages_to_scrap, self.number_of_pages)+1):
            feed_page_url = f'{self.search_word_url}&{self.page_query}={i}'
            feed_page = self.scrape_feed_page(feed_page_url)
            items_URLs = self.retrieve_items_URLs(
                feed_page, num_items_per_page)
            self.get_datials_data(items_URLs)

    @abstractmethod
    def create_product(self, product_url):
        """
        Abstract method to create a product instance based on the product URL.

        Args:
            product_url (str): The URL of the product.

        Returns:
            Product: An instance of a product class.
        """
        pass

    def scrape_feed_page(self, feed_page_url):
        """
        Scrapes a feed page from the marketplace.

        Args:
            feed_page_url (str): The URL of the feed page to scrape.

        Returns:
            list: List of items extracted from the feed page.
        """
        items = []
        response = requests.get(feed_page_url)
        if not response.ok:
            print("Server rsponded: ", response.status_code)
            return
        try:
            soup = BeautifulSoup(response.text, 'lxml')
            dom = etree.HTML(str(soup))
            items = dom.xpath(self.__class__.xpath_item_a_tag_elemnt)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        return items

    def retrieve_items_URLs(self, feed_page, number_of_items_to_scrap):
        """
        Retrieves a list of item URLs from the feed page.

        Args:
            feed_page (list): List of items extracted from the feed page.
            number_of_items_to_scrap (int): The maximum number of items to retrieve.

        Returns:
            list: List of item URLs.
        """
        url_list = []
        for i in range(min(number_of_items_to_scrap+1, len(feed_page))):
            try:
                url_list.append(feed_page[i].get("href"))
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                continue
        return url_list

    def get_datials_data(self, items_URLs):
        """
        Retrieve details data for each item URL and save it as JSON.

        This method iterates through a list of item URLs, creates product objects for each URL,
        retrieves detailed data for those products, and saves the data as JSON files.

        Args:
            items_URLs (list): List of item URLs to retrieve data for.

        Example:
            Given a list of item URLs, this method creates product objects, populates them with data,
            and saves the data as JSON files for further analysis.

        """
        for product_url in items_URLs:
            product = self.create_product(product_url)
            try:
                product = product.populate()
                product.save_as_json_file(self.sesrch_word)
            except Exception as e:
                print(f"An error occurred: {str(e)}")

    def count_pages(self, total_results_xpath, total_items_per_page_xpath):
        """
        Counts the number of pages to scrape based on the total results and items per page.

        Args:
            total_results_xpath (str): XPath to extract the total number of results.
            total_items_per_page_xpath (str): XPath to extract the number of items per page.

        Returns:
            int: The total number of pages to scrape.
        """
        response = requests.get(self.search_word_url)
        if not response.ok:
            print("Server rsponded: ", response.status_code)
        try:
            soup = BeautifulSoup(response.text, 'lxml')
            dom = etree.HTML(str(soup))
            total_items_elements = dom.xpath(total_results_xpath)
            total_items_num = int(
                total_items_elements[0].text.replace(",", ""))
            items_in_page_elemnts = dom.xpath(total_items_per_page_xpath)
            item_in_page_num = int(
                items_in_page_elemnts[0].text.replace(",", ""))
        except Exception as e:
            print(f"An error occurred: {str(e)}")

        return math.ceil(total_items_num/item_in_page_num)
