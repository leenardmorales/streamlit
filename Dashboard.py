import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# DB Connection Info



engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
try:
    # Pull data from your table
    df = pd.read_sql('''
    SELECT 
     	ci.t_id AS customer_id,
        company_name,
        unit_name,
        center_name,
        l_date_recog::date,
        customer_name,
        member_status,
        ci.ao_staff_id ,
        acct_officer_name AS staff_name
    FROM 
        public.cust_dashboard ci
    WHERE 
        ci.l_date_recog::date BETWEEN DATE_TRUNC('month', CURRENT_DATE) AND CURRENT_DATE
        AND ci.l_date_recog IS NOT NULL
        AND ci.member_status != 'Resigned'
    ORDER BY center_name;
    ''', engine)

    st.title("📊 New Members Dashboard")

    # ---- FILTER SECTION ----
    unit_names = ["All Units"] + sorted(df["unit_name"].dropna().unique().tolist())
    selected_unit = st.selectbox("Filter by Unit Name:", unit_names)

    if selected_unit != "All Units":
        filtered_df = df[df["unit_name"] == selected_unit]
    else:
        filtered_df = df.copy()

    # ---- PIE CHART SECTION ----
    if "unit_name" in filtered_df.columns:
        unit_summary = filtered_df["unit_name"].value_counts().reset_index()
        unit_summary.columns = ["unit_name", "Count"]

        fig = px.pie(unit_summary, names="unit_name", values="Count",
                     title=f"New Members Distribution ({selected_unit})")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No 'unit_name' column found for pie chart.")

    # ---- TABLE SECTION ----
    st.subheader(f"📋 Raw Table Data ({selected_unit})")
    st.dataframe(filtered_df, use_container_width=True)

except Exception as e:
    st.error(f"❌ Error loading data: {e}")
