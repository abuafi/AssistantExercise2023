from urllib.parse import urlparse
from threading import Thread
from queue import Queue
from warnings import warn

from concurrent.futures import ThreadPoolExecutor

from parsers.CourseParserUSI import CourseParserUSI

parse_switch = {
    "search.usi.ch": CourseParserUSI
}

def parse_url(url:str) -> None:
    domain = urlparse(url).netloc
    try:
        parser = parse_switch[domain](url)
        return parser.parse_stats()
    except KeyError:
        warn(f"Domain name {domain} not supported!")

if __name__ == "__main__":
    urls = [
    "https://search.usi.ch/en/courses/35265726/advanced-java-programming",
    "https://studentservices.uzh.ch/uzh/anonym/vvz/index.html?sap-language=EN&sap-ui-language=EN#/details/2022/004/SM/51048814/50000003/Wirtschaftswissenschaftliche%2520Fakult%25C3%25A4t/50773260/Master%2520of%2520Science%2520UZH%2520in%2520Informatik%2520(RVO16)/50774406/Computing%2520and%2520Economics",
    "https://search.usi.ch/en/courses/35265666/programming-styles",
    "https://search.usi.ch/en/courses/352653/",
    "https://search.usi.ch/en/courses/35265754/distributed-algorithms",
    ]

    dataqueue = Queue()

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(parse_url, urls))
        results = [x for x in results if x is not None]
        print(results)
