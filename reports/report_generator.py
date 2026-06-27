# reports/report_generator.py

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
import pandas as pd
from datetime import datetime
from services.analytics_service import get_all_kpis
from config import EXPORT_DIR


def generate_report():
    """
    Saare KPIs nikalo aur 3 files save karo:
      exports/analytics_YYYY-MM-DD.json
      exports/categories_YYYY-MM-DD.csv
      exports/top_products_YYYY-MM-DD.csv
    """
    os.makedirs(EXPORT_DIR, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")

    print("\nReport generate ho raha hai...")
    data = get_all_kpis()

    # ── 1. JSON report ─────────────────────────────────────
    json_path = os.path.join(EXPORT_DIR, f"analytics_{date_str}.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"JSON  → {json_path}")

    # ── 2. Category CSV ────────────────────────────────────
    if data["category_stats"]:
        df = pd.DataFrame(data["category_stats"])
        cat_path = os.path.join(EXPORT_DIR, f"categories_{date_str}.csv")
        df.to_csv(cat_path, index=False)
        print(f"CSV   → {cat_path}")

    # ── 3. Top Products CSV ────────────────────────────────
    if data["top_rated"]:
        df2 = pd.DataFrame(data["top_rated"])
        top_path = os.path.join(EXPORT_DIR, f"top_products_{date_str}.csv")
        df2.to_csv(top_path, index=False)
        print(f"CSV   → {top_path}")

    # ── Console summary ────────────────────────────────────
    print("\n" + "="*52)
    print("ANALYTICS SUMMARY")
    print("="*52)
    print(f"  Total Products  : {data['total_products']}")
    print(f"  Total Users     : {data['total_users']}")
    print(f"  Total Orders    : {data['total_orders']}")
    print(f"  Total Revenue   : ${data['total_revenue']}")

    print(f"\n  Category Breakdown:")
    for c in data["category_stats"]:
        bar = "█" * min(c["total_products"], 20)
        print(f"    {c['category']:<25} {bar} {c['total_products']} products  Avg: ${c['avg_price']}")

    print(f"\n  Top 5 Rated Products:")
    for i, p in enumerate(data["top_rated"][:5], 1):
        stars = "★" * int(p["rating"]) + "☆" * (5 - int(p["rating"]))
        print(f"    {i}. {stars}  {p['title'][:35]:<35}  ${p['price']}")

    print(f"\n  Price Distribution:")
    for r in data["price_ranges"]:
        bar = "▓" * min(r["count"], 30)
        print(f"    {r['range']:<15} {bar} {r['count']}")

    print(f"\n  Data Sources:")
    for s in data["source_stats"]:
        print(f"    {s['source']:<20} {s['count']} products")

    print("="*52 + "\n")
    return data
