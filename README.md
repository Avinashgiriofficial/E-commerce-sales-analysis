# E-Commerce Sales Analysis

A complete end-to-end Data Science project — Real Web Scraping, Data Cleaning, and Visual Sales Dashboard built entirely in Python.

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat&logo=python)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-Scraping-green?style=flat)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat&logo=pandas)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?style=flat&logo=plotly)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=flat&logo=jupyter)

---

## Project Overview

This project scrapes 188 real products from an e-commerce platform, cleans the data, and generates a complete sales performance dashboard with 4 key visualizations.

| Field | Details |
|---|---|
| **Data Source** | scrapingcourse.com/ecommerce — 188 real products |
| **Categories** | Hoodies, T-Shirts, Jackets, Bottoms, Bags, Footwear, Accessories |
| **Tech Stack** | Python, BeautifulSoup, Pandas, Matplotlib, Seaborn, Plotly |
| **Output** | CSV Dataset + Static PNG Dashboard + Interactive HTML Dashboard |

---

## Key Questions Answered

- Which product categories have the highest average prices?
- How are prices distributed across different categories?
- Which categories get the most customer reviews?
- What are the top 10 most reviewed products?

---

## Project Structure

```
ecommerce-sales-analysis/
│
├── ecommerce_sales_dashboard_v3.ipynb   <- Main notebook (scraper + analysis + charts)
├── scraper.py                           <- Standalone web scraper
├── analysis.py                          <- Standalone dashboard generator
├── config.py                            <- All project settings in one place
├── ecommerce_sales_data.csv             <- Scraped & cleaned dataset (generated)
├── ecommerce_interactive_dashboard.html <- Interactive Plotly dashboard (generated)
├── requirements.txt                     <- Python dependencies
├── .gitignore
├── LICENSE
│
└── visualization/                       <- All chart images stored here
    ├── README.md                        <- Details about each chart
    ├── dashboard_preview.png
    ├── chart1_avg_price.png
    ├── chart2_price_dist.png
    ├── chart3_ratings_bubble.png
    └── chart4_top10_products.png
```

> All images inside the `visualization/` folder are auto-generated when you run `analysis.py` or the Jupyter notebook.

---

## Visualizations

All charts are saved inside the [`visualization/`](visualization/) folder. Here is a summary of what each one shows:

| Chart | File | Description |
|---|---|---|
| Bar Chart | `chart1_avg_price.png` | Average selling price per category |
| Histogram | `chart2_price_dist.png` | How product prices are spread within each category |
| Bubble Chart | `chart3_ratings_bubble.png` | Category rating vs total review count |
| Horizontal Bar | `chart4_top10_products.png` | Top 10 most reviewed products with price and rating |
| Full Dashboard | `dashboard_preview.png` | All 4 charts combined in one layout |

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

Run all cells top to bottom. Scraping takes around 3 minutes for 188 products.

**3b. Run via Python scripts**
```bash
python scraper.py     # Scrape data and save to CSV
python analysis.py    # Generate all charts and dashboards
```

---

## Output Files

| File | Description |
|---|---|
| `ecommerce_sales_data.csv` | Clean dataset ready for analysis |
| `visualization/dashboard_preview.png` | Static 4-chart dashboard |
| `ecommerce_interactive_dashboard.html` | Open in browser for interactive charts |

---

## Tech Stack

| Library | Purpose |
|---|---|
| `requests` + `beautifulsoup4` | Web scraping |
| `pandas` + `numpy` | Data cleaning and analysis |
| `matplotlib` + `seaborn` | Static chart generation |
| `plotly` | Interactive HTML dashboard |

---

## Author

**Avinash Giri**
GitHub: [@Avinashgiriofficial](https://github.com/Avinashgiriofficial)
Email: avinashgiri363@gmail.com

---

## License

This project is open source under the [MIT License](LICENSE).
