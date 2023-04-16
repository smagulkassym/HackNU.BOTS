from collections import defaultdict
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import time
import sys
import json

DB_USER = 'postgres'
DB_PASSWORD = '1'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'umag_hacknu'

engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

def calculate_gross_profit(barcode, fromTime, toTime):
    # SQL queries
    sql_querySales = f"SELECT barcode, price, quantity FROM umag_hacknu.sale WHERE barcode = {barcode} AND sale_time >= timestamp '{fromTime}' AND sale_time <= timestamp '{toTime}';"
    sql_querySupplies = f"SELECT barcode, price, quantity FROM umag_hacknu.supply WHERE barcode = {barcode} AND supply_time <= timestamp '{toTime}';"

    # Get results from the database
    with engine.connect() as conn:
        # Get supply data
        result = conn.execute(text(sql_querySupplies))
        supplies = []
        for supply in result.fetchall():
            supplies.append(list(supply))

        # Get sales data
        result = conn.execute(text(sql_querySales))
        sales = []
        for sale in result.fetchall():
            sales.append(list(sale))

    # Initialize variables
    total_quantity = 0
    total_revenue = 0
    total_cost = 0

    # Loop through the sales data and calculate the gross profit using the FIFO approach
    for sale in sales:
        sale_quantity = sale[2]
        sale_price = sale[1]
        total_quantity += sale_quantity
        total_revenue += sale_quantity * sale_price

        while sale_quantity > 0:
            if len(supplies) == 0:
                break
            supply = supplies[0]
            supply_quantity = supply[2]
            supply_price = supply[1]

            if sale_quantity >= supply_quantity:
                total_cost += supply_quantity * supply_price
                sale_quantity -= supply_quantity
                supplies.pop(0)
            else:
                total_cost += sale_quantity * supply_price
                supplies[0][2] -= sale_quantity
                sale_quantity = 0

    # Calculate the gross profit
    gross_profit = total_revenue - total_cost

    # print(barcode)
    # print(total_quantity)
    # print(total_revenue)
    # print(gross_profit)

    result = {
        "barcode": barcode,
        "quantity": total_quantity,
        "revenue": total_revenue,
        "netProfit": gross_profit
    }
    # Return result
    return result
    
##########################   
# start_time = time.time()
##########################

#                 TEST
##########################################
# barcodeRequest = '48743587'
# fromTimeRequest = '2022-01-01 00:00:00'
# toTimeRequest = '2023-01-04 15:45:00'
##########################################

barcodeRequest = sys.stdin.readline().strip()
fromTimeRequest = sys.stdin.readline().strip()
toTimeRequest = sys.stdin.readline().strip()

response = calculate_gross_profit(barcodeRequest, fromTimeRequest, toTimeRequest)
json_response = json.dumps(response)

# Send the JSON object back to Node.js
sys.stdout.write(json_response)

# print(response)

#################################################
# end_time = time.time()
# time_taken = end_time - start_time
# print(f"Time taken: {time_taken:.5f} seconds")
#################################################