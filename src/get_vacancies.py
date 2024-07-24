from abc import ABC, abstractmethod


class GetVacanciesAPI(ABC):
    """Абстрактный класс для получения вакансии с hh.ru"""

    @abstractmethod
    def _get_response(self, keyword, per_page):
        pass

    @abstractmethod
    def _get_vacancies(self, keyword, per_page):
        pass

    @abstractmethod
    def get_filter_vacancies(self, keyword, per_page):
        pass
