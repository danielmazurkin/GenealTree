from abc import ABC, abstractmethod


class BaseService(ABC):
    """Базовый класс сервиса для формирования данных."""

    @staticmethod
    @abstractmethod
    def form_data():
        ...

    @staticmethod
    @abstractmethod
    def form_data_for_context(context, name_model=None):
        ...
