# Amazon price tracker
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/) ![Python Version](https://img.shields.io/badge/python-v3.12%20-blue)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)

This Python script tracks and monitors the price fluctuations of products listed on Amazon. It utilizes web scraping techniques to fetch the current price data and plots the price history over time using Matplotlib. This programme is ideal for users interested in monitoring price changes of specific Amazon products.
## Requirements

Python 3 must be installed in the system.
Additionally install the required Python libraries using pip:

```bash
  pip install requests beautifulsoup4 faker matplotlib pandas
```
`requests` for making HTTP requests to fetch the Amazon page.

`beautifulsoup4` for parsing HTML content of the Amazon page.

`matplotlib` for plotting the price history graph.

`pandas` for handling data in a tabular format.
## Usage

- Replace `url` variable with the URL of the Amazon product that user wants to track.


- Run the programme to fetch the current price of the product on Amazon and save it to a `.txt` file (eg. `price_history.txt`).


- This programme visualizes the price history of the product. The script reads the data from `price_history.txt` and plots a graph using Matplotlib. It also saves the plot as a `.png` file. (eg.`price_history.png` )

## Features

- Fetches and tracks the current price of a specified Amazon product at fixed intervals.
- Stores price data in a `.txt` file for historical tracking.
- This project utilizes `faker` library to randomize the user-agent. 
- Visualizes price history with an interactive plot using Matplotlib.
- Easy setup and execution with clear instructions for customization.


## License



This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License - see the LICENSE file for details.
## 🚀 About Me
I'm a microbiology student. i have keen interest in python and programming in general.

