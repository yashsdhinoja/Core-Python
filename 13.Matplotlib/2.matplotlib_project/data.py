"""Synthetic e-commerce sales data.

In a real project this module would load a CSV / database table instead.
Everything else (dashboard.py) only needs a DataFrame with the columns below,
so you can swap in real data without touching the plotting code.
"""
import numpy as np
import pandas as pd

CATEGORY_BASE_PRICE = {
    "Electronics": 220.0,
    "Fashion": 45.0,
    "Home": 70.0,
    "Sports": 55.0,
    "Grocery": 12.0,
}
REGIONS = ["North", "South", "East", "West"]
WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def generate_sales_data(n_orders: int = 6000, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)

    # --- when orders happen: yearly seasonality + festive spike (Nov/Dec) ---
    day_of_year = np.arange(365)
    day_weights = 1 + 0.35 * np.sin(2 * np.pi * (day_of_year - 90) / 365)
    day_weights = day_weights + 0.9 * (day_of_year >= 305)
    day_weights = day_weights / day_weights.sum()
    days = rng.choice(day_of_year, n_orders, p=day_weights)

    # --- time of day: small lunch peak, big evening peak ---
    h = np.arange(24)
    hour_weights = 0.15 + np.exp(-((h - 13) ** 2) / 18) + 1.4 * np.exp(-((h - 20) ** 2) / 8)
    hour_weights = hour_weights / hour_weights.sum()
    hours = rng.choice(h, n_orders, p=hour_weights)

    order_date = pd.Timestamp("2025-01-01") + pd.to_timedelta(days, unit="D")

    # --- what was bought ---
    categories = rng.choice(
        list(CATEGORY_BASE_PRICE), n_orders, p=[0.18, 0.27, 0.2, 0.15, 0.2]
    )
    base = np.array([CATEGORY_BASE_PRICE[c] for c in categories])
    unit_price = base * rng.lognormal(mean=0.0, sigma=0.25, size=n_orders)
    quantity = 1 + rng.poisson(1.1, n_orders)
    discount = rng.choice([0.0, 0.05, 0.10, 0.20, 0.30], n_orders, p=[0.4, 0.2, 0.2, 0.12, 0.08])

    df = pd.DataFrame(
        {
            "order_date": order_date,
            "hour": hours,
            "category": categories,
            "region": rng.choice(REGIONS, n_orders, p=[0.3, 0.22, 0.25, 0.23]),
            "unit_price": unit_price.round(2),
            "quantity": quantity,
            "discount": discount,
        }
    )
    df["revenue"] = (df["unit_price"] * df["quantity"] * (1 - df["discount"])).round(2)
    df["weekday"] = df["order_date"].dt.dayofweek.map(dict(enumerate(WEEKDAYS)))
    df["month"] = df["order_date"].dt.to_period("M").dt.to_timestamp()
    return df.sort_values("order_date").reset_index(drop=True)
