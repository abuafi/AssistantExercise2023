from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from warnings import warn
import requests

class CourseParser(ABC):
    def __init__(self, url) -> None:
        self.url = url

    def warn(self, string):
        warn(f"{string} in parser {str(self.__class__)} for url {self.url}")

    def parse_stats(self):
        req = requests.get(self.url, timeout=3)
        if req.status_code != 200:
            self.warn(f"Unexpected status code {req.status_code}")
            return

        html = req.text
        soup = BeautifulSoup(html, "html.parser")
        try:
            staff = self.parse_staff(soup)
            description = self.parse_description(soup).strip()
            return {
            'Teaching Staff':staff,
            'Description':description
            }
        except Exception:
            self.warn(f"Exception in parser")

    @abstractmethod
    def parse_staff(self, soup:BeautifulSoup): pass

    @abstractmethod
    def parse_description(self, soup:BeautifulSoup): pass