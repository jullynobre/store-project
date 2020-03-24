import helpers.SQLConnections as connections
import pandas as pd
import datetime


class SalesQueries:
    # creating connections
    postgres_connection = connections.create_connection_postgres("", "postgres", "12345678", "0.0.0.0", "5432")
    mysql_connection = connections.create_connection_mysql("127.0.0.1", "root", "Buster")
    mysql_connection.database = "CLIENTS_DB"

    # getting data frames
    sales_df = pd.io.sql.read_sql_query("SELECT * FROM sales", postgres_connection)
    sales_items_df = pd.io.sql.read_sql_query("SELECT * FROM sale_items", postgres_connection)
    products_df = pd.io.sql.read_sql_query("SELECT id, name FROM products", mysql_connection)
    clients_df = pd.io.sql.read_sql_query("SELECT id, name FROM clients", mysql_connection)

    def sales(self, initial_date: datetime = None, final_date: datetime = None, client_id: int = None):
        filtered_sales = self.sales_df
        # where date is after initial_date
        if initial_date:
            filtered_sales = filtered_sales[filtered_sales['created_at'] >= initial_date]
        # where date is before final_date
        if final_date:
            filtered_sales = filtered_sales[filtered_sales['created_at'] <= final_date]
        # where client is equal to
        if client_id:
            filtered_sales = filtered_sales[filtered_sales['client_id'] == client_id]

        return filtered_sales

    def products_with_sales(self):
        sales_with_items_df = self.sales_df.set_index("id").join(self.sales_items_df.set_index("sale_id"))
        sales_with_items_df = sales_with_items_df[["id", "created_at", "product_id", "price", "quantity"]]
        sales_with_items_df["total_price"] = sales_with_items_df["price"] * sales_with_items_df["quantity"]
        sales_with_items_df = sales_with_items_df.set_index("product_id") \
            .join(self.products_df[["id", "name"]].set_index("id"))

        return sales_with_items_df

    def total_sales_by_products(self, initial_date: datetime, final_date: datetime):
        filtered_sales_df = self.sales(initial_date, final_date)
        sales_with_items_df = filtered_sales_df.set_index("id").join(self.sales_items_df.set_index("sale_id"))
        sales_with_items_df["total_sale"] = sales_with_items_df["price"] * sales_with_items_df["quantity"]
        sales_with_items_df = sales_with_items_df[["product_id", "total_sale"]]
        sales_with_items_df = sales_with_items_df.groupby(['product_id']).sum()
        sales_with_items_df = sales_with_items_df.join(self.products_df[["id", "name"]].set_index("id"))
        sales_with_items_df.reset_index(inplace=True)

        return sales_with_items_df

    def total_sales_by_month(self):
        sales_with_items_df = self.sales_df.set_index("id").join(self.sales_items_df.set_index("sale_id"))
        sales_with_items_df["total_sale"] = sales_with_items_df["price"] * sales_with_items_df["quantity"]
        sales_with_items_df["Month/Year"] = pd.to_datetime(sales_with_items_df['created_at']).dt.to_period('M')
        sales_with_items_df = sales_with_items_df[["Month/Year", "total_sale"]]
        sales_with_items_df = sales_with_items_df.groupby(["Month/Year"]).sum()
        sales_with_items_df.reset_index(inplace=True)

        return sales_with_items_df

    def total_sales_by_client(self):
        sales_with_items_df = self.sales_df.set_index("id").join(self.sales_items_df.set_index("sale_id"))
        sales_with_items_df["total_sale"] = sales_with_items_df["price"] * sales_with_items_df["quantity"]
        sales_with_items_df = sales_with_items_df[["client_id", "total_sale"]]
        sales_with_items_df = sales_with_items_df.groupby(["client_id"]).sum()
        sales_with_items_df = sales_with_items_df.join(self.clients_df[["id", "name"]].set_index("id"))
        sales_with_items_df.reset_index(inplace=True)

        return sales_with_items_df
