"""
config.py
=========
Central configuration file for the E-Commerce Sales Analysis project.
Author : Avinash Giri (@Avinashgiriofficial)

Edit values here to customize scraping behavior, output paths, or styling.
"""

# ── Scraper Settings ──────────────────────────────────────────────────────────

BASE_URL     = "https://www.scrapingcourse.com/ecommerce/"
PAGES_LIMIT  = None        # Set to an integer (e.g. 5) to limit pages scraped
REQUEST_DELAY = (0.8, 1.5) # Random delay range between requests (seconds)
TIMEOUT       = 15         # HTTP request timeout in seconds
MAX_RETRIES   = 3          # Number of retries on failed requests

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

# ── File Paths ────────────────────────────────────────────────────────────────

DATA_FILE            = "ecommerce_sales_data.csv"
STATIC_DASHBOARD     = "ecommerce_dashboard.png"
INTERACTIVE_DASHBOARD= "ecommerce_interactive_dashboard.html"

# ── Currency Conversion ───────────────────────────────────────────────────────

USD_TO_INR = 83   # Update this value for current exchange rate

# ── Category Keywords ─────────────────────────────────────────────────────────

CATEGORY_KEYWORDS = {
    "Hoodies":     ["hoodie", "hoody"],
    "T-Shirts":    ["tee", "t-shirt", "shirt"],
    "Jackets":     ["jacket", "coat", "parka"],
    "Bottoms":     ["pant", "jean", "short", "trouser"],
    "Bags":        ["bag", "backpack", "tote"],
    "Footwear":    ["shoe", "boot", "sneaker", "sandal"],
    "Dresses":     ["dress", "skirt", "blouse"],
    "Accessories": [],  # Default / fallback category
}

# ── Price Buckets ─────────────────────────────────────────────────────────────

PRICE_BINS   = [0, 1000, 2500, 5000, 10000, float("inf")]
PRICE_LABELS = ["<Rs1K", "Rs1K-2.5K", "Rs2.5K-5K", "Rs5K-10K", "Rs10K+"]

# ── Dashboard Styling ─────────────────────────────────────────────────────────

COLOR_PALETTE = [
    "#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4",
    "#FFEAA7", "#DDA0DD", "#98D8C8", "#F7DC6F"
]
BACKGROUND_COLOR = "#0d1117"
CARD_COLOR       = "#161b22"
CHART_DPI        = 150
CHART_FIGSIZE    = (20, 14)
