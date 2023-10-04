# hw_python_oop - Калькулятор денег и калорий спринт 2 в Яндекс.Практикум
## Спринт 2 - Калькулятор денег и калорий

### hw_python_oop -  Калькулятор денег и калорий Яндекс.Практикум

Создайте два калькулятора: для подсчёта денег и калорий.
Пользовательскую часть калькуляторов, их «лицо», писать не нужно, напишите только логику — отдельный класс для каждого из калькуляторов.

Калькулятор денег должен уметь:
- Сохранять новую запись о расходах методом add_record()
- Считать, сколько денег потрачено сегодня методом get_today_stats()
- Определять, сколько ещё денег можно потратить сегодня в рублях, долларах или евро — метод get_today_cash_remained(currency)
- Считать, сколько денег потрачено за последние 7 дней — метод get_week_stats()

Калькулятор калорий должен уметь:
- Сохранять новую запись о приёме пищи — метод add_record()
- Считать, сколько калорий уже съедено сегодня — метод get_today_stats()
- Определять, сколько ещё калорий можно/нужно получить сегодня — метод get_calories_remained()
- Считать, сколько калорий получено за последние 7 дней — метод get_week_stats()

У калькуляторов много пересекающихся функций: они должны уметь хранить какие-то записи (о еде или деньгах, но по сути - всё числа и даты), знать дневной лимит (сколько в день можно истратить денег или сколько калорий можно получить) и суммировать записи за конкретные даты.

Всю эту общую функциональность заложите в родительский класс Calculator, а от него унаследуйте классы CaloriesCalculator и CashCalculator.

Конструктор класса Calculator должен принимать один аргумент — число limit (дневной лимит трат/калорий, который задал пользователь). В конструкторе создайте пустой список, в котором потом будут храниться записи (назовите его records).

Чтобы было удобнее создавать записи, создайте для них отдельный класс Record. В нём сохраните:

- число amount (денежная сумма или количество килокалорий),
- дату создания записи date (передаётся в явном виде в конструктор, либо присваивается значение по умолчанию — текущая дата),
- комментарий comment, поясняющий, на что потрачены деньги или откуда взялись калории.

### Настройка и запуск на ПК

Клонируем проект:

```bash
git clone https://github.com/themasterid/hw_python_oop.git
```

или

```bash
git clone git@github.com:themasterid/hw_python_oop.git
```

Переходим в папку с проектом:

```bash
cd hw_python_oop
```

Устанавливаем виртуальное окружение:

```bash
python -m venv venv
```

Активируем виртуальное окружение:

```bash
source venv/bin/activate
```

Для деактивации виртуального окружения выполним (после работы):
```bash
deactivate
```

Устанавливаем зависимости:

```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Запускаем скрипт:

```bash
pip install -r requirements.txt
```

Примеры работы скрипта, добавив в конец секцию:

```python
if __name__ == "__main__":
    limit = 1000
    cash_calculator = CashCalculator(limit)
    calories_calculator = CaloriesCalculator(limit)

    # записи для денег
    r1 = Record(amount=145, comment='кофе')
    r2 = Record(amount=300, comment='Серёге за обед')
    r3 = Record(
        amount=3000,
        comment='Бар на Танин день рождения',
        date='08.11.2022')

    # записи для калорий
    r4 = Record(
        amount=118,
        comment='Кусок тортика. И ещё один.')
    r5 = Record(
        amount=84,
        comment='Йогурт.')
    r6 = Record(
        amount=1140,
        comment='Баночка чипсов.',
        date='24.02.2019')

    cash_calculator.add_record(r1)
    cash_calculator.add_record(r2)
    cash_calculator.add_record(r3)

    calories_calculator.add_record(r4)
    calories_calculator.add_record(r5)
    calories_calculator.add_record(r6)

    # вывод результатов
    print(cash_calculator.get_today_cash_remained('rub'))
    print(calories_calculator.get_calories_remained())
