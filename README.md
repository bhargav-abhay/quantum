# Quantium starter repo
#This Project is For Quantium
#   Overview

This is a simple interactive web dashboard built with Python and the Dash framework. The application allows users to visualize sales data for "Pink Morsel" products, with options to filter the data by region and switch between a line chart and a bar chart representation.

# Features
Interactive Visualization: Displays sales data over time using a Plotly graph.

Region Filtering: A radio button component allows users to filter the data to a specific region (North, East, South, West) or view sales for all regions combined.

Chart Type Selection: A dropdown menu lets the user choose between a line chart or a bar chart to represent the data.

# Prerequisites
To run this application, you need to have Python installed. The following libraries are required:

dash

pandas

plotly

For running the unit tests, you will also need:

pytest

# Installation
Ensure you have Python installed on your system.

Install the required libraries using pip:

# Bash

pip install dash pandas plotly pytest
Make sure you have a combined_sales_data.csv file in the same directory as app.py, or update the file path in app.py to your specific location.

Note: The current code has a hardcoded absolute file path ('C:/Users/ABHAY TRIPATHI/OneDrive/Desktop/javascript/combined_sales_data.csv'). For portability, it is recommended to place the CSV file in the same directory as app.py and change the path to a relative one: pd.read_csv('combined_sales_data.csv').

# Usage
To start the application, navigate to the project directory and run the app.py file from your terminal:

# Bash

python app.py
After running the command, you will see a message in the terminal indicating that the Dash app is running. Open your web browser and go to the provided URL (e.g., http://127.0.0.1:8050/) to view the dashboard.

# Testing
The project includes a suite of unit tests using pytest to ensure the main components of the application's layout are present.

To run the tests, execute the following command in your terminal from the project root directory:

# Bash

pytest
The tests verify that the main header, the sales graph component, and the region picker radio buttons are correctly defined in the app's layout.

# Project Structure
.
├── app.py                     # The main Dash application file
├── test_app.py                # The pytest unit tests
└── combined_sales_data.csv    # The dataset used by the application (assumed)
