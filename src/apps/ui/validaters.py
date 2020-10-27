from typing import Union
from dataclasses import dataclass
from src.apps.sevices.models.state.base import StateType


@dataclass
class ValidateError:
    message: str


def validate_int(value: str) -> Union[int, ValidateError]:
    """Валидатор для количества товаров"""
    prefix: str = 'Укажите количество единиц товаров: '
    if isinstance(value, str):
        try:
            result: int = int(value.strip())
            if result > 0:
                return result
            else:
                return ValidateError(
                    message=prefix + 'число должно быть боле 0'
                )
        except ValueError:
            pass
    return ValidateError(message=prefix + 'число должно быть целым')


def validate_float(value: str) -> Union[float, ValidateError]:
    """Валидатор для цены за товар"""
    prefix: str = 'Укажите цену товара: '
    if isinstance(value, str):
        try:
            result: float = float(value.strip())
            if result > 0.0:
                return result
            else:
                return ValidateError(
                    message=prefix + 'число должно быть больше 0.0'
                )
        except ValueError:
            pass
    return ValidateError(message=prefix + 'число должно быть дробным')


def validate_state(value: str) -> Union[StateType, ValidateError]:
    """Валидатор типа штата"""
    if isinstance(value, str):
        try:
            return StateType(value.upper())
        except ValueError:
            pass
    return ValidateError(message='Укажите код штата (ut/nv/tx/al/ca)')
