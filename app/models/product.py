import os
from turtle import pd
from typing_extensions import Self
import requests
from bs4 import
from app.models.opinion import Opinion
from app.utils import get_item
import json
import pandas as pd
from matplotlib import pyplot as plt


class Product:
    def __init__(self, product_id=0, opinions=[], product_name="", opinions_count=0, pros_count=0, cons_count=0, average_score=0):
    pros 
        self.product_id = product_id
        self.product_name = product_name
        self.opinions = opinions
        self.opinions_count = opinions_count
        self.pros_count = pros_count
        self.cons_count = cons_count
        self.average_score = average_score
        return self

def extract_name(self):
    url = f"https://www.ceneo.pl/{self.product_id}#tab=reviews"
    self.product_name = get_item(,"h1.product-top__product-info__name")
    response = requests.get(url)
        page = BeautifulSoup(response.text, 'html.parser')
        self.product_name = get_item(page, "h1.product-top__product-info__name")
    return self
    product

def calculate_status(self):

    opinions = pd.read_json(json_dumps([opinion.to_dict()]))
    opinions["stars"] = opinions["stars"].map(lambda x: float(x.split("/")[0].replace(",", ".")))
    
        self.opinions_count: len(opinions)
        self.pros_count: opinions["pros"].map(bool).sum()
        self.cons_count: opinions["cons"].map(bool).sum()
        self.average_score: opinions["stars"].mean().round(2)
    
        return Self
    if not os.path.exists("app/plots"):
           os.makedirs("app/plots")
    recommendation = opinions["recommendation"].value_counts(dropna=False).sort_index().reindex(["Nie polecam", "Polecam", None], fill_value=0)
    recommendation.plot.pie(
        label="",
        autopct = lambda p: '{:.1f}%'.format(round(p)) if p > 0 else '',
        colors = ["crimson", "forestgreen", "lightskyblue"],
        labels = ["Nie polecam", "Polecam", "Nie mam zdania"]
    )
    plt.title("Rekomendacje")
    plt.savefig(f"app/plots/{product_id}_recommendations.png")
    plt.close()
    stars = opinions["stars"].value_counts().sort_index().reindex(list(np.arange(0,5.5,0.5)), fill_value=0)
    stars.plot.bar(
        color = "pink"
    )
    plt.title("Oceny produktu")
    plt.xlabel("Liczba gwiazdek")
    plt.ylabel("Liczba opinii")
    plt.grid(True, axis="y")
    plt.xticks(rotation=0)
    plt.savefig(f"app/plots/{product_id}_stars.png")
    plt.close()
    return render_template("product.html.jinja", product_id=product_id, stats=stats, opinions=opinions)

    def __str__(self)__ -> str:
        pass

    def __repr__(self) -> str:
        pass
    def to_dict(self)

    def export_opnions():
        pass

    def export_product():
        pass