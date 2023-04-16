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
1. GET: api/sales?barcode=&fromTime=&toTime=
2. GET: api/sales/id
3. POST: api/sales
{
  "barcode": 12334565,
  "price": 123,
  "quantity": 2,
  "saleTime": "2022-12-28 11:00:02"
}
4. PUT: api/sales/id
{
  "barcode": 12334565,
  "price": 123,
  "quantity": 2,
  "saleTime": "2022-12-28 11:00:02"
}
5. DELETE: api/sales/id

## Supply
1. 

## Report
1. api/reports?barcode=48743587&fromTime=2022-01-01 00:00:00&toTime=2023-01-04 15:45:00