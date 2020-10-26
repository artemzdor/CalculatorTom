from enum import Enum
from abc import ABC


class StateType(str, Enum):
    """Перечисление Штатов"""
    UT: str = "UT"
    NV: str = "NV"
    TX: str = "TX"
    AL: str = "AL"
    CA: str = "CA"


class BaseState(ABC):
    """Базовый класс Штатов для UI"""
    _state: StateType
    _name: str
    _tax_rate: float

    @classmethod
    def state(cls) -> StateType:
        """Тип Штата"""
        return cls._state

    @classmethod
    def name(cls) -> str:
        """Наименование штата"""
        return cls._name

    @classmethod
    def tax_rate(cls) -> float:
        """Налоговая ставка"""
        return cls._tax_rate

    @classmethod
    def calculated_rate(cls, discount_price: float) -> float:
        """Расчет налога"""
        return round(discount_price * (cls.tax_rate() / 100), 2)
