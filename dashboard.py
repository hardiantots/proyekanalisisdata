import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# Load Data
customers_per_state = pd.read_csv('customers_per_state.csv')
orders_per_state = pd.read_csv('orders_per_state.csv')
customers_per_city = pd.read_csv('customers_per_city.csv')

revenue_per_state = pd.read_csv('revenue_per_state.csv')
avg_order_value_per_state = pd.read_csv('avg_order_value_per_state.csv')
revenue_per_city = pd.read_csv('revenue_per_city.csv')

monthly_sales_2018 = pd.read_csv('monthly_sales_2018.csv')
monthly_sales_2017 = pd.read_csv('monthly_sales_2017.csv')

cost_freight = pd.read_csv('cost_freight.csv')
category_revenue = pd.read_csv('category_revenue.csv')
avg_order_value_per_category = pd.read_csv('avg_order_value_per_category.csv')

late_delivery_per_state = pd.read_csv('late_delivery_per_state.csv')

rfm_df = pd.read_csv('rfm_df.csv')

def function_bar(df, x, y, xlabel, ylabel, title, colors):
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(
        data=df,
        x=x, 
        y=y,
        ax=ax,
        palette=colors)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    st.pyplot(fig)

def function_line(df, x, y, xlabel, ylabel, title, xticks):
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(
        data=df,
        x=x, 
        y=y,
        marker='o', 
        linewidth=2, 
        color='royalblue'
    )
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticklabels(xticks)
    st.pyplot(fig)

st.title("Dashboard E-commerce")

st.sidebar.markdown("Dibuat oleh:")
st.sidebar.markdown("""
Hardianto Tandi Seno (https://github.com/hardiantots)
""")

# Sidebar Navigation
selected_page = st.sidebar.selectbox(
    "Pilih Analisis:",
    [
        "Demografi Pelanggan Berdasarkan Lokasi",
        "Wilayah dengan Pendapatan Tertinggi",
        "Tren Penjualan Bulanan 2 Tahun Terakhir",
        "Kontribusi Kategori Produk terhadap Total Pendapatan",
        "Wilayah dengan Rata-rata Keterlambatan Tertinggi",
        "RFM Analisis"
    ]
)

# Page 1: Demografi Pelanggan
if selected_page == "Demografi Pelanggan Berdasarkan Lokasi":
    st.header("Demografi Pelanggan Berdasarkan Lokasi Geografis")

    # Visualisasi 1: Pelanggan unik per negara bagian
    function_bar(customers_per_state.sort_values(by='customer_unique_id', ascending=False).head(5), "customer_state", "customer_unique_id","State", "Number of Customers",
                "Number of Customers by State", colors = ["#33FF57", "#D2D2D2", "#D2D2D2", "#D2D2D2", "#D2D2D2"])

    # Visualisasi 2: Jumlah pesanan per negara bagian
    function_bar(orders_per_state.sort_values(by='order_id', ascending=False).head(5), "customer_state", "order_id", "State", "Number of Orders",
                "Number of Orders by State", colors = ["#33FF57", "#D2D2D2", "#D2D2D2", "#D2D2D2", "#D2D2D2"])

    # Visualisasi 3: Sebaran pelanggan per kota
    function_bar(customers_per_city.sort_values(by='customer_unique_id', ascending=False).head(5), "customer_unique_id", "customer_city", "Number of Customers",
             "City", "Top 5 Cities with Most Customers", colors = ["#33FF57", "#D2D2D2", "#D2D2D2", "#D2D2D2", "#D2D2D2"])


# Page 2: Wilayah dengan Pendapatan Tertinggi
elif selected_page == "Wilayah dengan Pendapatan Tertinggi":
    st.header("Wilayah dengan Pendapatan Penjualan Tertinggi")

    # Visualisasi 1: Total pendapatan per negara bagian
    function_bar(revenue_per_state.sort_values(by='payment_value', ascending=False).head(5), "customer_state", "payment_value", "State",
             "Total Sales Revenue", "Top 5 Total Sales Revenue by State", colors = ["#F4A261", "#D2D2D2", "#D2D2D2", "#D2D2D2", "#D2D2D2"])

    # Visualisasi 2: Rata-rata nilai pesanan per negara bagian
    function_bar(avg_order_value_per_state.sort_values(by='payment_value', ascending=False).head(5), "customer_state", "payment_value", "State",
             "Average Order Value (AOV)", "Average Order Value per State", colors = ["#F4A261", "#D2D2D2", "#D2D2D2", "#D2D2D2", "#D2D2D2"])

    # Visualisasi 3: Pendapatan per kota
    function_bar(revenue_per_city.sort_values(by='payment_value', ascending=False).head(5), "payment_value", "customer_city", "Total Sales Revenue",
             "City", "Top 5 Cities with Highest Sales Revenue", colors = ["#F4A261", "#D2D2D2", "#D2D2D2", "#D2D2D2", "#D2D2D2"])


