import psycopg2
import pandas as pd



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


    def __show_result(self, query, params=None):
        """Метод для вывода"""
        with self.connection:
            with self.connection.cursor() as cur:
                cur.execute(query, params)
                result = cur.fetchall()
                columns = [desc[0] for desc in cur.description]
                print(pd.DataFrame(result, columns=columns).to_string(index=False))

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


    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании"""
        query = """SELECT employer, COUNT(*) AS quantity_of_vacancies
                    FROM vacancy
                    GROUP BY employer;"""
        self.__show_result(query)

    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию"""
        query = """SELECT * FROM vacancy;"""
        self.__show_result(query)

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям"""
        query = """SELECT
    (SELECT ROUND(AVG(salary)) FROM vacancy WHERE salary <> 0) as avg_salary_from;"""
        self.__show_result(query)

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        query = """SELECT * FROM vacancy
WHERE salary >
    (SELECT ROUND(AVG(salary)) FROM vacancy WHERE salary <> 0);"""
        self.__show_result(query)

    def get_vacancies_with_keyword(self, keyword):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python"""
        query = """SELECT * FROM vacancy
WHERE LOWER(name) ILIKE %s;"""
        params = ("%" + keyword + "%",)
        self.__show_result(query, params=params)
