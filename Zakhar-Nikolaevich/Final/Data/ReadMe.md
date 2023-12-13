# README for Cryptocurrency Datasets

## Overview
This repository contains datasets detailing various cryptocurrencies, such as Bitcoin Cash (BCH), Bitcoin (BTC), Dash (DASH), and Decred (DCR), over a one-month period. The data, sourced from CoinMarketCap, is recognized for its reliability and is invaluable for analyzing market trends and the behavior of cryptocurrencies.

## Data Structure
Each dataset is presented in a single column with concatenated fields, separated by semicolons. These fields include `open`, `high`, `low`, `close`, `volume`, `marketCap`, and `timestamp`.

## Data Dictionary

| Field      | Description                           | Type      | Range                                       | Frequency  | Example Observations                  |
|------------|---------------------------------------|-----------|---------------------------------------------|------------|---------------------------------------|
| Open       | Opening price for the day.            | float     | 237.71817 - 242.876347                     | Daily      | 237.71817                             |
| High       | Highest price for the day.            | float     | 240.330968 - 250.72849                     | Daily      | 240.330968                            |
| Low        | Lowest price for the day.             | float     | 235.643338 - 242.086232                    | Daily      | 235.643338                            |
| Close      | Closing price for the day.            | float     | 238.234563 - 245.689438                    | Daily      | 238.234563                            |
| Volume     | Trading volume for the day.           | float     | 95444150.0 - 247213000.0                   | Daily      | 95444150.0                            |
| MarketCap  | Market capitalization.                | float     | 4657746000.0 - 4804134000.0                | Daily      | 4657746000.0                          |
| Timestamp  | Date and time of the record.          | datetime  | -                                           | Daily      | 2023-11-04T00:00:00.000Z              |

## Source and Reliability
The data provided in these datasets is sourced from CoinMarketCap, a leading provider of cryptocurrency market data. The information is widely regarded as reliable and accurate.

## Usage Note
The structure and fields are consistent across all datasets in this collection. It is recommended to apply similar parsing methods for each dataset to extract and analyze the data effectively.

![Explainable AI (XAI)(2)](https://github.com/Rising-Stars-by-Sunshine/Zakhar_Merinov_Zm76_Econ_211/assets/149359655/cf006d32-5e27-4f61-8254-f09b3170b8b4)

