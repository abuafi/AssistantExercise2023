from urllib.parse import urlparse
from typing import Optional
from threading import Thread
from queue import Queue
from warnings import warn
import sys

from concurrent.futures import ThreadPoolExecutor

from parsers.CourseParser import CourseParser
from parsers.CourseParserUSI import CourseParserUSI

parse_switch = {
    "search.usi.ch": CourseParserUSI
}

def get_parser(url:str) -> Optional[CourseParser]:
    """
    Computes the class of the parser for the given url, or None if an error occours.

    Parameters:
        url (str): url to create the parser from

    Returns:
        CourseParser: An object of type CourseParser, if the url is valid
        None: If the url is invalid or the domain is not supported
    """
    domain = urlparse(url).netloc
    if domain == "":
        warn(f"Invalid url: '{url}'")
        return
    try:
        parser = parse_switch[domain]
        return parser
    except KeyError:
        warn(f"Domain name '{domain}' not supported")
        return

def parse_url(parser:CourseParser) -> dict:
    """
    Calls the parse_stats method of the given parser.

    Parameters:
        parser (CourseParser): Parser object

    Returns:
        ictionary containing the parsed statistics
    """
    return parser.parse_stats()

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        raise ValueError("Usage: python3 input.txt [#threads]")

    inputfile = sys.argv[1]
    nthreads = int(sys.argv[2]) if len(sys.argv) > 2 else None
    with open(inputfile) as input:
        urls = input.readlines()

        with ThreadPoolExecutor(nthreads) if nthreads is not None else ThreadPoolExecutor() as executor:
            parsers = [get_parser(url) for url in urls]
            parsers = [x for x in parsers if x is not None]
            results = list(executor.map(parse_url, parsers))
            results = [x for x in results if x is not None]
            print(results)