# Page 3: Tren Penjualan Bulanan 2 Tahun Terakhir
elif selected_page == "Tren Penjualan Bulanan 2 Tahun Terakhir":
    st.header("Tren Penjualan Bulanan 2 Tahun Terakhir")

    # Visualisasi 1: Tren jumlah order per bulan
    function_line(monthly_sales_2018, 'order_purchase_month', 'order_id', "Month (2018)", "Number of Orders", "Monthly Order Volume in 2018",
              monthly_sales_2018['order_purchase_month'])

    function_line(monthly_sales_2017, 'order_purchase_month', 'order_id', "Month (2017)", "Number of Orders", "Monthly Order Volume in 2017",
              monthly_sales_2017['order_purchase_month'])


# Page 4: Kontribusi Kategori Produk terhadap Pendapatan
elif selected_page == "Kontribusi Kategori Produk terhadap Total Pendapatan":
    st.header("Kontribusi Kategori Produk terhadap Pendapatan")

    # Visualisasi 1: Pendapatan per kategori produk
    function_bar(cost_freight.sort_values(by='freight_value', ascending=False).head(5), "product_category_name_english", "freight_value", "Product Category",
             "Total Freight Cost", "Top 5 Total Freight Cost per Product Category", colors = ["#2A9D8F", "#D2D2D2", "#D2D2D2", "#D2D2D2", "#D2D2D2"])

    # Visualisasi 2: Biaya pengiriman per kategori
    function_bar(category_revenue.sort_values(by='real_price', ascending=False).head(5), "product_category_name_english", "real_price", "Product Category",
             "Total Revenue", "Top 5 Total Revenue per Product Category", colors = ["#2A9D8F", "#D2D2D2", "#D2D2D2", "#D2D2D2", "#D2D2D2"])

    # Visualisasi 3 : Rata-rata nilai pesanan per kategori
    function_bar(avg_order_value_per_category.sort_values(by='price', ascending=False).head(5), "price", "product_category_name_english", "Average Order Value",
             "Product Category", "Top 5 Average Order Value per Product Category", colors = ["#2A9D8F", "#D2D2D2", "#D2D2D2", "#D2D2D2", "#D2D2D2"])

# Page 5: Wilayah dengan Keterlambatan Pengiriman Tertinggi
elif selected_page == "Wilayah dengan Rata-rata Keterlambatan Tertinggi":
    st.header("Wilayah dengan Rata-rata Keterlambatan Pengiriman Tertinggi")

    # Visualisasi 1: Keterlambatan rata-rata per negara bagian
    function_bar(late_delivery_per_state.sort_values('delivery_delay', ascending=False).head(5), "delivery_delay", "customer_state", "Average Delivery Delay",
             "State", "Top 5 Average Delivery Delay", colors = ["#2A9D8F","#D2D2D2", "#D2D2D2", "#D2D2D2", "#D2D2D2"])
    
# Page 6: RFM Analisis
elif selected_page == "RFM Analisis":
    st.header("RFM Analisis pada E-commerce dataset")

    palette_color = ["#72BCD4"] * 5

    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(30, 15))

    # Top 5 Pelanggan berdasarkan Recency
    sns.barplot(
        y='Recency', 
        x="customer_id",
        hue="customer_id",
        data=rfm_df.sort_values(by='Recency', ascending=True).head(5), 
        palette=palette_color, 
        ax=ax[0]
    )
    ax[0].set_title("Best Customers by Recency (days)", fontsize=18)
    ax[0].set_xlabel("Customer ID")
    ax[0].set_ylabel("Recency (Days)")
    ax[0].tick_params(axis='x', labelsize=15, rotation=30)

    # Top 5 Pelanggan berdasarkan Frequency
    sns.barplot(
        y="Frequency", 
        x="customer_id",
        hue="customer_id",
        data=rfm_df.sort_values(by="Frequency", ascending=False).head(5), 
        palette=palette_color, 
        ax=ax[1]
    )
    ax[1].set_title("Best Customers by Frequency", fontsize=18)
    ax[1].set_xlabel("Customer ID")
    ax[1].set_ylabel("Frequency (Total Orders)")
    ax[1].tick_params(axis='x', labelsize=15, rotation=30)

    # Top 5 Pelanggan berdasarkan Monetary
    sns.barplot(
        y="Monetary", 
        x="customer_id", 
        hue="customer_id",
        data=rfm_df.sort_values(by="Monetary", ascending=False).head(5), 
        palette=palette_color, 
        ax=ax[2]
    )
    ax[2].set_title("Best Customers by Monetary", fontsize=18)
    ax[2].set_xlabel("Customer ID")
    ax[2].set_ylabel("Monetary (Total Spending)")
    ax[2].tick_params(axis='x', labelsize=15, rotation=30)

    plt.suptitle("Best Customers Based on RFM Parameters", fontsize=22)
    st.pyplot(fig)