# E-Commerce Sales Analysis

A complete end-to-end Data Science project — **Real Web Scraping → Data Cleaning → Visual Sales Dashboard** built entirely in Python.

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat&logo=python)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-Scraping-green?style=flat)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat&logo=pandas)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?style=flat&logo=plotly)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=flat&logo=jupyter)

---

## Project Overview

This project scrapes **188 real products** from an e-commerce platform, cleans the data, and generates a complete **sales performance dashboard** with 4 key visualizations.

| Field | Details |
|---|---|
| **Data Source** | scrapingcourse.com/ecommerce (188 products) |
| **Categories** | Hoodies, T-Shirts, Jackets, Bottoms, Bags, Footwear, Accessories |
| **Tech Stack** | Python, BeautifulSoup, Pandas, Matplotlib, Seaborn, Plotly |
| **Output** | CSV Dataset + Static PNG Dashboard + Interactive HTML Dashboard |

---

## Key Questions Answered

- Which product categories have the **highest average prices**?
- How are **prices distributed** across different categories?
- Which categories get the **most customer reviews**?
- What are the **top 10 most reviewed products**?

---

## Project Structure

```
ecommerce-sales-analysis/
│
├── ecommerce_sales_dashboard_v3.ipynb   <- Main notebook (scraper + analysis + charts)
├── scraper.py                           <- Standalone scraper script
├── analysis.py                          <- Standalone analysis + visualization script
├── config.py                            <- All project settings in one place
├── ecommerce_sales_data.csv             <- Scraped & cleaned dataset
├── requirements.txt                     <- Python dependencies
├── .gitignore
├── LICENSE
├── visuals/                             <- All chart images live here
│   ├── dashboard_preview.png
│   ├── chart1_avg_price.png
│   ├── chart2_price_dist.png
│   ├── chart3_ratings_bubble.png
│   └── chart4_top10_products.png
└── README.md
```

---

## Dashboard Preview

![Full Dashboard](visuals/dashboard_preview.png)

---

## Visualizations

### Chart 1 — Average Price by Category
![Avg Price](visuals/chart1_avg_price.png)

### Chart 2 — Price Distribution
![Price Distribution](visuals/chart2_price_dist.png)

### Chart 3 — Ratings vs Reviews
![Ratings Bubble](visuals/chart3_ratings_bubble.png)

### Chart 4 — Top 10 Most Reviewed Products
![Top 10 Products](visuals/chart4_top10_products.png)

---

## How to Run

**1. Clone the repository**
```bash
git clone https://github.com/Avinashgiriofficial/ecommerce-sales-analysis.git
cd ecommerce-sales-analysis
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3a. Run via Jupyter Notebook** (recommended)
```bash
jupyter notebook ecommerce_sales_dashboard_v3.ipynb
```

**3b. Run via Python scripts**
```bash
python scraper.py    # Step 1 — scrape and save CSV
python analysis.py   # Step 2 — generate all dashboards
```

---

## Output Files

| File | Description |
|---|---|
| `ecommerce_sales_data.csv` | Clean dataset with all 188 products |
| `visuals/dashboard_preview.png` | Dark-themed 4-chart static dashboard |
| `ecommerce_interactive_dashboard.html` | Open in browser — hover, zoom, filter |

---

## Tech Stack

| Library | Purpose |
|---|---|
| `requests` + `beautifulsoup4` | Web scraping |
| `pandas` + `numpy` | Data cleaning & analysis |
| `matplotlib` + `seaborn` | Static visualizations |
| `plotly` | Interactive dashboard |

---

## Author

**Avinash Giri**
GitHub: [@Avinashgiriofficial](https://github.com/Avinashgiriofficial)
Email: avinashgiri363@gmail.com

---

## License

This project is open source under the [MIT License](LICENSE).
