# Store Project

## Configuring the enviroment

### Initial Requirements
Python 3.7
Anaconda

### Configuring the enviroment
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
