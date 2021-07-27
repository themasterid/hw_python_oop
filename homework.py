import datetime
from typing import Any


class Record:
    """Класс запись занчений."""

    def __init__(self, amount: int, comment: str, date: str=datetime.date.today()): #datetime.date.today()
        self.amount = amount
        self.comment = comment
        self.date = date
        self.records: list = list()

    def add_record(self, obj):
        self.obj = obj
        self.records.append(self.obj)


class Calculator:
    """Базовый класс калькулятора колорий."""
    def __init__(self, limit):
        self.limit = limit
        self.records: list = list()

    def add_record(self, obj):
        self.obj = obj
        self.records.append(self.obj)

    def get_today_stats(self):
        count_today = 0
        for i in self.records:
            if i.date == datetime.date.today():
                count_today += i.amount
        print(count_today)

    def get_week_stats(self):
        return '2000'


class CaloriesCalculator(Calculator):
    """Класс калькулятора колорий."""
    def __init__(self, limit):
        self.limit = limit
        self.records: list = list()

    def get_calories_remained(self):
        count_today = 0
        for i in self.records:
            if i.date == datetime.date.today():
                count_today += i.amount
        return count_today


class CashCalculator(Calculator):
    """Класс калькулятора денег. 'rub', 'usd' или 'eur'."""
    USD_RATE = 424.60
    EURO_RATE = 500.90

    def __init__(self, limit):
        self.limit = limit
        self.records: list = list()

    def get_today_cash_remained(self, currency: str):
        cash_t = {"usd": 73.75, "rub": 1, "eur": 87.25}
        self.limittoday = self.limit
        self.currency = currency

        for i in self.records:
            if i.date == datetime.date.today():
                self.limittoday -= i.amount

        if self.limittoday > 0:
            return 'На сегодня осталось {} {}'.format(
                round(self.limittoday / cash_t[currency] * cash_t['rub'], 2),
                self.currency)
        elif self.limittoday == 0:
            return 'Денег нет, держись'
        else:
            return 'Денег нет, держись: твой долг - {0} {1}'.format(
                round((self.limittoday / cash_t[currency]) * cash_t['rub'], 2),
                self.currency)


# создадим калькулятор денег с дневным лимитом 1000
cash_calculator = CashCalculator(2500)

# дата в параметрах не указана,
# так что по умолчанию к записи
# должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=1000, comment='Тестовый коммент'))
# и к этой записи тоже дата должна добавиться автоматически
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=1000,
                                  comment='Тестовый коммент',
                                  date='01.09.201'))

print(cash_calculator.get_today_cash_remained('eur'))
# должно напечататься
# На сегодня осталось 555 руб 
