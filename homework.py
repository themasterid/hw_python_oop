import datetime as dt
from typing import Optional, Union

DATE_FMT: str = '%d.%m.%Y'


class Record:
    """Класс для хранения значений."""

    def __init__(
        self,
        amount: int,
        comment: str,
        date: Optional[str] = None
    ) -> None:
        self.amount = amount
        self.comment = comment
        if date is not None:
            self.date = dt.datetime.strptime(date, DATE_FMT).date()
        else:
            self.date = dt.datetime.now().date()


class Calculator:
    """Базовый класс калькулятора калорий и денег."""

    def __init__(self, limit: Union[float, int]):
        self.limit = limit
        self.records: list = []

    def add_record(self, record: Record) -> None:
        self.records.append(record)

    def get_today_stats(self) -> Union[int, float]:
        today = dt.date.today()
        return sum(
            day.amount for day in self.records
            if day.date == today)

    def get_week_stats(self) -> Union[int, float]:
        today = dt.date.today()
        offset_week = today - dt.timedelta(days=7)
        return sum(
            day.amount for day in self.records
            if offset_week <= day.date <= today)

    def get_limit_today(self) -> Union[int, float]:
        return self.limit - self.get_today_stats()


class CaloriesCalculator(Calculator):
    """Дочерний класс калькулятора калорий."""

    def get_calories_remained(self) -> str:
        limit_today = self.get_limit_today()
        if limit_today > 0:
            return ('Сегодня можно съесть что-нибудь ещё, но с общей '
                    f'калорийностью не более {limit_today} кКал')
        return 'Хватит есть!'


class CashCalculator(Calculator):
    """Дочерний класс калькулятора денег."""

    USD_RATE: float = 72.0
    EURO_RATE: float = 86.0
    RUB_RATE: float = 1.0
    CALC_ACCURACY: int = 2

    def get_today_cash_remained(self, currency: str) -> str:

        money: dict = {
            'rub': (self.RUB_RATE, 'руб'),
            'usd': (self.USD_RATE, 'USD'),
            'eur': (self.EURO_RATE, 'Euro')
        }

        if currency not in money:
            return '<выбрана неверная валюта>'

        limit_today = self.get_limit_today()

        if limit_today == 0:
            return 'Денег нет, держись'

        rate_m, name_money = money[currency]

        cash_today = round(abs(limit_today) / rate_m, self.CALC_ACCURACY)

        if limit_today > 0:
            return f'На сегодня осталось {cash_today} {name_money}'
        return f'Денег нет, держись: твой долг - {cash_today} {name_money}'


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
