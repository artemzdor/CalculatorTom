from typing import Type

import pytest

from src.apps.sevices.models.percent.base import Percent


class TestPercent:
    percent: Type[Percent] = Percent

    @pytest.mark.parametrize(
        'base_price,result_percent,calculation_percent',
        [
            (0.0, 0.0, 0.0),
            (50.0, 0.0, 0.0),
            (999.99, 0.0, 0.0),
            (1000.0, 3.0, 30.0),
            (1500.0, 3.0, 45.0),
            (4999.99, 3.0, 150.0),
            (5000.00, 5.0, 250.0),
            (6999.99, 5.0, 350.0),
            (7000.00, 7.0, 490.0),
            (9999.99, 7.0, 700.0),
            (10_000.00, 10.0, 1000.0),
            (49_999.99, 10.0, 5000.0),
            (50_000.00, 15.0, 7500.0),
            (100_000.00, 15.0, 15_000.0)
        ]
    )
    def test_percent(self, base_price: float, result_percent: float, calculation_percent: float):
        result: float = self.percent.get_percent(base_price=base_price)
        assert result == result_percent

        result_calculation_percent: float = self.percent.calculation_percent(base_price=base_price)
        assert result_calculation_percent == calculation_percent

