import requests
from bs4 import BeautifulSoup

product_code = input("Podaj kod produktu: ")
def get_cos(ancestor, selector=None, attribute=None, return_list=False):
    try:
        if return_list:
            return [tag.get_text().strip() for tag in ancestor.select(selector)]
        if not selector and attribute:
            return ancestor[attribute].strip()
        if attribute:
            return ancestor.select_one(selector)[attribute].strip()
        return ancestor.select_one(selector).get_text().strip()
    except (AttributeError, TypeError):
        return None

selectors = {
    "opinion_id": (None, "data-entry-id"),
    "author": ("span.user-post__author-name",),
    "recommendation": ("span.user-post__author-recomendation > em",),
    "stars": ("span.user-post__score-count",),
    "purchased": ("div.review-pz",),
    "opinion_date": ("span.user-post__published > time:nth-child(1)","datetime"),
    "purchase_date": ("span.user-post__published > time:nth-child(2)","datetime"),
    "usefull_count": ("button.vote-yes","data-total-vote"),
    "unusefull_count": ("button.vote-no","data-total-vote"),
    "content": ("div.user-post__text",),
    "pros": ("div.review-feature__title--positives ~ div.review-feature__item", None, True),
    "cons": ("div.review-feature__title--negatives ~ div.review-feature__item", None, True)
}

# product_code = input("Podaj kod produktu: ")
# product_code = "58835954"
product_code = "39562616"
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
respons = requests.get(url)
if  respons.status_code == requests.codes.ok:
    page_dom = BeautifulSoup(respons.text, 'html.parser')
    opinions = page_dom.select("div.js_product-review")
    opinions_all = []
    for opinion in opinions:
        single_opinion = {
            "opinion_id": opinion["data-entry-id"],
            "author": opinion.select_one("span.user-post__author-name").get_text().strip(),
            "recommendation": opinion.select_one("span.user-post__author-recomendation > em").get_text().strip(),
            "stars": opinion.select_one("span.user-post__score-count").get_text().strip(),
            "purchased": opinion.select_one("div.review-pz").get_text().strip(),
            "opinion_date": opinion.select_one("span.user-post__published > time:nth-child(1)")["datetime"].strip(),
            "purchase_date": opinion.select_one("span.user-post__published > time:nth-child(2)")["datetime"].strip(),
            "usefull_count": opinion.select_one("button.vote-yes")["data-total-vote"].strip(),
            "unusefull_count": opinion.select_one("button.vote-no")["data-total-vote"].strip(),
            "content": opinion.select_one("div.user-post__text").get_text().strip(),
            "pros": [p.get_text().strip for p in opinion.select("div.review-feature__title--positives ~ div.review-feature__item")],
            "cons": [c.get_text().strip for c in opinion.select("div.review-feature__title--negatives ~ div.review-feature__item")]
        }
        single_opinion = {}
        for key, value in selectors.items():
            single_opinion[key] = get_cos(opinion, *value)
        opinions_all.append(single_opinion)
    print(opinions_all)