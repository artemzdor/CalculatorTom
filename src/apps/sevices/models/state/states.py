from src.apps.sevices.models.state.base import StateType, BaseState

__all__ = ['StateUT', 'StateNV', 'StateTX', 'StateAL', 'StateCA']


class StateUT(BaseState):
    """Штат Юта"""
    _name = "Юта"
    _state = StateType.UT
    _tax_rate = 6.85


class StateNV(BaseState):
    """Штат Невада"""
    _name = "Невада"
    _state = StateType.NV
    _tax_rate = 8.0


class StateTX(BaseState):
    """Штат Техас"""
    _name = "Техас"
    _state = StateType.TX
    _tax_rate = 6.25


class StateAL(BaseState):
    """Штат Алабама"""
    _name = "Алабама"
    _state = StateType.AL
    _tax_rate = 4.0


class StateCA(BaseState):
    """Штат Калифорния"""
    _name = "Калифорния"
    _state = StateType.CA
    _tax_rate = 8.25
