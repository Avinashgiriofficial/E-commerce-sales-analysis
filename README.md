# 🛒 E-Commerce Sales Analysis

> A complete end-to-end data science project — scrape real product data, clean it, analyze it, and generate a full visual sales dashboard entirely in Python.

---

## 📌 Project Overview

| Field | Details |
|---|---|
| **Platform Scraped** | scrapingcourse.com/ecommerce (188 real products) |
| **Language** | Python 3.10+ |
| **Tools** | Jupyter Notebook · BeautifulSoup · Pandas · Matplotlib · Seaborn · Plotly |
| **Output** | CSV dataset · Static PNG dashboard · Interactive HTML dashboard |
| **Author** | [Avinash Giri](https://github.com/Avinashgiriofficial) |

---

## 🎯 Objective

Analyze product categories in an e-commerce store to identify:
- Which categories have the **highest average prices**
- How **prices are distributed** across categories
- Which products have the **best ratings and most reviews**
- The **top 10 most popular products** overall

---

## 📂 Project Structure

```
ecommerce-sales-analysis/
│
├── 📓 ecommerce_sales_dashboard_v3.ipynb   ← Main notebook (all-in-one)
├── 🐍 scraper.py                           ← Standalone scraper script
├── 🐍 visualize.py                         ← Standalone dashboard generator
├── 🐍 config.py                            ← All settings & constants
│
├── 📊 ecommerce_sales_data.csv             ← Scraped & cleaned dataset
├── 🖼️  ecommerce_dashboard.png             ← Static 4-chart dashboard
├── 🌐 ecommerce_interactive_dashboard.html ← Interactive Plotly dashboard
│
├── 📄 requirements.txt
├── 🚫 .gitignore
├── 📜 LICENSE
└── 📖 README.md
```

---

## 📊 Dashboard Preview

![E-Commerce Sales Dashboard](ecommerce_dashboard.png)

---

## 🔍 Key Analyses

| Chart | Description |
|---|---|
| 💰 **Avg Price by Category** | Bar chart comparing pricing across all categories |
| 📈 **Price Distribution** | Histogram showing how product prices are spread |
| ⭐ **Ratings vs Reviews** | Bubble chart — category quality vs popularity |
| 🏆 **Top 10 Products** | Most reviewed products with price & rating labels |

---

## 🛠️ Tech Stack

| Library | Purpose |
|---|---|
| `requests` + `BeautifulSoup` | Web scraping |
| `pandas` + `numpy` | Data cleaning & analysis |
| `matplotlib` + `seaborn` | Static visualizations |
| `plotly` | Interactive HTML dashboard |

---

## ▶️ How to Run

### Option A — Jupyter Notebook (Recommended)

```bash
git clone https://github.com/Avinashgiriofficial/ecommerce-sales-analysis.git
cd ecommerce-sales-analysis
pip install -r requirements.txt
jupyter notebook ecommerce_sales_dashboard_v3.ipynb
```
Run all cells top to bottom. Detail page scraping takes ~3 minutes — normal!

### Option B — Python Scripts

```bash
python scraper.py     # scrape & save CSV
python visualize.py   # generate dashboards
```

---

## 📈 Sample Results

```
Total Products   : 188
Categories       : Hoodies, T-Shirts, Jackets, Bottoms, Bags, Accessories
Avg Price (INR)  : ₹3,241
Avg Rating       : 4.2 ⭐
Most Reviewed    : Hoodies
Highest Rated    : Jackets
```

---

## 👤 Author

**Avinash Giri**
- GitHub : [@Avinashgiriofficial](https://github.com/Avinashgiriofficial)
- Email  : avinashgiri363@gmail.com

---

## 📄 License

This project is open source under the [MIT License](LICENSE).
