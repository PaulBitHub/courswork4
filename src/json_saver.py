import json

from config import VACANCIES_PATH
from src.saver import Saver
from src.vacancy import Vacancy
from src.vacancies import Vacancies


class JSONSaver(Vacancies, Saver):

    def write_data(self):
        """Метод проверки и записи данных в json файл"""
        try:
            data = json.load(open(VACANCIES_PATH))
        except FileNotFoundError:
            data = []

        data.append(self.to_list_dict())

        with open(VACANCIES_PATH, "w") as file:
            json.dump(self.to_list_dict(), file, indent=7, ensure_ascii=False)

    def get_data(self):
        """Метод по открытию и использованию данных, записанных в json файле"""
        with open(VACANCIES_PATH, encoding="utf-8") as file:
            data = json.load(file)
            self.__all_vacancies = []
            for vacancy in data:
                self.all_vacancies.append(Vacancy.vacancies_lst(vacancy))

    def del_data(self, data_json):
        """Очистка данных из файла json с вакансиями"""
        del data_json
