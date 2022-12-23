from main import *
import warnings

warnings.filterwarnings("ignore")

assert type(get_parser("https://search.usi.ch/en/courses/35265726")) == CourseParserUSI
assert get_parser("https://usi.ch/en/courses/35265726") == None