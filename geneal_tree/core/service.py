from abc import ABC, abstractmethod


class BaseService(ABC):
    """Базовый класс сервиса для формирования данных."""

    @staticmethod
    @abstractmethod
    def form_data():
        """Используется для формирования данных."""
        ...

    @staticmethod
    @abstractmethod
    def form_data_for_context(context, name_model=None):
        """Используется для формирования данных в контекст запроса."""
        ...
