import streamlit as st
import pandas as pd
import plotly.express as px

# Load your dataset
investment_data = pd.read_csv('dummy_sample.csv')

# Function to display total investment details
def display_total_investment_details():
    total_investment = investment_data['Investment ($M)'].sum()
    total_fund_size = investment_data['Fund Size ($M)'].sum()
    total_global_south_deals = investment_data['Global South Deals Funded'].sum()

    st.write("### Total Investment Overview")
    st.write(f"**Total Investment ($M):** {total_investment}")
    st.write(f"**Total Fund Size ($M):** {total_fund_size}")
    st.write(f"**Total Global South Deals Funded:** {total_global_south_deals}")

# Function to display company details in a friendly format
def display_company_details(company_name):
    company_info = investment_data[investment_data['Company Name'] == company_name]
    if not company_info.empty:
        # Aggregating country names
        countries = company_info['Country'].unique()
        country_names = ", ".join(countries)  # Combine country names

        # Display the details just once
        st.write("### Company Details")
        st.write(f"**Company Name:** {company_name}")
        st.write(f"**Countries:** {country_names}")  # Display all countries together
    else:
        st.write("No details available for this company.")

# Title of the dashboard
st.title("Company Investment Dashboard")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    h1 {
        color: #2c3e50;
        font-family: 'Arial';
    }
    .stButton>button {
        background-color: #2980b9;
        color: white;
        border: None;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #3498db;
    }
    </style>
""", unsafe_allow_html=True)

# Display total investment details
display_total_investment_details()

# Add a company input box and display the comparative graphs
selected_company = st.selectbox("Select a Company", investment_data['Company Name'].unique())

# Display company details
display_company_details(selected_company)

# Extracting data for the selected company
company_data = investment_data[investment_data['Company Name'] == selected_company]

# Check if company data is available
if not company_data.empty:
    st.write(f"### Comparative Analysis for {selected_company}")

    # 1. Bar Chart: Investment vs. Fund Size
    if 'Investment ($M)' in company_data.columns and 'Fund Size ($M)' in company_data.columns:
        fig_investment_vs_fundsize = px.bar(company_data, 
                                             x='Company Name', 
                                             y=['Investment ($M)', 'Fund Size ($M)'], 
                                             title='Investment vs. Fund Size for Selected Company',
                                             barmode='group')
        fig_investment_vs_fundsize.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')  # Transparent background
        st.plotly_chart(fig_investment_vs_fundsize)

    # 2. Bar Chart: Investment vs. Global South Deals Funded
    if 'Global South Deals Funded' in company_data.columns:
        fig_investment_vs_deals = px.bar(company_data, 
                                          x='Company Name', 
                                          y=['Investment ($M)', 'Global South Deals Funded'], 
                                          title='Investment vs. Global South Deals Funded for Selected Company',
                                          barmode='group')
        fig_investment_vs_deals.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')  # Transparent background
        st.plotly_chart(fig_investment_vs_deals)

    # 3. Bar Chart: Fund Size vs. Global South Deals Funded
    if 'Fund Size ($M)' in company_data.columns and 'Global South Deals Funded' in company_data.columns:
        fig_fundsize_vs_deals = px.bar(company_data,
                                        x='Company Name',
                                        y=['Fund Size ($M)', 'Global South Deals Funded'],
                                        title='Fund Size vs. Global South Deals Funded for Selected Company',
                                        barmode='group')
        fig_fundsize_vs_deals.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')  # Transparent background
        st.plotly_chart(fig_fundsize_vs_deals)

# Comparative Graphs for All Companies
st.write("### Comparative Analysis of All Companies")

# 1. Bar Chart: Investment vs. Fund Size for All Companies
if 'Investment ($M)' in investment_data.columns and 'Fund Size ($M)' in investment_data.columns:
    fig_all_investment_vs_fundsize = px.bar(investment_data, 
                                             x='Company Name', 
                                             y=['Investment ($M)', 'Fund Size ($M)'], 
                                             title='Investment vs. Fund Size for All Companies',
                                             barmode='group')
    fig_all_investment_vs_fundsize.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')  # Transparent background
    st.plotly_chart(fig_all_investment_vs_fundsize)

# 2. Bar Chart: Investment vs. Global South Deals Funded for All Companies
if 'Global South Deals Funded' in investment_data.columns:
    fig_all_investment_vs_deals = px.bar(investment_data, 
                                          x='Company Name', 
                                          y=['Investment ($M)', 'Global South Deals Funded'], 
                                          title='Investment vs. Global South Deals Funded for All Companies',
                                          barmode='group')
    fig_all_investment_vs_deals.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')  # Transparent background
    st.plotly_chart(fig_all_investment_vs_deals)

# 3. Bar Chart: Fund Size vs. Global South Deals Funded for All Companies
if 'Fund Size ($M)' in investment_data.columns and 'Global South Deals Funded' in investment_data.columns:
    fig_all_fundsize_vs_deals = px.bar(investment_data,
                                        x='Company Name',
                                        y=['Fund Size ($M)', 'Global South Deals Funded'],
                                        title='Fund Size vs. Global South Deals Funded for All Companies',
                                        barmode='group')
    fig_all_fundsize_vs_deals.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')  # Transparent background
    st.plotly_chart(fig_all_fundsize_vs_deals)