```

Получим:

```bash
На сегодня осталось 555.0 руб
Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более 798 кКал
```

Для запуска тестов выполним:

```bash
pytest
```

Получим:

```bash
pytest
======================================= test session starts =======================================
platform win32 -- Python 3.10.5, pytest-6.2.5, py-1.11.0, pluggy-0.13.1 -- ..\hw_python_oop\venv\Scripts\python.exe
rootdir: ...\hw_python_oop, configfile: pytest.ini, testpaths: tests/
collected 20 items

tests/test_homework.py::TestRecord::test_init[kwargs0] PASSED                                [  5%] 
tests/test_homework.py::TestRecord::test_init[kwargs1] PASSED                                [ 10%]
tests/test_homework.py::TestCalculator::test_init PASSED                                     [ 15%] 
tests/test_homework.py::TestCalculator::test_add_record PASSED                               [ 20%] 
tests/test_homework.py::TestCalculator::test_get_today_stats PASSED                          [ 25%] 
tests/test_homework.py::TestCalculator::test_get_week_stats PASSED                           [ 30%]
tests/test_homework.py::TestCalculator::test_get_calories_remained PASSED                    [ 35%] 
tests/test_homework.py::TestCalculator::test_get_today_cash_remained PASSED                  [ 40%] 
tests/test_homework.py::TestCaloriesCalculator::test_init PASSED                             [ 45%] 
tests/test_homework.py::TestCaloriesCalculator::test_get_calories_remained PASSED            [ 50%] 
tests/test_homework.py::TestCashCalculator::test_init PASSED                                 [ 55%] 
tests/test_homework.py::TestCashCalculator::test_get_today_cash_remained[0-usd] PASSED       [ 60%] 
tests/test_homework.py::TestCashCalculator::test_get_today_cash_remained[0-eur] PASSED       [ 65%] 
tests/test_homework.py::TestCashCalculator::test_get_today_cash_remained[0-rub] PASSED       [ 70%] 
tests/test_homework.py::TestCashCalculator::test_get_today_cash_remained[1-usd] PASSED       [ 75%] 
tests/test_homework.py::TestCashCalculator::test_get_today_cash_remained[1-eur] PASSED       [ 80%] 
tests/test_homework.py::TestCashCalculator::test_get_today_cash_remained[1-rub] PASSED       [ 85%] 
tests/test_homework.py::TestCashCalculator::test_get_today_cash_remained[-1-usd] PASSED      [ 90%]
tests/test_homework.py::TestCashCalculator::test_get_today_cash_remained[-1-eur] PASSED      [ 95%] 
tests/test_homework.py::TestCashCalculator::test_get_today_cash_remained[-1-rub] PASSED      [100%] 

======================================= 20 passed in 0.08s ======================================== 
```

# Подробнее о формате вывода

Метод get_calories_remained() калькулятора калорий должен возвращать ответы:
- «Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более N кКал», если лимит limit не достигнут,
- «Хватит есть!», если лимит достигнут или превышен,

Метод get_today_cash_remained(currency) денежного калькулятора должен принимать на вход код валюты: одну из строк "rub", "usd" или "eur". Возвращает он сообщение о состоянии дневного баланса в этой валюте, округляя сумму до двух знаков после запятой (до сотых):
- «На сегодня осталось N руб/USD/Euro» — в случае, если лимит limit не достигнут,
- «Денег нет, держись», если лимит достигнут,
- «Денег нет, держись: твой долг - N руб/USD/Euro», если лимит превышен.

Курс валют укажите константами USD_RATE и EURO_RATE, прямо в теле класса CashCalculator. Какой курс вы укажете — не так важно, выберите любой, похожий на правду. Значения обменного курса можно посмотреть, например, на главной странице Яндекса https://yandex.ru

Автор: [Дмитрий Клепиков](https://github.com/themasterid) :+1:
