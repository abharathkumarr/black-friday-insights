# 🛍️ Sales Analyzer Pro – Black Friday Purchase Insights

**Sales Analyzer Pro** is an interactive dashboard built with [Preswald](https://preswald.com) to explore and visualize Black Friday shopping patterns.  
It provides powerful data insights through dynamic filtering, SQL-like queries, and real-time visualizations.
---

## 📊 Features

### ✅ 1. Data Loading and Validation
- Loads data from `BlackFriday.csv` using Preswald's `get_df()`
- Displays a preview of the first 20 rows
- Includes error handling and validation
![image](https://github.com/user-attachments/assets/5075e480-7e39-4a59-9607-908a0cafa6fe)

### 🧹 2. Data Cleaning
- Drops unnecessary columns: `Product_Category_2` and `Product_Category_3`
- Removes rows with missing `Purchase` values
- Displays the cleaned dataset size
![image](https://github.com/user-attachments/assets/3951895a-19f8-4eac-b8ef-6564c689327d)

### 🧠 3. SQL-like Queries
- **Filtered Transactions:** Purchases over ₹10,000  
- **Aggregated View:** Average purchase value grouped by `Age` and `Gender`
  ![image](https://github.com/user-attachments/assets/29a03d57-c199-4f01-a323-8e1a1e1177f1)


### 🎛️ 4. Interactive Controls
- **Purchase Threshold Slider**: Dynamically filter purchases above a specified value
- **Age Group Selector** (logic-ready): Filter by selected age group
  ![image](https://github.com/user-attachments/assets/9da50540-75ee-4a19-a3c1-37e3440bb98c)


### 📈 5. Visual Insights
- **Pie Chart**: Gender Distribution of filtered transactions
- **Scatter Plot**: Purchase amounts by `Age` and `City_Category`
- **Bar Chart**: Average Spending by Product Category
  ![image](https://github.com/user-attachments/assets/c51f15e9-8c8a-4b2a-8ae6-9e988035268c)


---

## 📂 Folder Structure
```
STRUCTURELABSPROJECT/ 
├── .venv/ 
├── data/ 
  │ └── BlackFriday.csv 
├── images/ 
  │ ├── analytics.png 
  │ ├── favicon.ico 
  │ ├── logo.png 
  │ └── sidebar.png 
├── .gitignore 
├── hello.py 
├── preswald.toml 
├── pyproject.toml 
└── secrets.toml
```

- **.venv/**: (Optional) Python virtual environment folder.  
- **data/**: Contains the `BlackFriday.csv` dataset.  
- **images/**: Contains image files used in the dashboard (favicon, logos, etc.).  
- **.gitignore**: Lists files/folders that Git should ignore (e.g., `.venv`, secret keys).  
- **hello.py**: Main Preswald app script containing the dashboard code.  
- **preswald.toml**: Configuration file for Preswald (datasource settings, environment info).  
- **pyproject.toml**: Python project configuration (dependencies, packaging).  
- **secrets.toml**: Secure file to store private keys or credentials (excluded from Git).

---

## ⚙️ Technologies Used
- **Preswald SDK** for interactive UI, SQL queries, and deployment
- **Pandas** for data manipulation (via Preswald's built-in support)
- **Plotly Express** for visualizations
- **Python 3.12**

---

## 🛠️ How to Run Locally
```bash
preswald run


## 🧰 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/abharathkumarr/black-friday-insights.git
cd black-friday-insights
```
2.Set Up a Virtual Environment (Recommended)

```
python3 -m venv .venv
source .venv/bin/activate     # On macOS/Linux
.venv\Scripts\activate        # On Windows
```
3. Install Dependencies
```
pip install -r requirements.txt
```
4. Run the App Locally
```
preswald run
```


