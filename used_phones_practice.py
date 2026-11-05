"""Practice grouping, sampling, and plotting with the used-device dataset."""

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

PRICE = "normalized_used_price"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", nargs="?", type=Path,
                        default=Path("used_device_data.csv"))
    args = parser.parse_args()

    data = pd.read_csv(args.csv_path)
    missing_columns = {"5g", PRICE} - set(data.columns)
    if missing_columns:
        parser.error(f"Missing CSV columns: {', '.join(sorted(missing_columns))}")

    # Inspect the original labels before deciding how to encode 5G.
    print("Recorded 5G labels")
    print(data["5g"].value_counts(dropna=False).to_string())

    prices = data[PRICE].dropna()
    if prices.empty:
        parser.error("The CSV has no recorded normalized used prices.")

    # Show group sizes alongside medians to give each comparison context.
    summary = data.groupby("5g", dropna=False)[PRICE].agg(["count", "median"])
    print("\nNormalized used price by 5G label")
    print(summary.round(3).to_string())

    # Compare a reproducible sample mean with the full-data mean.
    sample = prices.sample(n=min(500, len(prices)), random_state=42)
    print(f"\nMean for all {len(prices):,} recorded prices: {prices.mean():.3f}")
    print(f"Mean for {len(sample):,} sampled prices: {sample.mean():.3f}")

    # Mark the median on the full distribution.
    figure, axes = plt.subplots(figsize=(7, 4))
    axes.hist(prices, bins=25, edgecolor="white")
    axes.axvline(np.median(prices), color="darkred", label="Median")
    axes.set(xlabel="Normalized used price", ylabel="Device count",
             title="Distribution of normalized used prices")
    axes.legend()
    figure.tight_layout()
    figure.savefig("used_price_histogram.png", dpi=150)
    plt.close(figure)


if __name__ == "__main__":
    main()
