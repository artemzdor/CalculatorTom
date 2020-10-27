# CalculatorTom

#### Задача 
Ui калькулятор тома
```
Готовый продукт - розничный калькулятор Тома
```

```
Три поля для ввода:
 - Количество товаров.
 - Общая стоимость заказа
 - Цена за товар.
```

```
Поле вывода:
 - Общая стоимость заказа
```

утсновка 
```bash
git clone git@github.com:artemzdor/CalculatorTom.git
cd CalculatorTom
python3.8 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```


запуск
```bash
cd CalculatorTom # зайти в корень проекта
source ./venv/bin/activate
export PYTHONPATH=$PWD
python ./src/main.py
```

тесты
```bash
cd CalculatorTom # зайти в корень проекта
source ./venv/bin/activate
export PYTHONPATH=$PWD
python -m pytest
```

flake8
```bash
cd CalculatorTom # зайти в корень проекта
source ./venv/bin/activate
export PYTHONPATH=$PWD
flake8 ./src/
```