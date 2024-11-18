# Customer-Complaints-Forecasting
## Predicting Customer Complaints: A Time Series Approach for Resource Allocation and Service Optimization

## Project Overview
Customer complaints are critical for assessing customer satisfaction and service quality. This project utilizes time series analysis to predict future customer complaints, enabling businesses to allocate resources efficiently and optimize service delivery. The model helps in proactive management of customer issues and ensures a seamless customer experience.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Problem
As the Head of Customer Support at Diogo's Delicious Chocolate Company, I've noticed a growing trend in customer complaints regarding slow response times to emails and lengthy waiting times on phone calls. We need to understand these trends better and forecast future complaint volumes to allocate our resources effectively and improve our customer service experience. I'd like you to analyze the time series data related to customer complaints and identify patterns that can help us in predicting and address these issues more efficiently.

Recently, the company has been facing a surge in customer complaints, primarily about delayed email responses and extended waiting times on phone calls. To address these concerns, manager, the Head of Customer Support, has tasked with analyzing time series data related to customer complaints. Our goal is to uncover trends, seasonality, and patterns in the data to forecast future complaint volumes. This analysis will play a crucial role in optimizing resource allocation, enhancing response efficiency, and improving the overall customer experience.

## Objectives
* Analyze customer complaints data to uncover trends, seasonality, and patterns through EDA and decomposition.
* Test for stationarity and prepare the data for robust time series modeling.
* Develop and compare forecasting models, including Holt-Winters, SARIMA, Auto ARIMA, and SARIMAX.
* Provide actionable insights to forecast complaint volumes and optimize resource allocation effectively.

## How to Use
To set up and run the Dash app, follow these steps:
### 1. Clone the Repository:
```
git clone 
```

### 2. Navigate to the Project Directory:
```
cd 
```
### 3. Create a Virtual Environment:
```
python -m venv venv
```
Activate the virtual environment:
On Windows:
```
.\venv\Scripts\activate
```
On macOS/Linux:
```
source venv/bin/activate
```

### 4. Install Required Dependencies:
```
pip install -r requirements.txt
```

### 5.Run the Dash App:
```
python app.py
```
Once the app is running, open your web browser and navigate to: http://127.0.0.1:8050

## Data
The dataset consists of weekly customer complaints and associated factors that may influence complaint volumes. It includes the following columns:
* week: The starting date of each week (time series index).
* complaints: The total number of customer complaints received during the week.
* discount_rate: The percentage discount offered during the week, potentially impacting complaint trends.
* small_commercial_event: Binary indicator (1/0) denoting the occurrence of a small-scale commercial event.
* medium_commercial_event: Binary indicator (1/0) denoting the occurrence of a medium-scale commercial event.
* big_commercial_event: Binary indicator (1/0) denoting the occurrence of a large-scale commercial event.

## Methodology
### 1. Data Preprocessing:
* Handling Time Series Data
* Cleaning missing and erroneous data.
* Data Type Conversion
  
### 2. Exploratory Data Analysis (EDA):
* Identifying trends, seasonality, and anomalies.
* Visualizing complaint distribution over time.
* Time-Series Decomposition and Seasonality Analysis

### 3. Stationarity Testing & Differencing
* ACF and PACF Plots

### 4. Model Selection:
* Applying models such as Holt-Winters, SARIMA, Auto ARIMA, SARIMAX.
* Comparing model performance using metrics like RMSE, MAE, and MAPE, AIC.

### 5. Evaluation:
* Validating predictions against test data.
* Generating visualizations for trend forecasts.

### 6. Insights:
* Offering actionable strategies to mitigate common complaints.

## Results & Visualization:
* The Holt-Winters model performed the best with the lowest MAE (406.87), RMSE (491.83), and MAPE (11.94%), making it the most accurate for predicting customer complaints.
*  The Auto SARIMA(2,1,1)X(1,0,0,52) model showed moderate performance, while SARIMAX and SARIMA models had higher error metrics, indicating less accuracy.
*  Overall, Holt-Winters proved to be the most effective model for this dataset.

* Results Plot:
<img width="835" alt="image" src="https://github.com/user-attachments/assets/e1d7ada7-d44b-4fee-af75-0af866244a6e">

* Plotting the Time Series:
<img width="597" alt="image" src="https://github.com/user-attachments/assets/fc5bbcdb-5f32-427f-aa07-8bf49883b0a3">

* STL Decomposition:
<img width="531" alt="image" src="https://github.com/user-attachments/assets/6c2c5fb8-eb93-4d4f-aa5b-1f38f14bd86b">

* Seasonally Differenced Time Series (Complaints):
<img width="572" alt="image" src="https://github.com/user-attachments/assets/24fc33ad-c3b9-4211-8fe9-82fb5f891f4d">

* ACF and PACF Plots:
<img width="845" alt="image" src="https://github.com/user-attachments/assets/f671d3b1-8049-47e8-952d-e8836fceac57">

### Forecasted Plots for different Models:
<img width="623" alt="image" src="https://github.com/user-attachments/assets/a95a7d4e-27f1-4eef-a3a6-ed2288d06544">

<img width="650" alt="image" src="https://github.com/user-attachments/assets/2985feed-2420-494e-a9a4-6fd78a66b4ec">

<img width="632" alt="image" src="https://github.com/user-attachments/assets/563a2490-307f-4d60-ba02-f6a1fd78d60d">

<img width="629" alt="image" src="https://github.com/user-attachments/assets/c423c7e1-ce19-4160-87ef-d2432d5cbd95">

<img width="612" alt="image" src="https://github.com/user-attachments/assets/d7e6f816-456e-4a3f-a0d8-f04c11dbae6d">










