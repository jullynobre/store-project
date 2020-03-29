# Store Project

## About implementation
![Data flow](https://github.com/jullynobre/store-project/blob/readme/docs/data-flow.png)

The project queries are executed once a day and the data is published to the RabbitMQ queue, where the client services can consume the data.

## Configuring the enviroment

### Initial Requirements
Python 3.7  
Anaconda

### Installation
Install pip for conda
```
conda install pip
```

Create the env with pip
```
conda create -n condenv pip
```

Activate the env
```
conda activate condenv
```

Install requirements
```
pip install requirements.txt
```

### Configuring the enviroment variables
On file [.env.example](.env.example) are the needed env variables for rurring the application.  

```
PSQL_USER=root
PSQL_PASSWORD=12345678
PSQL_PORT=1234
PSQL_HOST=0.0.0.0

MYSQL_USER=root
MYSQL_HOST=0.0.0.0
MYSQL_PASSWORD=12345678
MYSQL_DATABASE=CLIENTS_DB

SYSTEM_USERNAME=rootuser
```
Modify their values with valid data and rename the file to ".env".

## Using the queries

### Products with sales
Returns a join with all sales and their products
```
python queries/manager.py products-with-sales
```

### Total sales by month
Returns a total sum of the sales (in R$) grouped by months.
```
python queries/manager.py total-sales-by-month
```

### Total sales by client
Returns a total sum of the sales (in R$) grouped by clients.
```
python queries/manager.py total-sales-by-client
```

### Total sales by products (with filter by period)
Returns a total sum of the sales (in R$) with are made within the informed period, grouped by products.
```
python queries/manager.py total-sales-by-products 2018-01-01 2019-01-01
```
