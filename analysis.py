"""
analysis.py
===========
E-Commerce Sales Analysis — Visualization & Dashboard Generator
Author  : Avinash Giri (@Avinashgiriofficial)
GitHub  : https://github.com/Avinashgiriofficial/ecommerce-sales-analysis
Email   : avinashgiri363@gmail.com

Description:
    Reads ecommerce_sales_data.csv and generates:
      - ecommerce_dashboard.png          (static 4-chart dashboard)
      - ecommerce_interactive_dashboard.html (interactive Plotly dashboard)

Usage:
    python analysis.py
    (Run scraper.py first to generate ecommerce_sales_data.csv)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
import seaborn as sns
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
import os
import sys

warnings.filterwarnings("ignore")

# ── Config ────────────────────────────────────────────────────────────────────

INPUT_FILE        = "ecommerce_sales_data.csv"
STATIC_OUTPUT     = "ecommerce_dashboard.png"
INTERACTIVE_OUTPUT= "ecommerce_interactive_dashboard.html"

PALETTE = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7", "#DDA0DD", "#98D8C8", "#F7DC6F"]


# ── Load Data ─────────────────────────────────────────────────────────────────

def load_data(filepath):
    if not os.path.exists(filepath):
        print(f"ERROR: '{filepath}' not found.")
        print("Please run scraper.py first to generate the dataset.")
        sys.exit(1)
    df = pd.read_csv(filepath)
    print(f"Loaded: {df.shape[0]} rows x {df.shape[1]} columns")
    print(f"Categories: {df['Category'].value_counts().to_dict()}\n")
    return df


# ── Static Dashboard ──────────────────────────────────────────────────────────

def plot_static_dashboard(df, output_path):
    """Generate a 4-chart dark-themed matplotlib dashboard."""
    cat_list  = df["Category"].value_counts().index.tolist()
    color_map = {c: PALETTE[i % len(PALETTE)] for i, c in enumerate(cat_list)}

    fig = plt.figure(figsize=(20, 14), facecolor="#0d1117")
    fig.suptitle(
        "E-Commerce Sales Report Dashboard  |  scrapingcourse.com",
        fontsize=20, fontweight="bold", color="white", y=1.01
    )
    gs = gridspec.GridSpec(2, 2, figure=fig, hspace=0.42, wspace=0.32)

    def style_ax(ax, title):
        ax.set_facecolor("#161b22")
        ax.set_title(title, fontsize=13, fontweight="bold", color="white", pad=10)
        ax.tick_params(colors="#aaa")
        ax.xaxis.label.set_color("#aaa")
        ax.yaxis.label.set_color("#aaa")
        for spine in ax.spines.values():
            spine.set_edgecolor("#30363d")

    # Chart 1 — Avg Price by Category
    ax1 = fig.add_subplot(gs[0, 0])
    style_ax(ax1, "Average Price by Category (INR)")
    cat_avg = df.groupby("Category")["Price_INR"].mean().reindex(cat_list)
    bars = ax1.bar(cat_avg.index, cat_avg.values,
                   color=[color_map[c] for c in cat_avg.index], edgecolor="#0d1117")
    ax1.set_ylabel("Avg Price (INR)", color="#aaa")
    for bar, val in zip(bars, cat_avg.values):
        ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() * 1.02,
                 f"Rs{val:,.0f}", ha="center", fontsize=8.5, color="white", fontweight="bold")
    ax1.tick_params(axis="x", rotation=20)

    # Chart 2 — Price Distribution
    ax2 = fig.add_subplot(gs[0, 1])
    style_ax(ax2, "Price Distribution by Category")
    for cat in cat_list:
        data = df[df["Category"] == cat]["Price_INR"]
        ax2.hist(data, bins=15, alpha=0.65, label=cat, color=color_map[cat])
    ax2.set_xlabel("Price (INR)", color="#aaa")
    ax2.set_ylabel("Number of Products", color="#aaa")
    ax2.legend(fontsize=8, facecolor="#161b22", labelcolor="white",
               edgecolor="#30363d", ncol=2)

    # Chart 3 — Ratings vs Reviews Bubble
    ax3 = fig.add_subplot(gs[1, 0])
    style_ax(ax3, "Avg Rating vs Total Reviews  (bubble = product count)")
    stats = df.groupby("Category").agg(
        Avg_Rating    =("Rating", "mean"),
        Total_Reviews =("Reviews", "sum"),
        Count         =("Product Name", "count")
    ).reset_index()
    for _, row in stats.iterrows():
        ax3.scatter(row["Avg_Rating"], row["Total_Reviews"],
                    s=row["Count"] * 35, color=color_map[row["Category"]],
                    alpha=0.85, edgecolors="white", linewidth=1)
        ax3.annotate(
            f"{row['Category']}\n({row['Count']} products)",
            (row["Avg_Rating"], row["Total_Reviews"]),
            xytext=(7, 4), textcoords="offset points",
            fontsize=8.5, color="white"
        )
    ax3.set_xlabel("Average Rating", color="#aaa")
    ax3.set_ylabel("Total Reviews", color="#aaa")

    # Chart 4 — Top 10 Products
    ax4 = fig.add_subplot(gs[1, 1])
    style_ax(ax4, "Top 10 Most Reviewed Products")
    top10 = df.nlargest(10, "Reviews").copy()
    top10["Label"] = top10["Product Name"].str[:35] + "..."
    hbars = ax4.barh(top10["Label"], top10["Reviews"],
                     color=[color_map[c] for c in top10["Category"]], edgecolor="#0d1117")
    ax4.invert_yaxis()
    ax4.set_xlabel("Review Count", color="#aaa")
    for bar, (_, row) in zip(hbars, top10.iterrows()):
        ax4.text(bar.get_width() * 1.01, bar.get_y() + bar.get_height() / 2,
                 f"Rs{row['Price_INR']:,.0f}  {row['Rating']:.1f}*",
                 va="center", fontsize=8, color="white")
    patches = [mpatches.Patch(color=color_map[c], label=c) for c in cat_list]
    ax4.legend(handles=patches, fontsize=7.5, facecolor="#161b22",
               labelcolor="white", edgecolor="#30363d", loc="lower right")

    plt.savefig(output_path, dpi=150, bbox_inches="tight", facecolor="#0d1117")
    plt.show()
    print(f"Static dashboard saved: {output_path}")


# ── Interactive Dashboard ─────────────────────────────────────────────────────

def plot_interactive_dashboard(df, output_path):
    """Generate an interactive Plotly dashboard."""
    cat_list  = df["Category"].value_counts().index.tolist()
    color_map = {c: PALETTE[i % len(PALETTE)] for i, c in enumerate(cat_list)}

    cat_summary = df.groupby("Category").agg(
        Avg_Price     =("Price_INR", "mean"),
        Product_Count =("Product Name", "count"),
        Avg_Rating    =("Rating", "mean"),
        Total_Reviews =("Reviews", "sum"),
    ).reset_index().round(2)

    top10 = df.nlargest(10, "Reviews").copy()
    top10["Label"] = top10["Product Name"].str[:30]

    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=[
            "Avg Price by Category (INR)",
            "Product Share by Category",
            "Avg Rating by Category",
            "Top 10 Products by Reviews"
        ],
        specs=[[{"type": "xy"}, {"type": "domain"}],
               [{"type": "xy"}, {"type": "xy"}]]
    )

    fig.add_trace(go.Bar(
        x=cat_summary["Category"], y=cat_summary["Avg_Price"],
        marker_color=PALETTE[:len(cat_summary)],
        text=cat_summary["Avg_Price"].apply(lambda x: f"Rs{x:,.0f}"),
        textposition="outside", name="Avg Price"
    ), row=1, col=1)

    fig.add_trace(go.Pie(
        labels=cat_summary["Category"],
        values=cat_summary["Product_Count"],
        hole=0.42, marker_colors=PALETTE[:len(cat_summary)],
        textinfo="label+percent"
    ), row=1, col=2)

    fig.add_trace(go.Bar(
        x=cat_summary["Category"], y=cat_summary["Avg_Rating"],
        marker_color=PALETTE[:len(cat_summary)],
        text=cat_summary["Avg_Rating"].apply(lambda x: f"{x:.2f} stars"),
        textposition="outside", name="Avg Rating"
    ), row=2, col=1)

    fig.add_trace(go.Bar(
        x=top10["Reviews"], y=top10["Label"],
        orientation="h",
        marker_color=[color_map.get(c, "#4ECDC4") for c in top10["Category"]],
        text=top10["Reviews"], textposition="outside", name="Reviews"
    ), row=2, col=2)

    fig.update_layout(
        height=820,
        title_text="E-Commerce Interactive Sales Dashboard",
        title_font_size=20,
        template="plotly_dark",
        showlegend=False,
        paper_bgcolor="#0d1117",
    )
    fig.update_yaxes(autorange="reversed", row=2, col=2)
    fig.write_html(output_path)
    fig.show()
    print(f"Interactive dashboard saved: {output_path}")


# ── Summary Report ────────────────────────────────────────────────────────────

def print_summary(df):
    print("=" * 62)
    print("         E-COMMERCE SALES REPORT  |  SUMMARY")
    print("=" * 62)
    print(f"  Source              : scrapingcourse.com/ecommerce")
    print(f"  Total Products      : {len(df):,}")
    print(f"  Categories          : {', '.join(df['Category'].unique())}")
    print(f"  Avg Price (INR)     : Rs{df['Price_INR'].mean():,.0f}")
    print(f"  Avg Rating          : {df['Rating'].mean():.2f} stars")
    print(f"  Total Reviews       : {df['Reviews'].sum():,}")
    print(f"  Most Reviewed Cat   : {df.groupby('Category')['Reviews'].sum().idxmax()}")
    print(f"  Highest Rated Cat   : {df.groupby('Category')['Rating'].mean().idxmax()}")
    print(f"  Most Products Cat   : {df['Category'].value_counts().idxmax()}")
    print("=" * 62)
    print("\nPer Category Breakdown:")
    summary = df.groupby("Category").agg(
        Products      =("Product Name", "count"),
        Avg_Price     =("Price_INR", "mean"),
        Avg_Rating    =("Rating", "mean"),
        Total_Reviews =("Reviews", "sum")
    ).round(2)
    summary["Avg_Price"] = summary["Avg_Price"].apply(lambda x: f"Rs{x:,.0f}")
    print(summary.to_string())


# ── Entry Point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  E-Commerce Sales — Analysis & Dashboard")
    print("  Author: Avinash Giri (@Avinashgiriofficial)")
    print("=" * 55 + "\n")

    df = load_data(INPUT_FILE)
    print_summary(df)
    plot_static_dashboard(df, STATIC_OUTPUT)
    plot_interactive_dashboard(df, INTERACTIVE_OUTPUT)

    print("\nAll outputs generated:")
    print(f"  -> {STATIC_OUTPUT}")
    print(f"  -> {INTERACTIVE_OUTPUT}")
