import os
import json
import requests
from bs4 import BeautifulSoup

@@ -28,18 +30,32 @@ def get_cos(ancestor, selector=None, attribute=None, return_list=False):
    "cons": ("div.review-feature__title--negatives ~ div.review-feature__item", None, True)
}

# product_code = input("Podaj kod produktu: ")
product_code = input("Podaj kod produktu: ")
# product_code = "58835954"
product_code = "39562616"
# product_code = "39562616"
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
respons = requests.get(url)
if  respons.status_code == requests.codes.ok:
    page_dom = BeautifulSoup(respons.text, 'html.parser')
    opinions = page_dom.select("div.js_product-review")
    opinions_all = []
    for opinion in opinions:
        single_opinion = {}
        for key, value in selectors.items():
            single_opinion[key] = get_cos(opinion, *value)
        opinions_all.append(single_opinion)
    print(opinions_all)
opinions_all = []
while(url):
    print(url)
    respons = requests.get(url)
    if  respons.status_code == requests.codes.ok:
        page_dom = BeautifulSoup(respons.text, 'html.parser')
        opinions = page_dom.select("div.js_product-review")
        for opinion in opinions:
            single_opinion = {}
            for key, value in selectors.items():
                single_opinion[key] = get_cos(opinion, *value)
            opinions_all.append(single_opinion)
    try:
        url = "https://www.ceneo.pl"+get_cos(page_dom,"a.pagination__next","href")
    except TypeError:
        url = None
try:
    os.mkdir("opinions")
except FileExistsError:
    pass
# jf = open(f"opinions/{product_code}.json", "w", encoding="UTF-8")
# json.dump(opinions_all, jf, indent=4, ensure_ascii=False)
# jf.close()
with open(f"opinions/{product_code}.json", "w", encoding="UTF-8") as jf:
    json.dump(opinions_all, jf, indent=4, ensure_ascii=False)