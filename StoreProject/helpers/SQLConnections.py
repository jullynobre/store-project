import psycopg2
from psycopg2 import OperationalError
import mysql.connector
from mysql.connector import Error


def create_connection_postgres(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        print("Connection successful")
    except OperationalError as error:
        print(f"The error '{error}' occurred")
    return connection


def create_connection_mysql(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password
        )
        print("Connection Successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection
