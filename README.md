# Streamlit Dataframe Manipulation App with Natural Language

![Demo GIF](/static/demo.gif)

## Overview
This repository contains a Streamlit application that simplifies data visualization and manipulation using natural language. Users can upload CSV or Excel files, visualize and interact with the data, and modify it using commands in natural language, powered by a custom agent using ChatGPT-4o.

## How It Works
The application workflow is designed for ease of use and interactive data manipulation:

1. **File Upload**: Users can upload a CSV or Excel file which is then read into a DataFrame.
2. **Data Visualization**: The uploaded data is displayed, allowing users to visually inspect and interact with their dataset.
3. **Row Deletion**: Users can delete rows directly from the visualization interface. Note: Due to a current Streamlit widget bug, rows must be deleted twice.
4. **Column Removal**: Users have the option to drop columns from the DataFrame as needed.
5. **Natural Language Queries**: Users can specify queries or commands in natural language to modify the data.
6. **Query Processing and Execution**:
   - Queries are processed by a custom agent equipped with ChatGPT-4o, using the first 5 rows of the DataFrame to generate Python code within a `modify_df` function.
   - This code is executed to apply the specified modifications and return an updated DataFrame.

## Enhanced Capabilities with LLMs
Integrating advanced LLMs like ChatGPT-4o into this application unlocks significant potential for natural language processing in data manipulation. This allows users to interact with data in a more intuitive and accessible manner, reducing the need for technical expertise in data analysis or programming.

## Challenges and Development
The main challenge in this project has been creating robust prompts that consistently return executable Python code. Currently, as this is a prototype designed to showcase the capabilities of LLMs in streamlining data operations, error handling has not yet been implemented. This presents an ongoing area for development to enhance the application's reliability and user experience.

Please try the app here:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://dataframe-nl.streamlit.app/)
