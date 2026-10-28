from Cleaning_data import load_clean_data

Orders = load_clean_data()['Orders']
print(Orders)

def analyze_order(Orders):
    revenue = Orders['total_price'].sum()
    total_orders = Orders['order_id'].nunique()
    average_order_value = Orders['total_price'].mean()

    return {
        'Revenue': float(revenue),
        'Total_Orders': int(total_orders),
        'Average_Order': float(average_order_value)
    }

# print(analyze_order(Orders))

def monthly_orders(orders):
    orders['months'] = orders['order_datetime'].dt.to_period('M').astype(str)

    return orders.groupby('months')['order_id'].nunique()

print(monthly_orders(Orders))

