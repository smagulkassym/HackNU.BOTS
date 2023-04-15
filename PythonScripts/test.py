from collections import defaultdict
from datetime import datetime, timedelta
import pandas as pd

# Read the supply and sale tables into pandas dataframes
supply_df = pd.read_csv('umaghacknu_supply.csv', header=None)
sale_df = pd.read_csv('umaghacknu_sale.csv', header=None)

supply_df.columns = ["id", "barcode", "quantity", "price", "supplyTime"]
sale_df.columns = ["id", "barcode", "quantity", "price", "saleTime"]

print(supply_df.columns)
print(sale_df.columns)

def compute_net_profit(supply_df, sale_df, start_time, end_time):
    
    # Filter the supply and sale dataframes by the given time period
    supply_period_df = supply_df[(supply_df['supplyTime'] >= start_time) & (supply_df['supplyTime'] <= end_time)]
    sale_period_df = sale_df[(sale_df['saleTime'] >= start_time) & (sale_df['saleTime'] <= end_time)]
    
    # Sort the dataframes by time
    supply_period_df = supply_period_df.sort_values('supplyTime')
    sale_period_df = sale_period_df.sort_values('saleTime')
    
    # Create a dictionary to keep track of remaining quantity and purchase prices for each barcode
    supply_dict = defaultdict(list)
    for row in supply_period_df.itertuples():
        supply_dict[row.barcode].append((row.quantity, row.price, row.supplyTime))
    
    # Iterate through the sale table and calculate profits
    profits_data = []
    net_profit = 0
    for sale_row in sale_period_df.itertuples():
        barcode = sale_row.barcode
        sale_quantity = sale_row.quantity
        sale_price = sale_row.price
        sale_time = sale_row.saleTime
        
        if barcode not in supply_dict:
            continue
        
        total_supply_quantity = 0
        oldest_purchase_price = 0
        for i, (supply_quantity, purchase_price, purchase_time) in enumerate(supply_dict[barcode]):
            total_supply_quantity += supply_quantity
            if total_supply_quantity >= sale_quantity:
                oldest_purchase_price = purchase_price
                break
        
        if total_supply_quantity < sale_quantity:
            COGS = 0
        else:
            COGS = sale_quantity * oldest_purchase_price
        
        gross_profit = sale_price * sale_quantity - COGS
        net_profit += gross_profit
        
        # Update the remaining quantity for the oldest supply operation
        if total_supply_quantity == sale_quantity:
            del supply_dict[barcode][i]
        elif total_supply_quantity > sale_quantity:
            supply_dict[barcode][i] = (supply_quantity - sale_quantity, purchase_price, purchase_time)
        else:
            while total_supply_quantity < sale_quantity and supply_dict[barcode] :
                supply_quantity, purchase_price, purchase_time = supply_dict[barcode].pop(0) 
                total_supply_quantity += supply_quantity
                COGS += supply_quantity * purchase_price
            if total_supply_quantity > sale_quantity:
                supply_dict[barcode].insert(0, (total_supply_quantity - sale_quantity, purchase_price, purchase_time))
        
        profits_data.append((barcode, sale_price, purchase_price, sale_quantity,  COGS, gross_profit, sale_time))
    profits_df = pd.DataFrame(profits_data, columns=['barcode', 'salePrice','purchasePrice','quantity','GOCS' ,'gross_profit', 'sale_time'])
    profits_df.to_csv('profits.csv', index=False)
    return net_profit




# Create a dictionary to keep track of remaining quantity and purchase prices for each barcode
# Create a profits table
print(compute_net_profit(supply_df, sale_df, '2022-03-01 12:00:00', '2022-05-01 12:00:00'))

