import sys
import requests

class Receiver:
    def __init__(self):
        self.url = 'http://localhost:8000'


    def get(self, path):
        response = requests.get(self.url + path)
        return response.status_code, response.text

