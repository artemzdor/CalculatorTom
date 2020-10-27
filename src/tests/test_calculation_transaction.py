from src.apps.sevices.models.state.states import StateNV
from src.apps.sevices.models.state.base import StateType
from src.apps.sevices.models.calculation_transaction import (
    CalculationTransaction
)


class TestCalculationTransaction:
    transaction: CalculationTransaction = CalculationTransaction(
        price=10_000,
        count=2,
        state_type=StateType.NV,
        state=StateNV
    )

    def test_base_price(self):
        assert self.transaction.get_base_price() == 20_000.0

    def test_discount(self):
        assert self.transaction.get_discount() == 18_000.0

    def test_total_price(self):
        assert self.transaction.get_total_price() == 19_440.0
