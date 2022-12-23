from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from warnings import warn
import requests

class CourseParser(ABC):
    def __init__(self, url:str) -> None:
        """
        Initializer for objects of type CourseParser.

        Parameters:
            url (str): Url of the page to be parsed
        """
        self.url = url

    def warn(self, string):
        """
        Prints a warning when something goes wrong.

        Parameters:
            string (str): Some information about the error
        """
        warn(f"{string} in parser {str(self.__class__)} for url {self.url}")

    def parse_stats(self):
        """
        Sends a request to the url to parse and parses the necessary information.

        Returns:
            None: When the page doesn't respond with status 200 or an exception 
                is raised during parsing
            dict: A dictionary containing the crawled statistics, 
                namely the name of the teaching staff and the description of the course.
        """
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
    def parse_staff(self, soup:BeautifulSoup): 
        """
        Abstract method to implement to parse the teaching staff names.

        Parameters:
        soup (BeautifulSoup): An object containing the entire document

        Returns:
        list: A list containing the names of the directors and assistants
        """
        pass

    @abstractmethod
    def parse_description(self, soup:BeautifulSoup): 
        """
        Abstract method to implement to parse the course description.

        Parameters:
        soup (BeautifulSoup): An object containing the entire document

        Returns:
        str: A string containing the course description
        """
        pass