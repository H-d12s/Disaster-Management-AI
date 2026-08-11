"""
=========================================================
DisasterGuard AI
Data Cleaning Pipeline

Author : Your Team
Description:
    Cleans the raw river water level dataset and prepares
    it for feature engineering and model training.
=========================================================
"""

from pathlib import Path
import pandas as pd

# =========================================================
# Configuration
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "river"
    / "river_level.csv"
)

OUTPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "cleaned_data.csv"
)

# Station selected for Version 1
SELECTED_STATION = "Khandiovari"

# =========================================================
# Functions
# =========================================================

def load_data(path: Path) -> pd.DataFrame:
    """Load raw dataset."""
    print("Loading dataset...")
    df = pd.read_csv(path)
    print(f"Dataset Shape : {df.shape}")
    return df


def convert_datetime(df: pd.DataFrame) -> pd.DataFrame:
    """Convert timestamp column to datetime."""

    print("Converting datetime...")

    df["Data Acquisition Time"] = pd.to_datetime(
        df["Data Acquisition Time"],
        dayfirst=True,
        errors="coerce"
    )

    return df


def remove_invalid_dates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows with invalid timestamps."""

    before = len(df)

    df = df.dropna(subset=["Data Acquisition Time"])

    after = len(df)

    print(f"Removed {before-after} invalid rows")

    return df


def select_station(df: pd.DataFrame, station: str) -> pd.DataFrame:
    """Keep only one monitoring station."""

    print(f"Selecting Station : {station}")

    df = df[df["Station"] == station].copy()

    print(f"Rows Remaining : {len(df)}")

    return df


def keep_required_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Keep only columns needed for forecasting."""

    df = df[
        [
            "Data Acquisition Time",
            "River Water Level Telemetry Hourly (meter)"
        ]
    ]

    df.columns = [
        "Timestamp",
        "WaterLevel"
    ]

    return df


def sort_data(df: pd.DataFrame) -> pd.DataFrame:
    """Sort data chronologically."""

    df = df.sort_values("Timestamp")

    df = df.reset_index(drop=True)

    return df


def save_data(df: pd.DataFrame, path: Path):
    """Save cleaned dataset."""

    path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(path, index=False)

    print(f"\nCleaned dataset saved to:\n{path}")


# =========================================================
# Main Pipeline
# =========================================================

def main():

    df = load_data(RAW_DATA_PATH)

    df = convert_datetime(df)

    df = remove_invalid_dates(df)

    df = select_station(df, SELECTED_STATION)

    df = keep_required_columns(df)

    df = sort_data(df)

    save_data(df, OUTPUT_PATH)

    print("\nCleaning Completed Successfully!\n")

    print(df.head())

    print("\nDataset Info")

    print("--------------------------")

    print(df.info())

    print("--------------------------")

    print(df.describe())
    print(df.head(20))
    print(df.tail(20))
    print(df[df["WaterLevel"] > 10])


if __name__ == "__main__":
    main()