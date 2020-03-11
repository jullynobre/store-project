import helpers.SQLConnections as connections
import pandas.io.sql as pandas_sql

# creating connections
psql_connection = connections.create_connection_postgres("", "postgres", "12345678", "0.0.0.0", "5432")
mysql_connection = connections.create_connection_mysql("127.0.0.1", "root", "Buster")
mysql_connection.database = "CLIENTS_DB"

# getting dataframes
sales_df = pandas_sql.read_sql_query("SELECT id, created_at FROM queries", psql_connection)
sales_items_df = pandas_sql.read_sql_query("SELECT id, sale_id, product_id, price, quantity FROM sale_items",
                                           psql_connection)
products_df = pandas_sql.read_sql_query("SELECT id, name FROM products", mysql_connection)
clients_df = pandas_sql.read_sql_query("SELECT * FROM clients", mysql_connection)

# query with sale.id, sale.id, sale.date, sale_items.price * sale_items.quantity, product.id, product.name
sales_join_items = sales_df.set_index("id").join(sales_items_df.set_index("sale_id"))
sales_join_items = sales_join_items[["id", "created_at", "product_id", "price", "quantity"]]
sales_join_items_join_products = sales_join_items.set_index("product_id")\
    .join(products_df[["id", "name"]].set_index("id"))

print(
    print(sales_join_items_join_products)
)
