# README for Cryptocurrency Datasets

## Overview
This repository contains datasets detailing various cryptocurrencies, such as Bitcoin Cash (BCH), Bitcoin (BTC), Dash (DASH), and Decred (DCR), over a one-month period. The data, sourced from CoinMarketCap, is recognized for its reliability and is invaluable for analyzing market trends and the behavior of cryptocurrencies.

## Data Structure
Each dataset is presented in a single column with concatenated fields, separated by semicolons. These fields include `open`, `high`, `low`, `close`, `volume`, `marketCap`, and `timestamp`.

## Data Dictionary

- **Open**: Opening price for the day. *Type: float*
- **High**: Highest price for the day. *Type: float*
- **Low**: Lowest price for the day. *Type: float*
- **Close**: Closing price for the day. *Type: float*
- **Volume**: Trading volume for the day. *Type: float*
- **MarketCap**: Market capitalization. *Type: float*
- **Timestamp**: Date and time of the record. *Type: datetime*

## Source and Reliability
The data provided in these datasets is sourced from CoinMarketCap, a leading provider of cryptocurrency market data. The information is widely regarded as reliable and accurate.

## Usage Note
The structure and fields are consistent across all datasets in this collection. It is recommended to apply similar parsing methods for each dataset to extract and analyze the data effectively.

