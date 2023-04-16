# HackNU/2023 Team BOTS 

## Team BOTS

1. [Smagulkassym Arslanov](https://www.linkedin.com/in/smagulkassym/)
2. Ayan Myrzakhmet
3. Zhalgas Sansyzbay
4. Batyr Bodaubay

## Problem

### Umag/ZapisKZ

1. API: 
    + Sale (GET, GET, POST, PUT, DELETE), 
    + Supply (GET, GET, POST, PUT, DELETE), 
    + Report (GET)
2. The most efficient algorithm

## Stack of Technologies 

### API

1. NodeJS
2. Express
3. pg
4. dotenv

### Algorithm

1. Python
2. SQLAlchemy
3. psycopg2-binary

### Database

1. PostgreSQL
2. pgAdmin

# Time Tests of Algorithm

## Data Set: 
+ barcodeRequest = '48743587'
+ fromTimeRequest = '2022-01-01 00:00:00'
+ toTimeRequest = '2023-01-04 15:45:00'

## Output:
+ barcode: 48743587, 
+ quantity: 11361, 
+ revenue: 7455030, 
+ netProfit: 1133910

## Time Results:
1. 0.06364 seconds
2. 0.06814 seconds
3. 0.06408 seconds
4. 0.06508 seconds
5. 0.06738 seconds
6. 0.06692 seconds
7. 0.07098 seconds
8. 0.06523 seconds
9. 0.06581 seconds
10. 0.06470 seconds

# API Tests
## Sale
1. GET: api/sales?barcode=12334565&fromTime=2022-12-28 11:00:02&toTime=2023-01-05 12:00:02
```
response = 
        [
            {
                "id": 98602,
                "barcode": "12334565",
                "quantity": 2,
                "price": 123,
                "sale_time": "2022-12-28T05:00:02.000Z"
            }
        ]
```
2. GET: api/sales/1
```
response = 
        [
            {
                "id": 1,
                "barcode": "4870204391510",
                "quantity": 1,
                "price": 350,
                "sale_time": "2022-01-01T03:35:31.000Z"
            }
        ]
```
3. POST: api/sales
```
request = 
        {
            "barcode": 12334565,
            "price": 300,
            "quantity": 69,
            "saleTime": "2022-12-26 13:00:07"
        }
```
```
response = 
        {
            "id": 98612
        }
```
4. PUT: api/sales/98612
```
request = 
        {
            "barcode": 12334565,
            "price": 667,
            "quantity": 70,
            "saleTime": "2022-12-28 15:00:02"
        }
```
```
response = 
        {

        }
```
5. DELETE: api/sales/98612
```
response =
        {
            
        }
```
## Supply
1. GET: api/supplies?barcode=4870204391510&fromTime=2022-12-28 11:00:02&toTime=2023-01-05 12:00:02
```
response = 
        [
            {
                "id": 873,
                "barcode": "4870204391510",
                "quantity": 240,
                "price": 310,
                "supply_time": "2022-12-28T07:27:13.000Z"
            }
        ]
```
2. GET: api/supplies/1
```
response = 
        [
            {
                "id": 1,
                "barcode": "4870204391510",
                "quantity": 120,
                "price": 279,
                "supply_time": "2022-01-03T03:20:00.000Z"
            }
        ]
```
3. POST: api/supplies
```
request = 
        {
            "barcode": 12334565,
            "price": 300,
            "quantity": 69,
            "supplyTime": "2022-12-28 11:00:02"
        }
```
```
response = 
        {
            "id": 1075
        }
```
4. PUT: api/supplies/1075
```
request = 
        {
            "barcode": 12334565,
            "price": 667,
            "quantity": 70,
            "supplyTime": "2022-12-28 15:00:02"
        }
```
```
response = 
        {

        }
```
5. DELETE: api/supplies/1075
```
response =
        {
            
        }
```
## Report
1. GET: api/reports?barcode=48743587&fromTime=2022-01-01 00:00:00&toTime=2023-01-04 15:45:00
```
response =
        {
            "barcode": 48743587,
            "quantity": 11361,
            "revenue": 7455030,
            "netProfit": 1133910
        }
```