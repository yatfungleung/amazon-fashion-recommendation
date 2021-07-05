<img src="/image/streamlit/app_interface.png">

# Amazon Fashion Recommendation
This is a personal project I worked on in 2021.

#### -- Project Status: [Completed]

<br />

## Project Objective
The purpose of this project is to help companies to recommend similar products to target customers for marketing campaigns as well as advertising.

<br />

## Deployment

### Please click the link and have a look: 
### [Amazon Fashion Recommender](https://share.streamlit.io/yatfungleung/amazon-fashion-recommendation/main/app.py)

<br />

#### Demonstration
* Step 1: Select the category of apparel
<img src="/image/streamlit/app_step_1.png" width="700">

* Step 2: Browse through the list of items
  * You can see your competitor's fashion item on top (in this case, Calvin Klein's)
  * And followed by two of your company's recommended products below (Amazon products in this example)
<img src="/image/streamlit/app_step_2.png" width="700">

<br />

### Please click the link and have a look: 
### [Amazon Fashion Recommender](https://share.streamlit.io/yatfungleung/amazon-fashion-recommendation/main/app.py)

<br />

### Methods Used
* Web Scraping
* Image Recognition
* Statistical Modeling

<br />

### Requirements
* Python 3.9.5
* urllib3 1.26.5
* selenium 3.141.0
* tensorflow 2.5.0
* Streamlit 0.84.0
* etc.

<br />

### Project Overview
* [Data Collection(.ipynb)](/1_data_collection.ipynb)
  * Scraping Calvin Klein's Product Links
  * Scraping Each Product's Details
* [Data Cleaning(.ipynb)](/2_data_cleaning.ipynb)
  * 'Price' Cleaning
  * Feature Engineering
    * Creating 'Apparel' Feature
    * Creating 'Color' Feature
    * Combining Two Features
* [Modeling(.ipynb)](/3_modeling.ipynb)
  * Amazon Search Engine Setup
  * Scraping Every Search Result Details
  * Product Recommendation System

