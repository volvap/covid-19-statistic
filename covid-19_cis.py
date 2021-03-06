import threading
import requests
import re


page_link = "https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic"
countries = ['Belarus','Ukraine','Russia','Poland','Lithuania']

def wiki_parsing(main_str,get_request):
    pattern_string = r"(?<="+ main_str + r"\").\b.{1,200}\b"
    cis_countries = re.search(pattern_string,str(get_request.content))
    temp_content = str(cis_countries.group(0))
    cis_digit = re.search(r"(?<=n<td>).(?:\d{0,10},\d{1,10}|\d{1,10})",temp_content)
    print(f"In {main_str} right now infected {cis_digit.group(0)} people")

if __name__ == '__main__':
    get_request = requests.get(page_link)
    for i in countries:
        x = threading.Thread(target=wiki_parsing,args=(i,get_request))
        x.start()
