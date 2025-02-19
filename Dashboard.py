import datetime
import streamlit as st
import pandas as pd
import plotly.express
import datetime
import time

# Function to display real-time clock
def display_time():
    time_placeholder = st.sidebar.empty()  # Sidebar for top-left alignment
    while True:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time_placeholder.markdown(f"### 🕒 {now}")  # Styled time display
        time.sleep(1)  # Update every second

# Run the clock in a separate thread so it updates in real-time
import threading
threading.Thread(target=display_time, daemon=True).start()
# Read the existing CSV file
df = pd.read_csv("CAPSTONEDATA.csv")

# Ensure the required columns exist
required_columns = ["GROSSSALES", "DISCOUNT", "NETSALES", "OTHERINCOME"]
if all(col in df.columns for col in required_columns):
    # Calculate the sum of each column
    gross_sales_sum = df["GROSSSALES"].sum()
    discount_sum = df["DISCOUNT"].sum()
    net_sales_sum = df["NETSALES"].sum()
    other_sales_sum = df["OTHERINCOME"].sum()

    # Define a function to style the metric boxes
    def styled_metric(label, value):
        st.markdown(
            f"""
            <div style="
                border: 3px solid black; 
                border-radius: 20px; 
                padding: 15px; 
                text-align: center; 
                font-size: 20px;
                font-weight: bold;
                background-color: white;
                color: black;
                width: 100%;
            ">
                <p style="margin:0; font-size: 16px;">{label}</p>
                <p style="margin:0; font-size: 22px;">{value}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Display the results in styled containers side by side
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        styled_metric("Total Gross Sales", f"{gross_sales_sum:,.2f}")

    with col2:
        styled_metric("Total Discount", f"{discount_sum:,.2f}")

    with col3:
        styled_metric("Total Net Sales", f"{net_sales_sum:,.2f}")

    with col4:
        styled_metric("Total Other Income", f"{other_sales_sum:,.2f}")
else:
    st.error(f"CSV file must contain the following columns: {required_columns}")
st.divider()

# Read the existing CSV file
df = pd.read_csv("CAPSTONEDATA.csv")

# Ensure required columns exist
if "COUNTRY" in df.columns and "CATEGORY" in df.columns:
    # Get unique categories and add "All Categories" option
    categories = ["All Categories"] + list(df["CATEGORY"].unique())

    # Create a select box for category filtering
    selected_category = st.selectbox("Select a Category:", categories, index=0)

    # Filter data based on the selected category
    if selected_category == "All Categories":
        filtered_df = df  # No filtering, show all data
    else:
        filtered_df = df[df["CATEGORY"] == selected_category]

    # Count the total sales per country for the selected category
    country_sales_count = filtered_df["COUNTRY"].value_counts().reset_index()
    country_sales_count.columns = ["Country", "Total Sales Count"]

    # Create a line chart
    fig = plotly.express.line(country_sales_count, x="Country", y="Total Sales Count",
                  title=f"Total Sales Count per Country ({selected_category})", markers=True)

    # Display the graph
    st.plotly_chart(fig)
else:
    st.error("The CSV file must contain 'COUNTRY' and 'CATEGORY' columns.")

# Ensure the required columns exist
required_columns = ["TOTALTAXABLEINCOME", "NETTAXABLEINCOME"]
if all(col in df.columns for col in required_columns):
    # Calculate the sum of each column
    TOTALTAXABLE = df["TOTALTAXABLEINCOME"].sum()
    NETTAXABLE = df["NETTAXABLEINCOME"].sum()

    # Define a function to style the metric boxes
    def styled_metric(label, value):
        st.markdown(
            f"""
            <div style="
                border: 3px solid black; 
                border-radius: 20px; 
                padding: 15px; 
                text-align: center; 
                font-size: 20px;
                font-weight: bold;
                background-color: white;
                color: black;
                width: 100%;
            ">
                <p style="margin:0; font-size: 16px;">{label}</p>
                <p style="margin:0; font-size: 22px;">{value}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Display the results in styled containers side by side
    col1, col2 = st.columns(2)

    with col1:
        styled_metric("Total Taxable Income ", f"{TOTALTAXABLE:,.2f}")

    with col2:
        styled_metric("Total Net Taxable Income", f"{NETTAXABLE:,.2f}")
else:
    st.error(f"CSV file must contain the following columns: {required_columns}")
st.divider()

if __name__ == "__main__":
    display_time()



