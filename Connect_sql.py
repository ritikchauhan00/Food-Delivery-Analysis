import pandas as pd

from sqlalchemy import create_engine

def connect_database():
    try:
        engine=create_engine(url="mysql+pymysql://root:root@localhost/food_delivery")
      
    except:
        return None, False
    else:
          return engine,True



def connect_tables():
    try:
        engine,_=connect_database()
        if engine is not None:
            customer=pd.read_sql_query("select * from customers;",engine)
            menu_item=pd.read_sql_query("select * from menu_item;",engine)
            rest=pd.read_sql_query("select * from restaurants;",engine)
            delivery=pd.read_sql_query("select * from delivery;",engine)
            Orders=pd.read_sql_query("select * from orders;",engine)
        
    except:
        print("Table Name is Incorrect")
        raise
    else:
         return customer,menu_item,rest,Orders,delivery
        # return Orders

# customer,menu_item,rest,Orders,delivery=connect_tables()
# print(Orders)
# print(customer)
# print(menu_item)
# print(delivery)
# print(rest)


