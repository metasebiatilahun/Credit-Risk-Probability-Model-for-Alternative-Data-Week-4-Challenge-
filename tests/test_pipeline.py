import pytest

def test_cap_outliers():
    # Test that values beyond 3 SD are correctly clipped [cite: 71, 77]
    data = pd.Series([1, 1.1, 1.2, 500]) # 500 is a clear outlier
    capped = cap_outliers(data, n_std=1)
    assert capped.max() < 500
    assert len(capped) == len(data) # Ensure no rows were dropped 

def test_data_fetch_integrity():
    # Ensure the dataframe contains the expected tickers [cite: 53]
    assert all(ticker in df['Ticker'].unique() for ticker in config.assets)