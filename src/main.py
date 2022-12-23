from urllib.parse import urlparse

from parsers.CourseParserUSI import CourseParserUSI

parse_switch = {
    "search.usi.ch": CourseParserUSI
}

def parse_url(url:str) -> None:
    domain = urlparse(url).netloc
    parser = parse_switch[domain](url)
    return parser.parse_stats()

if __name__ == "__main__":
    url = "https://search.usi.ch/en/courses/35265726/advanced-java-programming"
    data = parse_url(url)
    print(data)
