from PySimpleGUI import Window, Text

from src.apps.sevices.models.calculation_transaction import (
    CalculationTransaction
)
from src.apps.ui.directory import (
    text_percent,
    text_total_price,
    text_tax_rate,
    text_discount,
    text_base_price,
    text_state_name
)


def clear_output_text_ui(window: Window) -> None:
    """Очистка данных от старых расчетов"""
    for iter_text in [
        text_percent,
        text_total_price,
        text_tax_rate,
        text_discount,
        text_base_price,
        text_state_name
    ]:
        iter_text: Text = window[iter_text]
        iter_text.update(value='')


def write_output_text_ui(
        transaction: CalculationTransaction, window: Window
) -> None:
    """Запись данных UI"""
    percent_display: Text = window[text_percent]
    total_price: Text = window[text_total_price]
    tax_rate: Text = window[text_tax_rate]
    discount: Text = window[text_discount]
    base_price: Text = window[text_base_price]
    state_name: Text = window[text_state_name]

    base_price.update(value=str(transaction.get_base_price()))
    state_name.update(value=transaction.state.name())
    discount.update(value=str(transaction.get_discount()))
    total_price.update(value=str(transaction.get_total_price()))

    value: str = str(transaction.discount_percent.get_percent(
        base_price=transaction.get_base_price())
    )

    percent_display.update(value=value)
    tax_rate.update(value=str(transaction.state.tax_rate()))
