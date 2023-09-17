from API.hh_api import HH
from DBmanager import DBManager
from config import EMPLOYER_MAP

hh = HH()
db_manager = DBManager()
db_manager.connecting_to_bd()

for employer_name, employer_id in EMPLOYER_MAP.items():
    compnay_vacancies = hh.get_vacancies(employer_id)
    for vacancy in compnay_vacancies:
        vacancy_name = vacancy["name"]
        vacancy_experience = vacancy["experience"]['name']
        vacancy_from = int(
            vacancy["salary"]["from"]) if vacancy.get("salary") is not None and vacancy["salary"].get(
            "from") is not None else 0
        db_manager.insert_all_vacancies_table(name=vacancy_name, experience=vacancy_experience, salary=vacancy_from,
                                              employer=employer_id)
    db_manager.insert_company_table(name=employer_name, hh_id=employer_id)

db_manager.disconnect_db()

