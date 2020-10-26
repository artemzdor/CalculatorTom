from typing import Union, List
from PySimpleGUI import Text, InputText, Cancel, Button
from src.apps.ui.directory import (
    input_price,
    input_count,
    input_state_code,
    text_base_price,
    text_discount,
    text_percent,
    text_state_name,
    text_tax_rate,
    text_total_price
)

layout_main: List[List[Union[Text, InputText, Button]]] = [
    [
        Text('В ведите пожалуйста. Цену, количество товаров и код штата')
    ],
    [
        Text('Цена за товар', size=(20, 1)),
        InputText(key=input_price, size=(48, 1))
    ],
    [
        Text('Количество товаров', size=(20, 1)),
        InputText(key=input_count, size=(48, 1))
    ],
    [
        Text('Код штата', size=(20, 1)),
        InputText(key=input_state_code, size=(20, 1))
    ],
    [
        Text('Базовая стоимость:', size=(20, 1)),
        Text('333', key=text_base_price, size=(20, 1))
    ],
    [
        Text('Стоимость со скидкой:', size=(20, 1)),
        Text('111', key=text_discount, size=(20, 1)),
        Text('Скидка, %', size=(20, 1)),
        Text('3', key=text_percent, size=(4, 1))
    ],
    [
        Text('Налоги штата:', size=(20, 1)),
        Text('Штат Калифорния', key=text_state_name, size=(20, 1)),
        Text('Налоговая ставка, %', size=(20, 1)),
        Text('8', key=text_tax_rate, size=(4, 1))
    ],
    [
        Text('Итоговая стоимость:', size=(20, 1)),
        Text('10', key=text_total_price, size=(48, 1))
    ],
    [
        Button('Расчет', key='calculation'),
        Cancel('Закрыть', key='exit')
    ]
]