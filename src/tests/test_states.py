from typing import Type

import pytest

from src.apps.sevices.utils import search_state
from src.apps.sevices.models.state.base import BaseState, StateType
from src.apps.sevices.models.state.states import (
    StateUT,
    StateNV,
    StateTX,
    StateAL,
    StateCA
)


class TestStates:

    @pytest.mark.parametrize(
        'state_type,state,tax_rate,discount_price,calculated_rate',
        [
            (StateType.UT, StateUT, 6.85, 1000, 68.5),
            (StateType.NV, StateNV, 8.0, 1000, 80.0),
            (StateType.TX, StateTX, 6.25, 1000, 62.5),
            (StateType.AL, StateAL, 4.0, 1000, 40.0),
            (StateType.CA, StateCA, 8.25, 1000, 82.5)
        ]
    )
    def test_get_states(self, state_type: StateType, state: BaseState,
                        tax_rate: float, discount_price: float, calculated_rate: float) -> None:
        state_result: Type[BaseState] = search_state(state=state_type)
        assert isinstance(state_result, type(state))
        assert state_result.state() == state.state()
        assert state_result.tax_rate() == tax_rate
        assert state_result.calculated_rate(discount_price=discount_price) == calculated_rate


