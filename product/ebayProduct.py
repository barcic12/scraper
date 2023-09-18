from product.product import Product

class EbayProduct(Product):
    """
    Represents a product listing on eBay.

    Attributes:
        title_xpath (str): XPath to extract the product title.
        description_path (str): XPath to extract the product description.
        price_xpath (str): XPath to extract the product price.
        image_xpath (str): XPath to extract the product image URL.
        market_name (str): The name of the marketplace (e.g., "ebay").
        extract_id_func (function): A lambda function to extract the product ID from the product URL.

    Methods:
        __init__(self, product_url):
            Initializes a new instance of the EbayProduct class.

    """
    
    title_xpath = "//h1[@class='x-item-title__mainTitle']/span[@class='ux-textspans ux-textspans--BOLD']"
    description_path = "//div[@class='vim d-item-description']/iframe"
    price_xpath = "//div[@class='x-price-primary']/span[@class='ux-textspans']"
    image_xpath =  "//div[@class='ux-image-carousel-container']//div[@class='ux-image-carousel-item active image']//img"
    market_name = "ebay"
    extract_id_func = lambda url : url.split("/itm/")[1].split("?")[0]
    
    def __init__(self,product_url):
        """
        Initializes a new instance of the EbayProduct class.

        Args:
            product_url (str): The URL of the eBay product listing.
        """
        super().__init__()
        self.product_url = product_url
        