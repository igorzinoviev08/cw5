import psycopg2
import pandas as pd
from config import DB_CONNECT


class DBManager:
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    def __init__(self):
        self.connection = None

    def connecting_to_bd(self):
        self.connection = psycopg2.connect(host = 'localhost',database='cw5', user='postgres', password='manager1')

    def disconnect_db(self):
        if self.connection:
            self.connection.close()

    def __execute_query(self, query, params=None):
        with self.connection:
            with self.connection.cursor() as curs:
                curs.execute(query, params)

    def insert_all_vacancies_table(self, **kwargs):
        query = """INSERT INTO vacancy (name, experience, salary, employer)
VALUES (%s, %s, %s, %s);"""
        params = list(kwargs.values())
        self.__execute_query(query, params)

    def insert_company_table(self, **kwargs):
        query = """INSERT INTO employees (name, hh_id)
VALUES (%s,%s);"""
        params = list(kwargs.values())
        self.__execute_query(query, params)
