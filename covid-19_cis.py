import requests
import re


page_link = "https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic"


def wiki_parsing(main_str):
    get_request = requests.get(page_link)
    pattern_string = r"(?<="+ main_str + r"\").\b.{1,200}\b"
    cis_countries = re.search(pattern_string,str(get_request.content))
    temp_content = str(cis_countries.group(0))
    cis_digit = re.search(r"(?<=;\">).\d{1,10}",temp_content)

    return cis_digit.group(0)


if __name__ == '__main__':
    by = wiki_parsing("Belarus")
    ukr = wiki_parsing("Ukraine")
    ru = wiki_parsing("Russia")
    print(f"In Belarus right now infected {by} people")
    print(f"In Ukrain right now infected {ukr} people")
    print(f"In Russia right now infected {ru} people")
