import json
from bs4 import BeautifulSoup
from lxml import etree
import os
import requests

class Product(object):
    """
    This class represents a product and provides methods for populating its attributes from a URL and saving it as a JSON file.

    Attributes:
        id (str): The identifier for the product.
        title (str): The title of the product.
        description (str): The description of the product.
        price (str): The price of the product.
        image_path (str): The path to the product's image.
        product_url (str): The URL of the product's webpage.

    Methods:
        populate(): Populate the product's attributes by scraping data from the product's webpage.
        save_as_json_file(): Save the product's attributes as a JSON file.
        fields_to_json(): Convert the product's attributes to a JSON-compatible format.
    """
    def __init__(self):
        """
        Initialize an instance of the Product class with default attribute values.
        """
        self.id = None
        self.title = None
        self.description = None
        self.price = None
        self.image_path= None
        self.product_url = None
  
  
    def populate(self):
        """
        Populate the product's attributes by scraping data from the product's webpage.

        Returns:
            Product: The product instance with populated attributes.
        """
        concrete_class = self.__class__
        response = requests.get(self.product_url)
        if not response.ok:
            raise Exception(f"Server rsponded: {response.status_code}")
        try: 
            soup = BeautifulSoup(response.text, 'lxml')
            dom = etree.HTML(str(soup))
            self.id = concrete_class.extract_id_func(self.product_url)
            self.title ="".join(item.text for item in dom.xpath(concrete_class.title_xpath))
            self.description = dom.xpath(concrete_class.description_path)[0].get('src')
            self.price = dom.xpath(concrete_class.price_xpath)[0].text.strip()
            self.image_path = dom.xpath(concrete_class.image_xpath)[0].get('src')
        except  Exception as e:
            print(f"An error occurred: {str(e)}")
        return self
        
        
    def save_as_json_file(self,item_name):
        """
    Save the product's attributes as a JSON file in a folder named after the market.

    This method saves the product's attributes, such as title, description, price, and image path, as a JSON file.
    The JSON file is named after the market and product ID. If the folder for the market's JSON files doesn't exist,
    it is created automatically.

    Args:
        item_name (str): A name or identifier for the specific item.
    
    Raises:
        Exception: If an error occurs while saving the JSON file.

 

    """
        concrete_class = self.__class__
        file_name = f"{concrete_class.market_name}_{self.id}" 
        folder_path = f'./{concrete_class.market_name}-{item_name}-JsonFolder'
        try:
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            with open(f'./{folder_path}/{file_name}.json', 'w') as json_file:
                product_json = self.fields_to_json()
                json.dump(product_json, json_file,indent=4)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            
            
    def fields_to_json(self):
        """
        Convert the product's attributes to a JSON-compatible format.

        Returns:
            dict: A dictionary containing the product's attributes in JSON format.
        """
        json = {
            'title':self.title,
            'description':self.description,
            "price":self.price,
            'image path':self.image_path
        }
        return json
        
