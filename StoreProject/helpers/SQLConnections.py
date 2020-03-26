import psycopg2
from psycopg2 import OperationalError
import mysql.connector
from mysql.connector import Error
from decouple import config


class Connections:

    @property
    def postgres_connection(self):
        connection = None
        print(config("PSQL_USER"), config("PSQL_PASSWORD"), config("PSQL_HOST"), config("PSQL_PORT"))
        try:
            connection = psycopg2.connect(
                dbname="",
                user=config("PSQL_USER"),
                password=config("PSQL_PASSWORD"),
                host=config("PSQL_HOST"),
                port=config("PSQL_PORT")
            )
            print("Connection successful")
        except OperationalError as error:
            print(f"The error '{error}' occurred")
        return connection

    @property
    def mysql_connection(self):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=config("MYSQL_HOST"),
                user=config("MYSQL_USER"),
                password=config("MYSQL_PASSWORD")
            )
            connection.database = config("MYSQL_DATABASE")
            print("Connection Successful")
        except Error as e:
            print(f"The error '{e}' occurred")
        return connection
