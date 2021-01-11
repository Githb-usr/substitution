import requests

from config.settings import API_BASE_URL

class Api:
    
    def get_products(self):
        result = requests.get(API_BASE_URL)
        