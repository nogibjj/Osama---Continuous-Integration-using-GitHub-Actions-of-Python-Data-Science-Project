"""Python Polars descriptive statistics common functions"""
import polars as pl
import matplotlib.pyplot as plt

def read_aircraft_data_from_google_drive(file_id):
    """
    Read aircraft wildlife strikes data from Google Drive and return it as a Polars DataFrame.

    Args:
    - file_id (str): The ID of the file hosted on Google Drive.

    Returns:
    - df (pl.DataFrame): The aircraft wildlife strikes data as a Polars DataFrame.
    """
    # Construct the URL for the Google Drive file
    url = f"https://drive.google.com/uc?id={file_id}"
    
    try:
        # Download the contents of the CSV file
        download = requests.get(url, timeout=1000).content

        # Read the CSV file into a Polars DataFrame
        df = pl.read_csv(io.StringIO(download.decode("utf-8")),
                         low_memory=False, infer_schema_length=10000)
        
        return df


def return_25th_quantile(data_: pl.DataFrame, target: str) -> float:
    """Takes in a dataframe and returns 25th quantile of the target column"""

    target_quantile = data_[target].quantile(0.25)

    return target_quantile


def return_mean(data_: pl.DataFrame, target: str) -> float:
    """Takes in a dataframe and returns the mean of the target column"""

    target_mean = data_[target].mean()

    return target_mean


def return_std_dev(data_: pl.DataFrame, target: str) -> float:
    """Takes in a dataframe and returns the standard deviation of the target column"""

    target_std = data_[target].std()

    return target_std


def return_median(data_: pl.DataFrame, target: str) -> float:
    """Takes in a dataframe and returns the mean of the target column"""

    target_median = data_[target].median()

    return target_median


 plt.bar(strikes.keys(), strikes.values())
    plt.xticks(rotation=90)
    plt.title("Aircraft Part Damage Probability")
    max_damaged_part = max(strikes, key=strikes.get)
    print(max_damaged_part)
    return strikes, max_damaged_part

def visualize_damage_probabilities(strikes):
    """
    Visualize the aircraft part damage probabilities using a bar chart
    Args:
    - strikes (dict): A dictionary where keys represent aircraft
    parts, and values represent the damage probability.
    """
    # Create a bar chart to visualize the damage probabilities
    plt.bar(strikes.keys(), strikes.values())
    plt.xticks(rotation=90)
    plt.title("Aircraft Part Damage Probability")
  
if __name__ == "__main__":
    file_id = "1TAD7Uyc9PjByt_q13uvGXGeubXnujnUi"
    TARGET_COLUMN = "Aircraft Mass"
    data = read_aircraft_data_from_google_drive(file_id)
    print('Target Column: ', 'TARGET_COLUMN')
    print('25th Quantile: ', return_25th_quantile(data, TARGET_COLUMN))
    print('Mean: ', return_mean(data, TARGET_COLUMN))
    print('Median: ', return_median(data, TARGET_COLUMN))
    print("Standard Deviation: ", return_std_dev(data, TARGET_COLUMN))
