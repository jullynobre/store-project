from queries.sales_queries import SalesQueries
from helpers.rabbit_publisher import RabbitPublisher
import sys


def main(args):
    sales_queries = SalesQueries()

    if args[0] == "products-with-sales":
        return sales_queries.products_with_sales()
    elif args[0] == "total-sales-by-month":
        return sales_queries.total_sales_by_month()
    elif args[0] == "total-sales-by-client":
        return sales_queries.total_sales_by_client()
    elif args[0] == "total-sales-by-products":
        return sales_queries.total_sales_by_products(args[1], args[2])
    elif args[0] == "publish-queries":
        publisher = RabbitPublisher()
        publisher.queue_message(sales_queries.products_with_sales().to_string())
        publisher.queue_message(sales_queries.total_sales_by_month().to_string())
        publisher.queue_message(sales_queries.total_sales_by_client().to_string())


if __name__ == '__main__':
    print(main(sys.argv[1:]))
