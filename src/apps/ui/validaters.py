from typing import Optional

from src.apps.sevices.models.state.base import StateType


def validate_int(value: str) -> Optional[int]:
    """Валидатор для количества товаров"""
    if isinstance(value, str) and value.strip().isdigit():
        result: int = int(value.strip())
        if result > 0:
            return result


def validate_float(value: str) -> Optional[float]:
    """Валидатор для цены за товар"""
    if isinstance(value, str):
        try:
            result: float = float(value.strip())
            if result > 0.0:
                return result
        except ValueError:
            return None


def validate_state(value: str) -> Optional[StateType]:
    """Валидатор типа штата"""
    if isinstance(value, str):
        try:
            return StateType(value.upper())
        except ValueError:
            return None

