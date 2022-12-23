from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from warnings import warn
import requests

class CourseParser(ABC):
    def __init__(self, url) -> None:
        self.url = url

    def parse_stats(self):
        req = requests.get(self.url, timeout=3)
        html = req.text
        soup = BeautifulSoup(html, "html.parser")
        return {
        'Teaching Staff':self.parse_staff(soup),
        'Description':self.parse_description(soup).strip()
        }

    @abstractmethod
    def parse_staff(self, soup:BeautifulSoup): pass

    @abstractmethod
    def parse_description(self, soup:BeautifulSoup): pass