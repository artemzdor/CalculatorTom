from typing import Optional, Type, Union

import PySimpleGUI
from PySimpleGUI import Window

from src.apps.ui.layout import layout_main
from src.apps.sevices.utils import search_state
from src.apps.sevices.models.percent.base import Percent
from src.apps.sevices.models.state.base import StateType, BaseState
from src.apps.ui.display import clear_output_text_ui, write_output_text_ui
from src.apps.ui.directory import input_price, input_count, input_state_code
from src.apps.ui.validaters import (
    validate_float,
    validate_int,
    validate_state,
    ValidateError
)
from src.apps.sevices.models.calculation_transaction import (
    CalculationTransaction
)


def main() -> None:
    PySimpleGUI.theme('Topanga')
    window: Window = Window('Калькулятор Тома', layout_main, finalize=True)

    clear_output_text_ui(window=window)

    while True:  # Event Loop
        event, values = window.read()
        clear_output_text_ui(window=window)

        if event in (PySimpleGUI.WIN_CLOSED, 'exit'):
            break

        price: Union[float, ValidateError] = validate_float(
            value=values[input_price]
        )

        count: Union[int, ValidateError] = validate_int(
            value=values[input_count]
        )

        state_type: Union[StateType, ValidateError] = validate_state(
            value=values[input_state_code]
        )

        if isinstance(price, ValidateError):
            PySimpleGUI.popup('Ошибка', price.message)
            continue

        if isinstance(count, ValidateError):
            PySimpleGUI.popup('Ошибка', count.message)
            continue

        if isinstance(state_type, ValidateError):
            PySimpleGUI.popup('Ошибка', state_type.message)
            continue

        state: Optional[Type[BaseState]] = search_state(state=state_type)

        if state is None:
            PySimpleGUI.popup('Ошибка', 'Не удалось найти штат для налогов')
            continue

        transaction: CalculationTransaction = CalculationTransaction(
            price=price,
            count=count,
            state_type=state_type,
            discount_percent=Percent,
            state=state
        )
        write_output_text_ui(transaction=transaction, window=window)


if __name__ == '__main__':
    main()
