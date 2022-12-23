from bs4 import BeautifulSoup
from parsers.CourseParser import CourseParser

class CourseParserUSI(CourseParser):

    def parse_staff(self, soup:BeautifulSoup):
        """
        Parses teaching staff names for an USI webpage.

        Parameters:
        soup (BeautifulSoup): An object containing the entire document

        Returns:
        list: A list containing the names of the directors and assistants
        """
        people = soup.find("h2", text="People").parent
        directors = [s.parent.find("a").text for s in people.find_all("p", text="Course director")]
        assistants = [s.parent.find("a").text for s in people.find_all("p", text="Assistant")]
        return directors + assistants

    def parse_description(self, soup:BeautifulSoup):
        """
        Parses course description for an USI webpage.

        Parameters:
        soup (BeautifulSoup): An object containing the entire document

        Returns:
        str: A string containing the course description
        """
        return soup.find("h2", text="Description").parent.find("div", {"class":"text_container"}).text
