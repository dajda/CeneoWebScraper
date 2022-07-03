from app import app
from flask import render_template, redirect, url_for, request
import json
import os
from app.models.product import Product
import markdown


@app.route('/')
def index():
    readme = ''

    with open('README.md', 'r') as rf:
        readme = markdown.markdown(rf.read(), extensions=['markdown.extensions.tables'])

    return render_template('index.html.jinja', readme=readme)


@app.route('/extract', methods=["POST", "GET"])
def extract():
    if request.method == "POST":
        product_id = request.form.get("product_id")
        product = Product(product_id)
        product.extract_name()
        if product.product_name:
            product.extract_opinions().calculate_stats().draw_charts()
            product.export_opinions()
            product.export_product()
        else:
            error = "Nie działa"
            return render_template("extract.html.jinja", error=error)

        return redirect(url_for('product', product_id=product_id))
    else:
        return render_template("extract.html.jinja")


@app.route('/products')
def products():
    products = [filename.split(".")[0]
                for filename in os.listdir("app/opinions")]
    return render_template("products.html.jinja", products=products)


@app.route('/author')
def author():
    return render_template("author.html.jinja")


@app.route('/product/<product_id>')
def product(product_id):
    product = Product(product_id)
    product.import_product()
    stats = product.stats_to_dict()
    opinions = product.opinions_to_df()
    return render_template("product.html.jinja", product_id=product_id, stats=stats, opinions=opinions)
    
