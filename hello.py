from preswald import text, slider, query, table, plotly, connect, get_df, sidebar
import plotly.express as px

# Initialize connection first
connect()

sb = sidebar(defaultopen=True)
sb["title"] = text("🛍️ **Sales Analyzer Pro**")
sb["desc"] = text("Explore Black Friday trends using filters and visual insights.")

# Load data with validation
try:
    df = get_df("black_friday")
    text(f"✅ Successfully loaded {len(df)} rows")
    text("**First 20 rows**")
    
    # Debug: Show first 20 rows to confirm load
    table(df.head(20), title="Data Load Preview")
    
    

except Exception as e:
    text(f"""
    ❌ Critical Error Loading Data: {str(e)}
    **Verify:**
    1. File exists in `data/` folder  
    2. Filename matches `preswald.toml`  
    3. CSV format is valid  
    """)
    raise

# Proceed only if data loaded successfully
if 'df' in locals():
    # Data Cleaning
    text("## Data Cleaning Steps")
    df_clean = df.drop(columns=['Product_Category_2', 'Product_Category_3'])
    df_clean = df_clean.dropna(subset=['Purchase'])
    text("✅ Dropped unused columns (`Product_Category_2`, `Product_Category_3`) and removed rows with missing purchase values.")
    text(f"📊 Final dataset has {len(df_clean.columns)} columns and {len(df_clean)} rows.")
    
    # SQL Analysis Section
    text("## SQL Analysis")

    text("🔍 Displaying the top 20 transactions where the purchase amount exceeds 10,000.")
    sql_filter = """
        SELECT User_ID, Gender, Age, City_Category, Purchase 
        FROM black_friday 
        WHERE Purchase > 10000
        LIMIT 20
    """
    basic_query = query(sql_filter, "black_friday")
    table(basic_query, title="Basic SQL Query Results")

    text("📊 Average spending grouped by age and gender segments.")
    sql_aggregate = """
        SELECT Age, Gender, AVG(Purchase) as Avg_Spending
        FROM black_friday 
        GROUP BY Age, Gender
    """
    aggregated_data = query(sql_aggregate, "black_friday")
    table(aggregated_data, title="Average Spending by Age/Gender")

    # Interactive Controls
    text("## Interactive Analysis")
    text("**Adjust the slider to view observations by Purchase Amount**")

    threshold = slider("Filter by Purchase Amount", 
                      min_val=0,
                      max_val=25000,
                      default=8000,
                      step=500)

    age_groups = ['All'] + sorted(df_clean['Age'].unique().tolist())
    selected_age = age_groups[0]

    # Dynamic Filtering
    filtered_df = df_clean[df_clean['Purchase'] > threshold]
    if selected_age != 'All':
        filtered_df = filtered_df[filtered_df['Age'] == selected_age]

    text(f"📉 Showing **{len(filtered_df)}** transactions")
    table(filtered_df.head(10), title="Live Filtered Data")

    # Visual Insights
    text("## Visual Insights")

    fig1 = px.pie(filtered_df, names='Gender', 
                 title='<b>Gender Distribution</b>')
    plotly(fig1)

    fig2 = px.scatter(
        filtered_df, x='Age', y='Purchase',
        color='City_Category', size='Purchase',
        size_max=30,
        color_discrete_sequence=px.colors.qualitative.Dark24,
        title='<b>Spending Across Cities</b>'
    )
    fig2.update_traces(marker=dict(opacity=0.9, line=dict(width=1, color='black')))
    plotly(fig2)

    fig3 = px.bar(
        df_clean.groupby('Product_Category_1')['Purchase'].mean().reset_index(),
        x='Product_Category_1', y='Purchase',
        title='<b>Average Spending by Product Category</b>'
    )
    plotly(fig3)

else:
    text("🛑 Cannot proceed - fix data loading first.")
