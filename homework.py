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

    def add_record(self, obj: Record) -> list:
        return self.records.append(obj)

    def get_today_stats(self) -> Union[int, float]:
        self.today = dt.date.today()
        return sum(
            day.amount for day in self.records
            if day.date == self.today)

    def get_week_stats(self) -> Union[int, float]:
        self.today = dt.date.today()
        offset_week: dt.date = self.today - dt.timedelta(days=7)
        return sum(
            day.amount for day in self.records
            if offset_week <= day.date <= self.today)

    def get_limit_today(self) -> Union[int, float]:
        return self.limit - self.get_today_stats()


class CaloriesCalculator(Calculator):
    """Дочерний класс калькулятора калорий."""

    def get_calories_remained(self) -> str:
        limit_today = self.get_limit_today()
        if limit_today > 0:
            return ('Сегодня можно съесть что-нибудь ещё, '
                    'но с общей калорийностью не более'
                    f' {limit_today} кКал')
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

        cash_tday = round(
            abs(limit_today / money[currency][0]),
            self.CALC_ACCURACY)

        resault = f"{cash_tday} {money[currency][1]}"

        if limit_today > 0:
            return f'На сегодня осталось {resault}'
        return f'Денег нет, держись: твой долг - {resault}'
