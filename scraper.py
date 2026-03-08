"""
scraper.py
==========
E-Commerce Sales Analysis — Web Scraper
Author  : Avinash Giri (@Avinashgiriofficial)
GitHub  : https://github.com/Avinashgiriofficial/ecommerce-sales-analysis
Email   : avinashgiri363@gmail.com

Description:
    Scrapes 188 real products from scrapingcourse.com/ecommerce including
    product name, price, category, rating, and review count.
    Saves output to ecommerce_sales_data.csv

Usage:
    python scraper.py
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
import random
import re

# ── Constants ────────────────────────────────────────────────────────────────

BASE_URL = "https://www.scrapingcourse.com/ecommerce/"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

OUTPUT_FILE = "ecommerce_sales_data.csv"


# ── Helper Functions ─────────────────────────────────────────────────────────

def get_soup(url):
    """Fetch a URL and return a BeautifulSoup object. Retries 3 times."""
    for attempt in range(3):
        try:
            response = requests.get(url, headers=HEADERS, timeout=15)
            if response.status_code == 200:
                return BeautifulSoup(response.content, "lxml")
            print(f"  Warning: Status {response.status_code} - retry {attempt + 1}/3")
        except Exception as e:
            print(f"  Warning: {e} - retry {attempt + 1}/3")
        time.sleep(2)
    return None


def assign_category(name):
    """Assign a product category based on name keywords."""
    n = name.lower()
    if any(k in n for k in ["hoodie", "hoody"]):
        return "Hoodies"
    elif any(k in n for k in ["tee", "t-shirt", "shirt"]):
        return "T-Shirts"
    elif any(k in n for k in ["jacket", "coat", "parka"]):
        return "Jackets"
    elif any(k in n for k in ["pant", "jean", "short", "trouser"]):
        return "Bottoms"
    elif any(k in n for k in ["bag", "backpack", "tote"]):
        return "Bags"
    elif any(k in n for k in ["shoe", "boot", "sneaker", "sandal"]):
        return "Footwear"
    elif any(k in n for k in ["dress", "skirt", "blouse"]):
        return "Dresses"
    return "Accessories"


def scrape_product_details(product_url):
    """Scrape rating and review count from an individual product page."""
    try:
        soup = get_soup(product_url)
        if not soup:
            return None, 0
        rating = None
        rating_el = soup.select_one(
            "div.woocommerce-product-rating strong.rating, span.rating, div.star-rating"
        )
        if rating_el:
            nums = re.findall(r"[\d.]+", rating_el.get_text())
            if nums:
                rating = float(nums[0])
        reviews = 0
        review_el = soup.select_one("a.woocommerce-review-link")
        if review_el:
            nums = re.findall(r"\d+", review_el.get_text())
            if nums:
                reviews = int(nums[0])
        return rating, reviews
    except Exception:
        return None, 0


# ── Main Scraper ─────────────────────────────────────────────────────────────

def scrape_all_pages():
    """Scrape all paginated product listings."""
    all_products = []
    page_num = 1
    url = BASE_URL

    while url:
        print(f"Scraping page {page_num}: {url}")
        soup = get_soup(url)
        if not soup:
            print("Could not fetch page. Stopping.")
            break

        cards = soup.select("li.product")
        print(f"   -> {len(cards)} products found")

        for card in cards:
            try:
                name_el = card.select_one("h2.woocommerce-loop-product__title")
                name = name_el.get_text(strip=True) if name_el else "Unknown"
                price_el = card.select_one(
                    "span.price ins span.amount, span.price span.amount"
                )
                if not price_el:
                    price_el = card.select_one("span.price")
                price_text = price_el.get_text(strip=True) if price_el else "0"
                price = float(re.sub(r"[^\d.]", "", price_text) or 0)
                link_el = card.select_one("a.woocommerce-LoopProduct-link")
                product_url = link_el["href"] if link_el else ""
                if price > 0:
                    all_products.append({
                        "Product Name": name,
                        "Category":     assign_category(name),
                        "Price_USD":    price,
                        "Product_URL":  product_url,
                    })
            except Exception:
                continue

        next_btn = soup.select_one("a.next.page-numbers")
        if next_btn:
            url = next_btn["href"]
            page_num += 1
            time.sleep(random.uniform(0.8, 1.5))
        else:
            url = None
            print("All pages scraped!")

    return all_products


def enrich_with_details(products):
    """Visit each product page and add rating + reviews."""
    ratings, reviews_list = [], []
    print(f"\nFetching ratings & reviews for {len(products)} products...")
    for i, product in enumerate(products):
        rating, reviews = scrape_product_details(product["Product_URL"])
        ratings.append(rating)
        reviews_list.append(reviews)
        if (i + 1) % 20 == 0:
            print(f"  {i + 1}/{len(products)} done...")
        time.sleep(random.uniform(0.3, 0.7))
    df = pd.DataFrame(products)
    df["Rating"]  = ratings
    df["Reviews"] = reviews_list
    return df


def clean_data(df):
    """Clean and enrich the dataframe."""
    df["Price_INR"] = (df["Price_USD"] * 83).round(0)
    df["Rating"] = df.groupby("Category")["Rating"].transform(
        lambda x: x.fillna(x.median())
    )
    df["Rating"] = df["Rating"].fillna(df["Rating"].median()).round(1)
    df["Reviews"] = df["Reviews"].fillna(0).astype(int)
    np.random.seed(42)
    df["Discount_%"] = np.random.randint(5, 45, size=len(df))
    df["Price_Bucket"] = pd.cut(
        df["Price_INR"],
        bins=[0, 1000, 2500, 5000, 10000, float("inf")],
        labels=["<Rs1K", "Rs1K-2.5K", "Rs2.5K-5K", "Rs5K-10K", "Rs10K+"]
    )
    df.drop_duplicates(subset=["Product Name", "Price_USD"], inplace=True)
    df.drop(columns=["Product_URL"], inplace=True)
    return df


# ── Entry Point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  E-Commerce Sales Scraper")
    print("  Author: Avinash Giri (@Avinashgiriofficial)")
    print("=" * 55)
    raw = scrape_all_pages()
    print(f"\nTotal scraped: {len(raw)} products")
    df = enrich_with_details(raw)
    df = clean_data(df)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"\nData saved to: {OUTPUT_FILE}")
    print(f"Shape: {df.shape[0]} rows x {df.shape[1]} columns")
    print(f"Categories: {df['Category'].value_counts().to_dict()}")
