import queries.sales_queries as sales_queries
import sys


def main(args):
    if args[0] == "products-with-sales":
        return sales_queries.products_with_sales()
    elif args[0] == "total-sales-by-month":
        return sales_queries.total_sales_by_month()
    elif args[0] == "total-sales-by-client":
        return sales_queries.total_sales_by_client()
    elif args[0] == "total-sales-by-products":
        return sales_queries.total_sales_by_products(args[1], args[2])


if __name__ == '__main__':
    print(main(sys.argv[1:]))
