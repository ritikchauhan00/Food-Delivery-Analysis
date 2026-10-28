import streamlit as st
from Cleaning_data import load_clean_data
from Customers_analysis import customer_analysis
from Orders_analysis import analyze_order,monthly_orders
from Delivery_analysis import analyze_delivery,delivery_status
from Connect_sql import connect_database

st.set_page_config(page_title="Food Delivery Analysis",layout="wide")
st.title("Food Delivery Analysis App 🚕")

# customer,menu_item,rest,Orders,delivery

try:
    data=load_clean_data()
    customer=data['Customers']
    orders=data['Orders']
    menu=data['Menu']
    rest=data['Rest']
    delivery=data['Delivery']

except:
    print("Database Connetion Failed")

CA,OA,DA=st.tabs(['Cutomer Analysis','Order Analysis','Delivery Analysis'])

with CA:
    st.header("Customer Analysis Report")
    st.divider()
    col1,col2,col3=st.columns(3)
    customer_analysis_data=customer_analysis(customer,orders)

    col1.header("Total Customers")
    col1.subheader(customer_analysis_data['Total_customer'])

    col2.header("Repeated Customers")
    col2.subheader(customer_analysis_data['repeted_customers'])

    col3.header("New Customers")
    col3.subheader(customer_analysis_data['unique customers'])

    st.divider()
    st.header("Gender Analysis")
    st.divider()
    st.bar_chart(customer_analysis_data['Gender Count'],color="green")
 
    st.divider()
    st.header("Area Analysis")
    st.divider()
    st.bar_chart(customer_analysis_data['City count'],color='green')
   
with OA:
    st.header("Order Analysis Report")
    st.divider()
    col1,col2,col3=st.columns(3)
    orders_analysis_data=analyze_order(orders)
    col1.header("Total Revenue")
    col1.subheader(orders_analysis_data['Revenue'])

    col2.header("Total Orders")
    col2.subheader(orders_analysis_data['Total_Orders'])

    col1.header("Average Order Value")
    col1.subheader(orders_analysis_data['Average_Order'])

    st.divider()
    monthly_order_data=monthly_orders(orders)
    st.header("Monthly Order Analysis")
    st.divider()
    st.line_chart(monthly_order_data,color="green")
   




with DA:
    st.header("Delivery Analysis Report 🛻")
    st.divider()
    d_m=analyze_delivery(orders,delivery)['delivery_minutes']

    average_delivery_minutes=d_m.mean().total_seconds()/60

    st.header("Average Delivery Time")

    st.subheader(average_delivery_minutes) 

    # st.metric("Average delivery Time",f"{average_delivery_minutes:.1f}minutes")

    st.divider()
    st.header("Delivery status")
    status=delivery_status(delivery)
    st.bar_chart(status)

    st.divider()
    st.dataframe(analyze_delivery(orders,delivery))







## SIDEBAR
st.sidebar.header("FOOD DELIVERY DATABASE")

engine,_=connect_database()

if engine is not None:
    st.sidebar.subheader("Status : connected")
else:
    st.sidebar.subheader("Status : Not Connected")




