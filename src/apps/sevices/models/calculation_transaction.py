from dataclasses import dataclass, field
from typing import Type

from src.apps.sevices.models.percent.base import Percent
from src.apps.sevices.models.state.base import StateType, BaseState


@dataclass
class CalculationTransaction:
    """Модель данных получаемых для расчетов"""
    price: float = field(default=..., metadata='Количество товаров')
    count: int = field(default=..., metadata='Цена за товар')
    state_type: StateType = field(default=..., metadata='Код штата')
    discount_percent: Type[Percent] = field(default=Percent, metadata='Процент скидки')
    state: Type[BaseState] = field(default=..., metadata='Штат')

    def get_base_price(self) -> float:
        """Базовая стоимость"""
        return round(self.price * self.count, 2)

    def get_discount(self) -> float:
        """Стоимость со скидкой"""
        base_price: float = self.get_base_price()
        return round(base_price - self.discount_percent.calculation_percent(base_price=base_price), 2)

    def get_total_price(self) -> float:
        """Обьщая стоимость"""
        discount_price: float = self.get_discount()
        return round(self.get_discount() + self.state.calculated_rate(discount_price=discount_price), 2)
