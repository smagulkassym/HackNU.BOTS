from collections import defaultdict
from datetime import datetime, timedelta
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import time

start_time = time.time()

engine = create_engine("postgresql+psycopg2://postgres:Ayan2002@localhost/umag_hacknu")


def calculate_gross_profit(barcode, fromTime, toTime):
    sql_querySales = f"SELECT barcode, price, quantity, sale_time FROM umag_hacknu.sale WHERE barcode = {barcode} AND sale_time >= timestamp '{fromTime}' AND sale_time <= timestamp '{toTime}';"
    sql_querySupplies = f"SELECT barcode, price, quantity, supply_time FROM umag_hacknu.supply WHERE barcode = {barcode} AND supply_time <= timestamp '{toTime}';"


    supply_df = pd.read_sql_query(sql_querySupplies, engine)
    sale_df = pd.read_sql_query(sql_querySales, engine)
    # Filter sales and supplies dataframes based on the given parameters
    # Sort the filtered supplies dataframe by supply_time
    # supply_df = supply_df.sort_values(by='supply_time')

    # Initialize variables
    total_quantity = 0
    total_revenue = 0
    total_cost = 0

    # Loop through the filtered sales dataframe and calculate the gross profit using the FIFO approach
    for index, sale in sale_df.iterrows():
        sale_quantity = sale['quantity']
        sale_price = sale['price']
        total_quantity += sale_quantity
        total_revenue += sale_quantity * sale_price

        while sale_quantity > 0:
            supply = supply_df.iloc[0]
            supply_quantity = supply['quantity']
            supply_price = supply['price']

            if sale_quantity >= supply_quantity:
                total_cost += supply_quantity * supply_price
                sale_quantity -= supply_quantity
                supply_df.iloc[0, 1] = 0
                supply_df = supply_df[supply_df['quantity'] > 0]
            else:
                total_cost += sale_quantity * supply_price
                supply_df.iloc[0, 1] -= sale_quantity
                sale_quantity = 0

    # Calculate the gross profit
    gross_profit = total_revenue - total_cost

    # return result
    return barcode, total_quantity, total_revenue, gross_profit
    
   
print(calculate_gross_profit('48743587','2022-01-01 00:00:00', '2023-01-04 15:45:00'))

end_time = time.time()
time_taken = end_time - start_time

print(f"Time taken: {time_taken:.5f} seconds")
