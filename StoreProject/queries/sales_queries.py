import helpers.SQLConnections as connections
import pandas.io.sql as pandas_sql
import datetime


class SalesQueries:
    # creating connections
    postgres_connection = connections.create_connection_postgres("", "postgres", "12345678", "0.0.0.0", "5432")
    mysql_connection = connections.create_connection_mysql("127.0.0.1", "root", "Buster")
    mysql_connection.database = "CLIENTS_DB"

    # getting data frames
    sales_df = pandas_sql.read_sql_query("SELECT * FROM sales", postgres_connection)
    sales_items_df = pandas_sql.read_sql_query("SELECT * FROM sale_items", postgres_connection)
    products_df = pandas_sql.read_sql_query("SELECT id, name FROM products", mysql_connection)
    clients_df = pandas_sql.read_sql_query("SELECT id, name FROM clients", mysql_connection)

    def sales(self, initial_date: datetime = None, final_date: datetime = None):
        filtered_sales = self.sales_df
        # where date is after initial_date
        if initial_date:
            filtered_sales = filtered_sales[filtered_sales['created_at'] >= initial_date]
        # where date is before final_date
        if final_date:
            filtered_sales = filtered_sales[filtered_sales['created_at'] <= final_date]

        return filtered_sales

    def sale_items(self, sale_id: int, product_id: int = None, client_id: int = None):
        filtered_sale_items = self.sales_items_df[self.sales_items_df['sale_id'] == sale_id]
        # where product is equal to
        if product_id:
            filtered_sale_items = filtered_sale_items[filtered_sale_items['product_id'] == product_id]
        # where client is equal to
        if client_id:
            filtered_sale_items = filtered_sale_items[filtered_sale_items['client_id'] == client_id]

        return filtered_sale_items

    def products_with_sales(self):
        # query with sale.id, sale.id, sale.date, sale_items.price * sale_items.quantity, product.id, product.name
        sales_join_items = self.sales_df.set_index("id").join(self.sales_items_df.set_index("sale_id"))
        sales_join_items = sales_join_items[["id", "created_at", "product_id", "price", "quantity"]]
        sales_join_items["total_price"] = sales_join_items["price"] * sales_join_items["quantity"]
        sales_join_items_join_products = sales_join_items.set_index("product_id") \
            .join(self.products_df[["id", "name"]].set_index("id"))

        return sales_join_items_join_products

    def total_sales_by_products(self, initial_date: datetime, final_date: datetime):
        sales_df = self.sales(initial_date, final_date)
        sales_with_items_df = sales_df.set_index("id").join(self.sales_items_df.set_index("sale_id"))
        sales_with_items_df["total_sale"] = sales_with_items_df["price"] * sales_with_items_df["quantity"]
        sales_with_items_df = sales_with_items_df[["created_at", "product_id", "total_sale"]]
        sales_with_items_df = sales_with_items_df.groupby(['product_id']).sum()
        sales_with_items_df = sales_with_items_df.join(self.products_df[["id", "name"]].set_index("id"))
        sales_with_items_df.reset_index(inplace=True)

        return sales_with_items_df

    def total_sales_by_month(self):
        return self.mysql_connection

    def total_sales_by_client(self):
        return self.mysql_connection


print(SalesQueries().total_sales_by_products('2019-03-28', '2019-04-28'))
