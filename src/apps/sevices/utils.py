from typing import Type, Optional

from src.settings.default import STATES
from src.apps.sevices.models.state.base import StateType, BaseState


def search_state(state: StateType) -> Optional[Type[BaseState]]:
    """Возвращает штат и проверяет тип штата"""
    result: Type[BaseState] = STATES.get(state)
    if result.state() == state:
        return result
