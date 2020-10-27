from typing import Dict, Type

from src.apps.sevices.models.state.base import StateType, BaseState
from src.apps.sevices.models.state.states import (
    StateUT,
    StateNV,
    StateTX,
    StateAL,
    StateCA
)


STATES: Dict[StateType, Type[BaseState]] = {
    StateType.UT: StateUT,
    StateType.NV: StateNV,
    StateType.TX: StateTX,
    StateType.AL: StateAL,
    StateType.CA: StateCA
}
