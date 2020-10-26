
class Percent:

    @classmethod
    def get_percent(cls, base_price: float) -> float:
        """Получение процента скидки
            >= 1000 -> % 3.0
            >= 5000 -> % 5.0
            >= 7000 -> % 7.0
            >= 10_000 -> % 10.0
            >= 50_000 -> % 15.0
        """
        if 0.0 >= base_price:
            return 0.0

        if 0.0 < base_price < 1000.0:
            return 0.0

        if 1000.0 <= base_price < 5000.0:
            return 3.0

        if 5000.0 <= base_price < 7000.0:
            return 5.0

        if 7000.0 <= base_price < 10_000.0:
            return 7.0

        if 10_000.0 <= base_price < 50_000.0:
            return 10.0

        if 50_000.0 <= base_price:
            return 15.0

    @classmethod
    def calculation_percent(cls, base_price) -> float:
        """Расчер скидки"""
        return round(base_price * (cls.get_percent(base_price=base_price) / 100), 2)
