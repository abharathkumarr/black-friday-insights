# 🛍️ Sales Analyzer Pro – Black Friday Purchase Insights

**Sales Analyzer Pro** is an interactive dashboard built with [Preswald](https://preswald.com) to explore and visualize Black Friday shopping patterns.  
It provides powerful data insights through dynamic filtering, SQL-like queries, and real-time visualizations.

---

## 🚀 Live Demo

> 📌 **Hosted on Preswald Cloud:**  
> 🔗 [Click here to view the live app](https://your-preswald-url.preswald.app)

---

## 📊 Features

### ✅ 1. Data Loading and Validation
- Loads data from `BlackFriday.csv` using Preswald's `get_df()`
- Displays a preview of the first 20 rows
- Includes error handling and validation

### 🧹 2. Data Cleaning
- Drops unnecessary columns: `Product_Category_2` and `Product_Category_3`
- Removes rows with missing `Purchase` values
- Displays the cleaned dataset size

### 🧠 3. SQL-like Queries
- **Filtered Transactions:** Purchases over ₹10,000  
- **Aggregated View:** Average purchase value grouped by `Age` and `Gender`

### 🎛️ 4. Interactive Controls
- **Purchase Threshold Slider**: Dynamically filter purchases above a specified value
- **Age Group Selector** (logic-ready): Filter by selected age group

### 📈 5. Visual Insights
- **Pie Chart**: Gender Distribution of filtered transactions
- **Scatter Plot**: Purchase amounts by `Age` and `City_Category`
- **Bar Chart**: Average Spending by Product Category

---

## 📂 Folder Structure
STRUCTURELABSPROJECT/ ├── hello.py # Main app script ├── preswald.toml # App config file ├── pyproject.toml ├── secrets.toml ├── data/ │ └── BlackFriday.csv ├── images/ │ ├── 
