## Customer Analysis

from Cleaning_data import load_clean_data

def customer_analysis(customer_df,Orders):
    total_customer=customer_df['customer_id'].nunique()
    gender_count=customer_df['gender'].value_counts()
    city=[]
    
    for address in customer_df['Address']:
        city.append(address.split(",")[-1].strip())
    customer_df['city']=city
    city_count=customer_df['city'].value_counts()
    
    # repeted_customers=Orders['customer_id'].value_counts()
    # total_repeted_customers=repeted_customers > 1

    # Find repeated customer IDs in Orders
    repeted_customers = Orders['customer_id'].value_counts()>1
    

    # Count repeated customer IDs
    total_repeted_customers = repeted_customers.sum()
    new_customers=total_customer-total_repeted_customers

    # return repeted_customers
    
    return {'Total_customer':total_customer,
            'Gender Count':gender_count,
            'City count':city_count,
            # 'repeted_customers':repeted_customers,
            'repeted_customers':total_repeted_customers,
            'unique customers':new_customers
            }

customer_df=load_clean_data()['Customers']

order_df=load_clean_data()['Orders']

print(order_df.columns)
print(order_df.shape)
print(customer_df.columns)


print(customer_analysis(customer_df,order_df))
